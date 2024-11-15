#!/usr/bin/env python3
""" Process notebooks, output download and JupyterLite versions.

There are two outputs:

* Notebooks for download
* Notebooks for inclusion in JupyterLite output.

For both sets of notebooks:

* Process quarto cross-references to be relative to corresponding HTML output
  page.  This uses the built HTML in the output directory defined in the given
  ``_quarto.yml`` file.  For each notebook, we can work out the corresponding
  HTML page by looking for the matching references in the HTML sources.  For
  example, if the notebook has a reference to ``#sec-my-heading``, then we can
  find a link to ``#sec-my-heading`` in the HTML sources.  By previously
  parsing the HTML sources we can make sure that all references to
  ``#sec-my-heading`` become ``my_page.html#sec-my-heading``, and therefore we
  know that any reference to ``#sec-my-page`` is from ``my_page.html``.

For the download notebooks:

* Replace any relative page URLs to absolute URLs relative to main site.

For the JupyterLite (JL) notebooks:

* Create JL notebook output directory.
* Copy all directories in input notebook directory to JL output directory.
* Replace local kernel with JL kernel specified in metadata.
* If url_data_root specified, replace local file with URL, add message.
* Prefix any site URLs to be relative to the eventual JL output directory.
* Write notebooks with extension given in Quarto config
  ``noteout.interact-nb-suffix``.
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from copy import deepcopy
from functools import partial
from pathlib import Path
import re
import shutil
from urllib.parse import urlparse
from zipfile import ZipFile

from bs4 import BeautifulSoup as BS
import jupytext
import yaml


def cell_gen(nb, ctype):
    """ Generator for notebook cells
    """
    for cell in nb['cells']:
        if cell['cell_type'] == ctype:
            yield cell


class NBProcessor:

    _JL_JSON_FMT = r'''\
    {{
    "jupyter-lite-schema-version": 0,
    "jupyter-config-data": {{
        "contentsStorageName": "rss-{language}"
    }}
    }}
    '''

    # Find data read.
    _READ_FMT = r'''^(?P<indent>\s*)
    (?P<equals>\w+\s*{equal_re}\s*)
    (?P<read_func>{read_re}\w+\(
    ['"])
    (?P<fname>.*?)
    (?P<closequote>['"]
    \))
    '''

    PY_READ_RE = re.compile(
        _READ_FMT.format(equal_re='=', read_re=r'pd\.read_'),
        flags=re.MULTILINE | re.VERBOSE)

    R_READ_RE = re.compile(
        _READ_FMT.format(equal_re='<-', read_re=r'read\.'),
        flags=re.MULTILINE | re.VERBOSE)

    # Glob to use in searching for HTML files.
    html_globber = '*.html'

    # Attributes to search for in HTML for Quarto cross-ref.
    xref_attrs = {'class': 'quarto-xref'}

    def __init__(self, quarto_config, jl_out_path):
        self.quarto_config = Path(quarto_config)
        self.jl_out_path = Path(jl_out_path)
        self.source_path = self.quarto_config.parent
        self.quarto_vars = yaml.safe_load(self.quarto_config.read_text())
        self._noteout_config = self.quarto_vars['noteout']
        self._proc_config = self.quarto_vars['processing']
        self.book_path = self.source_path / self.quarto_vars['project']['output-dir']
        self._nb_in_path = self.book_path / self._noteout_config['nb-dir']
        self._nb_in_suffix='.' + self._noteout_config['nb-format']
        self.language = self._proc_config['language']
        self._nb_regex = (self.PY_READ_RE if self.language == 'python' else
                          self.R_READ_RE)
        self._jl_out_suffix = self._noteout_config .get('interact-nb-suffix',
                                                         self._nb_in_suffix)
        self._xrefs = None

    def _copy_in_dirs(self, out_path):
        out_path.mkdir(exist_ok=True, parents=True)
        for path in self._nb_in_path.glob('*'):
            if path.is_dir():
                shutil.copytree(path, out_path / path.name, dirs_exist_ok=True)

    def read_nbs(self):
        nbs_out = []
        for path in self._nb_in_path.glob('*' + self._nb_in_suffix):
            nb = jupytext.read(path)
            nbs_out.append((path, nb))
        return nbs_out

    def _process_nbs(self, nbs_in, funcs):
        nbs_out = []
        for path, nb in nbs_in:
            for func in funcs:
                nb = func(deepcopy(nb))
            nbs_out.append((path, nb))
        return nbs_out

    def _write_nbs(self, nbs_out, out_path, out_suffix):
        for nb_path, nb in nbs_out:
            out_root = out_path / nb_path.stem
            jupytext.write(nb, out_root.with_suffix(out_suffix))

    def _rezip_zips(self, out_path):
        for zf_path in out_path.glob('*.zip'):
            self._rezip_zip(zf_path)

    def _rezip_zip(self, zf_path):
        zf_dir = zf_path.parent
        with ZipFile(zf_path, 'r') as zf:
            paths = zf.namelist()
        with ZipFile(zf_path, "w") as zf:
            for path in paths:
                zf.write(zf_dir / path, path)

    def fix_kernels(self, nb):
        nb['metadata']['kernelspec'] = {
            'name': self._proc_config['kernel-name'],
            'display_name': self._proc_config['kernel-display']}
        return nb

    def fix_data_source(self, nb):
        url_data_root = self._proc_config.get('interact-data-root', None)
        if url_data_root:
            nb = self._path_to_url(nb, url_data_root)
        return nb

    def fix_xrefs(self, nb):
        for cell in cell_gen(nb, 'markdown'):
            src_soup = self._get_soup(cell['source'])
            for sxr in self._get_xrefs(src_soup):
                if (matching_xr := self.xrefs.get(sxr['href'])):
                    sxr.replace_with(matching_xr)
            cell['source'] = str(src_soup)
        return nb

    def prefix_xref(self, nb, prefix):
        for cell in cell_gen(nb, 'markdown'):
            src_soup = self._get_soup(cell['source'])
            for sxr in self._get_xrefs(src_soup):
                sxr['href'] = f"{prefix}{sxr['href']}"
            cell['source'] = str(src_soup)
        return nb

    @property
    def xrefs(self):
        if self._xrefs is None:
            self._xrefs = self._web2xrefs()
        return self._xrefs

    def _web2xrefs(self):
        """ Parse HTML files at HTML output path for cross-references.

        Returns
        -------
        xrefs : dict
            Dictionary of cross-references. Keys are anchor references,
            starting with ``#`` followed by the Quarto reference - e.g.
            ``#sec-my-heading``.   Values are the HTML tags, where the HREFs
            are always relative to the containing page.
        """
        all_xrefs = {}
        for page_path in self.book_path.glob(self.html_globber):
            from_root = page_path.relative_to(self.book_path)
            soup = self._get_soup(page_path.read_text())
            xrefs = self._get_xrefs(soup)
            for xr in self._relativize_xrefs(xrefs, from_root):
                #** Consider case of xrefs without anchor.
                if '#' in xr['href']:
                    key = '#' + xr['href'].split('#')[1]
                    all_xrefs[key] = xr
        return all_xrefs

    def _relativize_xrefs(self, xrefs, from_root):
        """ Convert `xrefs` to page-relative.

        Parameters
        ----------
        xrefs : list
            List of a href HTML tags containing cross-references.
        from_root :class:`Path`
            Path to containing page, relative to website directory.

        Returns
        -------
        soup : :class:`BeautifulSoup` object
        xrefs : dict
            Dictionary of cross-references.
        """
        name = '/'.join(from_root.parts)
        for xr in xrefs:
            if xr['href'].startswith('#'):
                xr['href'] = f"{name}{xr['href']}"
        return xrefs

    def _get_soup(self, html_text):
        return BS(html_text, 'html.parser')

    def _get_xrefs(self, soup):
        return soup.find_all( 'a', attrs=self.xref_attrs)

    def _path_to_url(self, nb, root_url):
        out_nb = deepcopy(nb)

        def _read_re_replace(m):
            d = m.groupdict()
            d['fname'] = Path(d['fname']).name
            return ('''\
{indent}# Read data from web URL instead of local data directory
{indent}# (so that notebook works in online version).
{indent}{equals}{read_func}{root_url}/{fname}{closequote}'''
                .format(**d, root_url=root_url))

        for cell in cell_gen(out_nb, 'code'):
            cell['source'] = self._nb_regex.sub(
                _read_re_replace, cell['source'])
        return out_nb

    def _book_base(self):
        book_path = urlparse(self._noteout_config['book-url-root']).path
        return '/' + book_path.lstrip('/')

    def process(self):
        fixed_nbs = self._process_nbs(self.read_nbs(), (self.fix_xrefs,))
        self._write_downloads(fixed_nbs)
        self._write_jls(fixed_nbs)

    def _write_downloads(self, fixed_nbs):
        dl_prefix = self._noteout_config['book-url-root'] + '/'
        dl_nbs = self._process_nbs(
            fixed_nbs,
            (partial(self.prefix_xref, prefix=dl_prefix),))
        self._write_nbs(dl_nbs, self._nb_in_path, self._nb_in_suffix)
        self._rezip_zips(self._nb_in_path)

    def _write_jls(self, fixed_nbs):
        self._copy_in_dirs(self.jl_out_path)
        jl_prefix = self._book_base() + '/'
        jl_nbs = self._process_nbs(fixed_nbs, (
            self.fix_kernels,
            self.fix_data_source,
            partial(self.prefix_xref, prefix=jl_prefix)))
        self._write_nbs(jl_nbs, self.jl_out_path, self._jl_out_suffix)
        (self.jl_out_path / 'jupyter-lite.json').write_text(
            self._JL_JSON_FMT.format(**self._proc_config))


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('quarto_config',
                        help='Quarto configuration file')
    parser.add_argument('jl_output_dir',
                        help='Output directory for JupyterLab notebooks')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    nbp = NBProcessor(args.quarto_config, args.jl_output_dir)
    nbp.process()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
""" Process notebooks

* Copy all files in given directory.
* Write notebooks with given extension.
* Replace local kernel with Pyodide kernel in metadata.
* If url_data_root specified, replace local file with URL, add message.
* Backport crossreferences from HTML output.
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from copy import deepcopy
from pathlib import Path
import re
import shutil

import jupytext
import yaml


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

    def __init__(self, quarto_config, output_dir):
        self.quarto_config = Path(quarto_config)
        self.source_path = self.quarto_config.parent
        self.quarto_vars = yaml.safe_load(self.quarto_config.read_text())
        self._noteout_config = self.quarto_vars['noteout']
        self.nb_in_path = self.source_path / self._noteout_config['nb-dir']
        self._proc_config = self.quarto_vars['processing']
        self.language = self._proc_config['language']
        self.nb_regex = (self.PY_READ_RE if self.language == 'python' else
                         self.R_READ_RE)
        self.out_path = Path(output_dir)
        self.out_suffix = self._noteout_config['url_nb_suffix']

    def copy_dirs(self):
        self.out_path.mkdir(exist_ok=True, parents=True)
        for path in self.nb_in_path.glob('*'):
            if path.is_dir():
                shutil.copytree(path,
                                self.out_path / path.name,
                                dirs_exist_ok=True)

    def process_nbs(self):
        in_nb_suffix='.' + self._noteout_config['nb-format']
        for path in self.nb_in_path.glob('*' + in_nb_suffix):
            nb = jupytext.read(path)
            out_root = self.out_path / path.stem
            nb = self.process_nb(out_root, nb)
            jupytext.write(nb, out_root.with_suffix(self.out_suffix))

    def process_nb(self, out_root, nb):
        pconfig = self._proc_config
        nb['metadata']['kernelspec'] = {
            'name': pconfig['kernel-name'],
            'display_name': pconfig['kernel-display']
        }
        url_data_root=pconfig.get('url-data-root', None)
        if url_data_root:
            nb = self._path_to_url(nb, url_data_root)
        return nb

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

        for cell in out_nb['cells']:
            if cell['cell_type'] != 'code':
                continue
            cell['source'] = self.nb_regex.sub(
                _read_re_replace, cell['source'])
        return out_nb

    def write_jl_config(self):
        (self.out_path / 'jupyter-lite.json').write_text(
            self._JL_JSON_FMT.format(**self._proc_config))

    def process(self):
        self.copy_dirs()
        self.process_nbs()
        self.write_jl_config()


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('quarto_config',
                        help='Quarto configuration file')
    parser.add_argument('output_dir',
                        help='Directory to which to output notebooks')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    NBProcessor(args.quarto_config, args.output_dir).process()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from copy import deepcopy
import os.path as op
from pathlib import Path
import re
import shutil

import jupytext

# Find data read
READ_RE = re.compile(
    r'''^(?P<indent>\s*)
    (?P<equals>\w+\s*(=|<-)\s*)
    (?P<read_func>(pd\.)*read[._]\w+\(
    ['"])
    (?P<fname>.*?)
    (?P<closequote>['"]
    \))
    ''',
    flags=re.MULTILINE | re.VERBOSE)


def path_to_url(nb, root_url):
    out_nb = deepcopy(nb)

    def _read_re_replace(m):
        d = m.groupdict()
        d['fname'] = Path(d['fname']).name
        return ('{indent}{equals}{read_func}{root_url}/{fname}{closequote}'
                .format(**d, root_url=root_url))

    for cell in out_nb['cells']:
        if cell['cell_type'] != 'code':
            continue
        cell['source'] = READ_RE.sub(_read_re_replace, cell['source'])
    return out_nb


def process_dir(input_dir, output_dir, nb_suffix, kernel_name, kernel_dname,
                url_root=None):
    if not nb_suffix.startswith('.'):
        nb_suffix = '.' + nb_suffix
    output_dir.mkdir(exist_ok=True, parents=True)
    for path in input_dir.glob('*'):
        if path.is_dir():
            shutil.copytree(path, output_dir / path.name, dirs_exist_ok=True)
            continue
        if path.suffix != nb_suffix:
            continue
        nb = jupytext.read(path)
        nb['metadata']['kernelspec'] = {
            'name': kernel_name,
            'display_name': kernel_dname}
        if url_root:
            nb = path_to_url(nb, url_root)
        jupytext.write(nb, output_dir / (path.stem + '.ipynb'))


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('input_dir',
                        help='Directory containing notebooks to process')
    parser.add_argument('output_dir',
                        help='Directory to which to output notebooks')
    parser.add_argument('nb_suffix',
                        help='suffix for input notebooks ("Rmd" or "ipynb")')
    parser.add_argument('kernel_name',
                        help='Name for Jupyter kernel')
    parser.add_argument('kernel_dname',
                        help='Display name for Jupyter kernel')
    parser.add_argument('--url-root',
                        help='URL root to data (for URL data loads)')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    print(args.nb_suffix)
    process_dir(Path(args.input_dir),
                Path(args.output_dir),
                args.nb_suffix,
                args.kernel_name,
                args.kernel_dname,
                args.url_root)


if __name__ == '__main__':
    main()

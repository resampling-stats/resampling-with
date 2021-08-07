#!/usr/bin/env python
""" Set parameters in _quarto.yml
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter

QUARTO_TEMPLATE = '_quarto.yml.template'
VARS_TEMPLATE = '_variables.yml.template'

def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('version',
                        help='One of "python" or "r"')
    return parser


def set_version(version):
    version = version.lower()
    language = version.capitalize()
    other_language = 'Python' if language == 'R' else 'R'
    for fname in (QUARTO_TEMPLATE, VARS_TEMPLATE):
        with open(fname, 'rt') as fobj:
            fmt_str = fobj.read()
        out_fname = fname.replace('.template', '')
        with open(out_fname, 'wt') as fobj:
            fobj.write(fmt_str.format(**locals()))


def main():
    parser = get_parser()
    args = parser.parse_args()
    set_version(args.version)


if __name__ == '__main__':
    main()

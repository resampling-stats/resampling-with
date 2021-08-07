#!/usr/bin/env python
""" Set parameters in _quarto.yml
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter

TEMPLATE_FNAME = '_quarto.yml.template'

def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('version',
                        help='One of "python" or "r"')
    return parser


def set_version(version):
    version = version.lower()
    with open(TEMPLATE_FNAME, 'rt') as fobj:
        fmt_str = fobj.read()
    with open("_quarto.yml", 'wt') as fobj:
        fobj.write(fmt_str.format(version=version))


def main():
    parser = get_parser()
    args = parser.parse_args()
    set_version(args.version)


if __name__ == '__main__':
    main()

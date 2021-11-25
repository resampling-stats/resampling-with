#!/usr/bin/env python
""" Set parameters in _quarto.yml
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import yaml


QUARTO_TEMPLATE = '_quarto.yml.template'

LANG_VARS_SOURCE = 'variables.yml'
LANG_VARS_TARGET = '_variables.yml'

QUARTO_VARS = {
    'r': {
        'filter_divspans': "['python']",
        'nb_flatten_divspans': "['+', 'r']",
        'nb_format': 'Rmd'
    },
    'python': {
        'filter_divspans': "['r']",
        'nb_flatten_divspans': "['+', 'python']",
        'nb_format': 'ipynb'
    }
}


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('version',
                        help='One of "python" or "r"')
    return parser


def fill_template(fn, version):
    version = version.lower()
    variables = QUARTO_VARS[version] | {'version': version}

    with open(fn, 'rt') as fobj:
        fmt_str = fobj.read()
    out_fname = fn.replace('.template', '')
    with open(out_fname, 'wt') as fobj:
        fobj.write(fmt_str.format(**variables))


def main():
    parser = get_parser()
    args = parser.parse_args()
    fill_template(QUARTO_TEMPLATE, args.version)

    vars = yaml.load(open(LANG_VARS_SOURCE, 'r'), Loader=yaml.FullLoader)
    with open(LANG_VARS_TARGET, 'w') as f:
        yaml.dump(vars[args.version], f)


if __name__ == '__main__':
    main()

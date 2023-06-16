#!/usr/bin/env python
""" Set parameters in _quarto.yml
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import yaml


QUARTO_TEMPLATE = '_quarto.yml.template'

LANG_VARS_SOURCE = 'text_variables.yml'
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
    parser = ArgumentParser(
        description=__doc__,  # Usage from docstring
        formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'version',
        choices=['python', 'r'],
        help='Book version'
    )
    parser.add_argument('-o', '--output', help='Destination file', default="_quarto.yml")
    return parser


def fill_template(infile : str, outfile : str, data: dict):
    with open(infile) as f:
        template = f.read()

    with open(outfile, 'w') as f:
        f.write(
            template.format(**data)
        )


def main():
    parser = get_parser()
    args = parser.parse_args()
    lang = args.version
    print(f"Writing configuration to {args.output}...")
    fill_template(
        QUARTO_TEMPLATE,
        args.output,
        {'version': args.version, **QUARTO_VARS[args.version]}
    )

    print("Writing _variables.yml...")
    vars = yaml.load(open(LANG_VARS_SOURCE, 'r'), Loader=yaml.FullLoader)
    with open(LANG_VARS_TARGET, 'w') as f:
        yaml.dump(vars[args.version], f)


if __name__ == '__main__':
    main()

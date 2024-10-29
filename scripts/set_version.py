#!/usr/bin/env python
""" Set parameters in _quarto-{lang}.yml and _variables.yml
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path
import yaml

# Template that fill be format-filled to write output file.
QUARTO_TEMPLATE = '_quarto.yml.template'
# Config file with variables specific and not-specific to build.
CONFIG_VARS = 'config_variables.yml'
# Text variables for each version.
LANG_VARS_SOURCE = 'text_variables.yml'
# Output file for variables.
LANG_VARS_TARGET = '_variables.yml'


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('version',
                        choices=['python', 'r'],
                        help='Book version')
    parser.add_argument('-o', '--output',
                        help='Destination file',
                        default="_quarto.yml")
    return parser


def recursive_fill_vars(fname, start_dict):
    txt = Path(fname).read_text()
    vars1 = {**yaml.safe_load(txt), **start_dict}
    txt2 = txt.format(**vars1)
    return yaml.safe_load(txt2)


def main():
    parser = get_parser()
    args = parser.parse_args()
    version = args.version.lower()
    start_dict = {'version': version}
    config_vars = recursive_fill_vars(CONFIG_VARS, start_dict)
    # Put matching version keys at top level.
    config_vars.update(config_vars[version])
    print(f"Writing configuration to {args.output}...")
    out_config = Path(QUARTO_TEMPLATE).read_text().format(**config_vars)
    Path(args.output).write_text(out_config)
    print("Writing _variables.yml...")
    vars = yaml.safe_load(Path(LANG_VARS_SOURCE).read_text())
    Path(LANG_VARS_TARGET).write_text(yaml.safe_dump(vars[version]))


if __name__ == '__main__':
    main()

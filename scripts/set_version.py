#!/usr/bin/env python
""" Set parameters in _quarto-{lang}.yml and _variables.yml
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path
from subprocess import check_output
import yaml

# Template that fill be format-filled to write output file.
QUARTO_TEMPLATE = '_quarto.yml.template'
# Config file with variables specific and not-specific to build.
CONFIG_VARS = 'config_variables.yml'
# Text variables for each version.
LANG_VARS_SOURCE = 'text_variables.yml'
# Output file for variables.
LANG_VARS_TARGET = '_variables.yml'

OTHER_VERSIONS = {'r': 'python', 'python': 'r'}


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


def version_to_top(var_dict, version, other_version):
    version_dict = var_dict.pop(version)
    var_dict.pop(other_version)
    return {**var_dict, **version_dict}


def get_edition():
    branch_name = check_output(['git', 'rev-parse',  '--abbrev-ref', 'HEAD'],
                               text=True).strip()
    return 'latest' if branch_name == 'main' else branch_name


def main():
    parser = get_parser()
    args = parser.parse_args()
    version = args.version.lower()
    other_version = OTHER_VERSIONS[version]
    start_dict = {'version': version,
                  'other-version': other_version,
                  'edition': get_edition()}
    config_vars = recursive_fill_vars(CONFIG_VARS, start_dict)
    config_vars = version_to_top(config_vars, version, other_version)
    print(f"Writing configuration to {args.output}...")
    out_config = Path(QUARTO_TEMPLATE).read_text().format(**config_vars)
    Path(args.output).write_text(out_config)
    print("Writing _variables.yml...")
    variables = recursive_fill_vars(LANG_VARS_SOURCE, config_vars)
    variables = version_to_top(variables, version, other_version)
    Path(LANG_VARS_TARGET).write_text(yaml.safe_dump(variables))


if __name__ == '__main__':
    main()

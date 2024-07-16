#!/usr/bin/env python3
""" Postprocess Quarto site for variables that have not been substituted.

Maybe relevant: `https://github.com/quarto-dev/quarto-cli/issues/8987`_.
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path
import re
import yaml

TEXT_EXTS = ('.html', '.json')

VAR_RE = re.compile(
    r'\{\{(<|&lt;)\svar\s+(?P<varname>\w+)\s+(>|&gt;)\}\}',
    flags=re.MULTILINE | re.VERBOSE)


def postprocess_site(build_path, var_conf, exts):

    def _var_replace(m):
        return var_conf[m.groupdict()['varname']]

    for path in build_path.glob('*'):
        if path.suffix not in exts:
            continue
        in_txt = path.read_text()
        out_txt = VAR_RE.sub(_var_replace, in_txt)
        if in_txt != out_txt:
            path.write_text(out_txt)


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('quarto_config',
                        help='Quarto configuration file')
    parser.add_argument('--var-config',
                        help='Quarto variable file')
    parser.add_argument('--build-dir',
                        help='Directory containing built files')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    source_path = Path(args.quarto_config).parent
    var_path = (Path(args.var_config) if args.var_config else
                source_path / '_variables.yml')
    with open(args.quarto_config, 'rt') as fobj:
        quarto_conf = yaml.load(fobj, Loader=yaml.FullLoader)
    build_path = (Path(args.build_dir) if args.var_config else
                  source_path / quarto_conf['project']['output-dir'])
    with open(var_path, 'rt') as fobj:
        var_conf = yaml.load(fobj, Loader=yaml.FullLoader)
    postprocess_site(build_path, var_conf, TEXT_EXTS)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
""" Show ::: blocks in .Rmd file
"""

from pathlib import Path
import re
import warnings
from argparse import ArgumentParser, RawDescriptionHelpFormatter


START_RE = re.compile(r'^:::+\s*\S+')
END_RE = re.compile(r'^:::+\s*$')


def level2prefixed(level, line):
    if level == 0:
        return line
    prefix = '|' * level
    return f'{prefix} {line}' if line else prefix


def mark_contents(contents):
    out_lines = []
    level = 0
    for i, line in enumerate(contents.splitlines()):
        if END_RE.match(line):
            level -= 1
        if level < 0:
            raise ValueError(
                f'Negative level at line no {i + 1}:\n"""\n{line}\n"""')
        out_lines.append(level2prefixed(level, line))
        if START_RE.match(line):
            level += 1
    if level != 0:
        warnings.warn('Unterminated block at end of file')
    return '\n'.join(out_lines)


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('notebook_fname',
                        help='Notebook filename')
    parser.add_argument('-0', '--out-fname',
                        help='Output filename for notebook with marked blocks')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    nb_path = Path(args.notebook_fname)
    out_path = (Path(args.out_fname) if args.out_fname is not None else
                nb_path.with_stem('_marked_' + nb_path.stem))
    contents = nb_path.read_text()
    marked = mark_contents(contents)
    out_path.write_text(marked)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
""" Hackish script to parse ResamplingStats programs from Rmd files
"""

from pathlib import Path
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import re


class NbParser:
    """ Parser for notebook
    """

    PROB_LINE_RE = re.compile(
        r'^`\s+(If )?([Pp]\()')
    PROGRAM_LINE_RE = re.compile(
        r'^`\s+([A-Z]+.*?)\s+`$')
    CONTINUATION_LINE_RE = re.compile(
        r'^`\s+(.*?)\s+`$')
    FILENAME_RE = re.compile(r'file "([A-Za-z0-9]+)"')
    FREE_FLOAT_RE = re.compile(r'(\s+)(\.\d+\s+)')
    one_indent = '    '

    def __init__(self, nb_fname):
        self.path = Path(nb_fname)
        self.contents = self.path.read_text()
        self.lines = tuple(self.contents.splitlines())

    def reset_parser(self):
        self.programs = {}
        self.state = 'text'
        self.reset_program()

    def reset_program(self):
        self.indent_level = 0
        self.program_lines = []
        self.start_line = None

    def finalize_program(self, line_no):
        program = {
            'code': '\n'.join(self.program_lines),
            'start_line': self.start_line,
            'end_line': line_no,
            'fname': str(self.path.name)}
        if (match := self.FILENAME_RE.search(program['code'])):
            name = match.groups()[0]
        else:
            name = f'{self.path.stem}_{len(self.programs):02d}'
        self.programs[name] = program
        self.reset_program()

    def append_code(self, line):
        # Replace e.g .2 with 0.2 (for Statistics101 parsing).
        line = self.FREE_FLOAT_RE.sub(r'\g<1>0\2', line)
        self.append_pline(line)

    def append_comment(self, line):
        self.append_pline("' " + line)

    def append_pline(self, line):
        self.program_lines.append(self.one_indent * self.indent_level + line)

    def parse(self):
        self.reset_parser()
        for line_no, line in enumerate(self.lines):
            self.parse_line(line_no, line)

    def parse_line(self, line_no, line):
        line = line.strip()
        if self.state == 'text':
            # This is a probability line, not a program line
            if (match := self.PROB_LINE_RE.match(line)):
                return
        if (match := self.PROGRAM_LINE_RE.match(line)):
            if self.state == 'text':
                self.start_line = line_no
            self.state = 'program-line'
            code = match.groups()[0]
            if code.startswith('END') and self.indent_level:
                self.indent_level -= 1
            self.append_code(code)
            # For subsequent lines.
            if code.startswith('REPEAT') or code.startswith('IF'):
                self.indent_level += 1
            return
        if self.state == 'program-line':
            if line == '':
                return
            if (match := self.CONTINUATION_LINE_RE.match(line)):
                code = match.groups()[0]
                # Stats101 interface does not allow continuation lines
                last_line = self.program_lines.pop()
                self.append_code(last_line + ' ' + code)
                return
            self.state = 'comment-para'
        if self.state == 'comment-para':
            if line == '':
                # This could be the end of the program, or
                # just the end of the paragraph.
                self.state = 'pending-end'
                return
            if line.startswith('![]'):  # An image, false positive
                self.state = 'aborted-comment'
                line_no -=1
            elif line != '':
                self.append_comment(line)
                return
        if self.state == 'pending-end':
            if line.startswith('Note:') or line.endswith('.'):
                # There's an extra Note: paragraph, or a single-sentence line.
                self.state = 'comment-para'
                self.program_lines.append('')
                self.append_comment(line)
                return
        if self.state != 'text':
            # We were parsing the program, but we've got to the end.
            self.finalize_program(line_no)
        self.state = 'text'
        if line.startswith('` '):  #  A crazy line in the exercises file.
            remaining = line.replace('`', '').strip()
            assert len(remaining) == 0

    def write_notebook(self, pth=None):
        if pth is None:
            pth = self.path
        lines = list(self.lines)
        for name, program in self.programs.items():
            start, stop = program['start_line'], program['end_line']
            n_padding = (stop - start - 1)
            code_contents = '\n'.join(
                ['',
                '<!--- Resampling stats file; Matlab syntax closeish -->',
                '',
                '```matlab',
                '',
                f'\' Program file: "{name}.rss"',
                '',
                program['code'],
                '```',
                ''])
            lines[start:stop] = [code_contents] + [None] * n_padding
        lines = [L for L in lines if L is not None]
        pth.write_text('\n'.join(lines) + '\n')

    def write_programs(self, out_pth):
        if not out_pth.is_dir():
            out_pth.mkdir()
        for name, program in self.programs.items():
            out_file_pth = out_pth / (name + '.rss')
            start_line, fname = program['start_line'], program['fname']
            header = (f'\'"{name}" from "{fname}" starting at line {start_line}')
            out_file_pth.write_text(
                '\n'.join([header, '', program['code']]))


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('notebook', nargs='+',
                        help='Notebooks to parse')
    parser.add_argument('-o', '--out-dir', default=str(Path()),
                        help='output directory for files')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    out_pth = Path(args.out_dir)
    for nb_fname in args.notebook:
        parser = NbParser(nb_fname)
        parser.parse()
        parser.write_notebook()
        parser.write_programs(out_pth)


if __name__ == '__main__':
    main()

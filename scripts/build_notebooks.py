#!/usr/bin/env python3
""" Build notebooks from build Markdown

* Extract notebooks from page Markdown.
* Convert to Jupyter Notebook.
"""

import os.path as op
import re
from argparse import ArgumentParser

import jupytext as jpt

NB_RE = re.compile(r'<!---\s+nb:(.*?)\s+-->$(.*?)^<!---\s+nb:end\s+-->$',
                   re.MULTILINE | re.DOTALL)


def extract_nb_md(page_contents):
    parsed = NB_RE.findall(page_contents)
    return {fname: text.strip() for fname, text in parsed}


def text2nb_text(nb_text):
    return jpt.writes(jpt.reads(nb_text, 'markdown'), 'ipynb')


def read_fname(fname):
    with open(fname, 'rt') as fobj:
        return fobj.read()


def rewrite_notebooks(page_contents, out_path):
    for fname, contents in extract_nb_md(page_contents).items():
        nb_text = text2nb_text(contents)
        fname = op.join(out_path, fname) if out_path else fname
        print('Writing', fname)
        with open(fname, 'wt') as fobj:
            fobj.write(nb_text)


def main():
    parser = ArgumentParser()
    parser.add_argument('md_fname', nargs='+')
    parser.add_argument('--out-path')
    args = parser.parse_args()
    if args.out_path is None:
        if len(args.md_fname) > 1:
            raise RuntimeError('Specify --out-path for more '
                               'than one input filename')
        args.out_path = op.dirname(args.md_fname[0])
    for md_fname in args.md_fname:
        contents = read_fname(md_fname)
        rewrite_notebooks(contents, args.out_path)


if __name__ == '__main__':
    main()

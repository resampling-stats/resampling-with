#!/usr/bin/env python3
""" Build notebooks from built Markdown.

* Extract notebooks from page Markdown.
* Convert to Jupyter or RMarkdown notebook.
"""

import os.path as op
import re
from argparse import ArgumentParser

import jupytext as jpt

# Stuff inside notebook delimiting markers
NB_RE = re.compile(r'<!---\s+nb:(.*?)\s+-->$(.*?)^<!---\s+nb:end\s+-->$',
                   re.MULTILINE | re.DOTALL)
# Stuff inside HTML (and Markdown) comment markers.
COMMENT_RE = re.compile(r'<!--.*?-->', re.MULTILINE | re.DOTALL)
# Start of fenced code block.
FENCE_START_RE = re.compile(r'^```\s*(\w+)$', re.MULTILINE)

FMT_RECODES = {'r': 'Rmd',
               'R': 'Rmd',
               'python': 'ipynb',
               'Python': 'ipynb'}


def extract_nb_md(page_contents):
    parsed = NB_RE.findall(page_contents)
    return {fname: text.strip() for fname, text in parsed}


def proc_text(nb_text):
    """ Process notebook GFM markdown
    """
    # Strip comments
    txt = COMMENT_RE.sub('', nb_text)
    # Modify code fencing to add curlies around fence arguments.
    # This converts from GFM Markdown fence blocks to RMarkdown fence blocks.
    return FENCE_START_RE.sub(r'```{\1}', txt)


def text2nb_text(nb_text, out_fmt):
    """ Process notebook GFM Markdown, write to notebook format `out_fmt`
    """
    txt = proc_text(nb_text)
    return jpt.writes(jpt.reads(txt, 'Rmd'), out_fmt)


def read_fname(fname):
    with open(fname, 'rt') as fobj:
        return fobj.read()


def rewrite_notebooks(page_contents, out_path, out_fmt):
    for fname, contents in extract_nb_md(page_contents).items():
        nb_text = text2nb_text(contents, out_fmt)
        fname = op.join(out_path, fname) if out_path else fname
        print('Writing', fname)
        with open(fname, 'wt') as fobj:
            fobj.write(nb_text)


def main():
    parser = ArgumentParser()
    parser.add_argument('md_fname', nargs='+')
    parser.add_argument('--out-path')
    parser.add_argument('--out-fmt', default='ipynb')
    args = parser.parse_args()
    if args.out_path is None:
        if len(args.md_fname) > 1:
            raise RuntimeError('Specify --out-path for more '
                               'than one input filename')
        args.out_path = op.dirname(args.md_fname[0])
    if args.out_fmt in FMT_RECODES:
        args.out_fmt = FMT_RECODES[args.out_fmt]
    for md_fname in args.md_fname:
        contents = read_fname(md_fname)
        rewrite_notebooks(contents, args.out_path, args.out_fmt)


if __name__ == '__main__':
    main()

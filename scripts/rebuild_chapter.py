#!/usr/bin/env python3
# Rebuild single chapter
# Useage example:
#  rebuild_chapter.py probability_theory_1a.Rmd --edition=r
#  rebuild_chapter.py sampling_variability.Rmd --edition=python

import os
import os.path as op
from shutil import rmtree
from subprocess import check_call
from argparse import ArgumentParser, RawDescriptionHelpFormatter

HERE = op.dirname(__file__)


def rebuild_chapter(rmd, edition, fmt):
    edition = edition.lower()
    if fmt.lower() == 'html':
        fmt = "bookdown::gitbook"
    elif fmt.lower() == "pdf":
        fmt = "bookdown::pdf_book"
    book_build_md = op.join(HERE, '..', f'{edition}-book', 'index.md')
    if not op.isfile(book_build_md):
        raise RuntimeError(
            "You need a full book build before building single chapters.\n"
            f"Run 'make {edition}-book' first.")
    book_source = op.join(HERE, '..', 'source')
    rmd_root = op.splitext(rmd)[0]
    cache_dir = op.join(book_source, '_bookdown_files', f'{rmd_root}_cache')
    if op.isdir(cache_dir):
        rmtree(cache_dir)
    config = f"_{edition}_bookdown.yml"
    os.environ['BOOK_ED'] = edition
    check_call(['Rscript', '-e',
                f"bookdown::preview_chapter('{rmd_root}.Rmd', "
                f"output='{fmt}', config_file='{config}')"],
               cwd=book_source)


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('rmd',
                        help='Rmd filename of chapter to rebuild')
    parser.add_argument('-e', '--edition', default='python',
                        help='Edition of book (Python or R)')
    parser.add_argument('-f', '--format', default='html',
                        help='Output format (html or pdf)')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    print(f"Building {args.rmd} for {args.edition} edition.")
    rebuild_chapter(args.rmd, args.edition, args.format)


if __name__ == '__main__':
    main()

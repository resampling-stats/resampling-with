""" Utilities for analyzing chapters
"""

from pathlib import Path
import re

ROOT_PTH = Path(__file__).parent.parent.resolve()
PDF_PTH = ROOT_PTH / 'unported'

YAML_HDR = re.compile(r'^---$.*^---$', re.S | re.M)
ED2_INFO = re.compile(r'^\s+ed2_fname\s*:\s*(.*)\s*$', re.M)

CHAPTERS = tuple(PDF_PTH.glob('??-Chap*.pdf'))
RMDS = tuple((ROOT_PTH / 'source').glob('*.Rmd'))
CHAPTER_NO_RE = re.compile(r'\d\d-Chap-(\d+)$')


def pth2chap_name(pth):
    pth = Path(pth)
    content = pth.read_text()
    match = YAML_HDR.search(content)
    if not match:
        raise RuntimeError(f'Cannot find YAML header in {pth}')
    match = ED2_INFO.search(match.group())
    if not match:
        raise RuntimeError(f'Cannot find ed2 info in {pth}')
    return match.groups()[0]


def chap_name4chap_no(chapter_number):
    chapter_number = int(chapter_number)
    for chapter in CHAPTERS:
        if not (match := CHAPTER_NO_RE.match(chapter.stem)):
            continue
        if int(match.groups()[0]) == chapter_number:
            return match.group()
            break
    else:
        raise RuntimeError(f'Could not find chapter {chapter_number}')


def pdf4chap_name(chap_name):
    return PDF_PTH / (chap_name + '.pdf')


def rmd4chap_name(chap_name):
    for rmd in RMDS:
        try:
            this_chap = pth2chap_name(rmd)
        except RuntimeError:
            continue
        if chap_name == this_chap:
            return rmd
    raise RuntimeError(f'No Rmd file for chapter {chap_name}')

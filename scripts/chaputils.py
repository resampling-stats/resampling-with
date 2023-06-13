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

_NAMES = """\
01-Preface preface_second
02-Intro intro
03-Afternote-1 dramatizing_resampling
04-Afternote-2 intro
05-Chap-1 resampling_method
06-Chap-2 basic_probability_1
07-Chap-3 basic_probability_2
08-Chap-4 probability_theory_1a
09-Chap-5 probability_theory_1b
10-Chap-6 probability_theory_2_compound
11-Chap-7 probability_theory_3
12-Chap-8 probability_theory_4_finite
13-Chap-9 sampling_variability
14-Chap-10 monte_carlo
15-Chap-11 inference_ideas
16-Chap-12 inference_intro
17-Chap-13 point_estimation
18-Chap-14 framing_questions
19-Chap-15 testing_counts_1
20-Chap-16 significance
21-Chap-17 testing_counts_2
22-Chap-18 testing_measured
23-Chap-19 testing_procedures
24-Chap-20 confidence_1
25-Chap-21 confidence_2
26-Chap-22 reliability_average
27-Chap-23 correlation_causation
28-Chap-24 how_big_sample
29-Chap-25 bayes_simulation
30-Exercise-sol exercise_solutions
Technical technical_note
acknow acknowlegements
""".splitlines()
RENAMES = dict([L.split(' ', 1) for L in _NAMES])


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

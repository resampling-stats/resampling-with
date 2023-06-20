""" Script to rename chapters, move to source directory

Run once, probably won't need to run again.
"""
import re
import os.path as op

in_sdir = 'unported'
out_sdir = 'source'

lines = """\
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
renames = [line.split(' ', 1) for line in lines]

header = """\
---
jupyter:
  jupytext:
    metadata_filter:
      notebook:
        additional: all
        excluded:
        - language_info
    text_representation:
      extension: .Rmd
      format_name: rmarkdown
      format_version: '1.0'
      jupytext_version: 0.8.6
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
resampling_with:
    ed2_fname: {}
---

"""

h1_re = re.compile(r'^([A-Z].*)\n===+\n', flags=re.M)
h2_re = re.compile(r'^([A-Z].*)\n--+\n', flags=re.M)

rmd_files = []
for f1, f2 in renames:
    in_fn = op.join(in_sdir, f1 + '.Rmd')
    out_fn = op.join(out_sdir, f2 + '.Rmd')
    with open(in_fn, 'rt') as fobj:
        contents = fobj.read()
    contents = h1_re.sub(r'# \1\n', contents)
    contents = h2_re.sub(r'## \1\n', contents)
    with open(out_fn, 'wt') as fobj:
        fobj.write(header.format(f1) + contents)
    rmd_files.append(f'    "{f2}.Rmd"')

print("Insert this into _*_bookdown.yml files")

print(',\n'.join(rmd_files))

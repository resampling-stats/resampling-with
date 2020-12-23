""" Collect, process, write table 1 from Zhou et al 2000
"""

import os.path as op
import re

import pdftotext

paper_fname = op.join(op.dirname(__file__),
                      '..', '..', '..',
                      'simon-book-files',
                      'zhou2000long.pdf')

with open(paper_fname, "rb") as f:
    page3 = pdftotext.PDF(f)[2]

table_data = re.search(r'^(Year\s+TP\s+.*)^Mean\s+', page3,
                       flags=re.M | re.S).groups()[0]
lines = table_data.splitlines()

header = ' '.join(lines[:3])
header = re.sub(r'NOÿ\s+3 -N', 'NO3_minus_N', header) 
header = re.sub(r'NH\+\s+4 -N', 'NH4_minus_N', header)
header = re.sub(r'NH\+\s+4 -N', 'NH4_minus_N', header)
header = re.sub('In.ow', 'Inflow', header)

table_text = header + '\n'.join(lines[3:])
table_csv = re.sub(' +', ',', table_text)

with open('lough_erne.csv', 'wt') as fobj:
    fobj.write(table_csv)

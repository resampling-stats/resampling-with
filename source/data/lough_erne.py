#!/usr/bin/env python3
""" Collect, process, write table 1 from Zhou et al 2000
"""

from pathlib import Path
import re

import pdftotext

import numpy as np
import pandas as pd

HERE = Path(__file__).parent

paper_fname = (HERE / '..' / '..' / '..' / 'simon-book-files' /
               'zhou2000long.pdf')

with open(paper_fname, "rb") as f:
    page3 = pdftotext.PDF(f)[2]

table_data = re.search(r'^(Year\s+TP\s+.*)^Mean\s+', page3,
                       flags=re.M | re.S).groups()[0]
lines = table_data.splitlines()

inflow_parsed = 'In¯ow'
inflow_ind = lines.index(inflow_parsed)
assert inflow_ind != -1

header = ' '.join(lines[:inflow_ind + 1])
header = re.sub(r'NOÿ\s+3 -N', 'NO3_minus_N', header) 
header = re.sub(r'NH\+\s+4 -N', 'NH4_minus_N', header)
header = re.sub(r'NH\+\s+4 -N', 'NH4_minus_N', header)
header = re.sub('In.ow', 'Inflow', header)
col_names = header.split()

data_lines = lines[inflow_ind + 1:]
while data_lines[0] == '':
    data_lines.pop(0)

cols = []
vals = []
for line in data_lines:
    if line == '':
        cols.append(vals)
        vals = []
        continue
    vals.append(line)
if vals:
    cols.append(vals)

table = pd.DataFrame(data = np.array(cols).T, columns=col_names)
table.to_csv(HERE / 'lough_erne.csv', index=None)

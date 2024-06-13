#!/usr/bin/env python3
""" Build draft correlation tables for correlation / causation chapter.
"""
from pathlib import Path

import numpy as np
import pandas as pd

rnd = np.random.default_rng()


def replace_val(part, val):
    vs = f' {val}'
    if len(vs) > len(part) - 1:
        raise ValueError(f'{vs} is too long to replace in {part}')
    return vs + ' ' * (len(part) - len(vs))


def prepend_row(tab_md, vals):
    lines = tab_md.splitlines()
    assert lines[0].startswith('+')
    L1 = lines[1]
    assert (L1[0], L1[-1]) == ('|', '|')
    parts = lines[1].split('|')[1:-1]
    new_parts = []
    for part, val in zip(parts, vals):
        new_parts.append(replace_val(part, val))
    L1 = '|'.join(new_parts)
    return '\n'.join([lines[0], f'|{L1}|'] + lines)


def footerize_table(tab_md, indices=(-2, -1)):
    lines = tab_md.splitlines()
    line_indices = [i for i, line in enumerate(lines)
                    if line[:2] in ('+-', '+=')]
    for to_footerize in indices:
        LI = line_indices[to_footerize]
        lines[LI] = lines[LI].replace('-', '=')
    return '\n'.join(lines)


def write_footerized(df, path, prepended=None):
    tab_md = df.to_markdown(index=None, tablefmt='grid', numalign="left")
    if prepended is not None:
        tab_md = prepend_row(tab_md, prepended)
    print(f'Writing {path}')
    Path(path).write_text(footerize_table(tab_md))


df = pd.read_csv('data/athletic_iq.csv')
ath = np.array(df['athletic_score'])
iq = np.array(df['iq_score'])

siq = np.sort(iq)
athi = np.argsort(ath)
iq_pos = siq[athi]
iq_neg = siq[athi[::-1]]

out = pd.DataFrame(
    data={'Athletic score': ath,
          'Hypothetical\nIQ pos': iq_pos,
          'Col 1 x Col 2': ath * iq_pos,
          'Hypothetical\nIQ neg': iq_neg,
          'Col 1 x Col 4': ath * iq_neg,
          'Actual IQ': iq,
          'Col 1 x Col 6': ath * iq}
)

sums = out.sum(axis='index')

not_sums = [c for c in out if ' x ' not in c]
sums[not_sums] = ''
sums.iloc[0] = '**SUMS**'

out2 = pd.concat([out, sums.to_frame().T])

write_footerized(out2, 'cc_tab.md', np.arange(1, out2.shape[1] + 1))

samp_out = pd.DataFrame(
    data={'Athletic\nscore': ath}
)
n_trials = 10
for t_no in range(1, n_trials + 1):
    samp_out[t_no] = rnd.permuted(iq)

def sumprod(col):
    return np.sum(col * ath)

samp_sums = samp_out.agg(sumprod, axis='index')

samp_out2 = pd.concat([samp_out, samp_sums.to_frame().T])

write_footerized(samp_out2, 'cc_samp_tab.md')

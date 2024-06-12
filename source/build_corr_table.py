#!/usr/bin/env python3
""" Build draft correlation tables for correlation / causation chapter.
"""

import numpy as np
import pandas as pd

rnd = np.random.default_rng()

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

out2 = pd.concat([out, sums.to_frame().T])

print('Writing cc_tab.md')
out2.to_markdown('cc_tab.md', index=None, tablefmt='grid', numalign="left")

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

print('Writing cc_samp_tab.md')
samp_out2.to_markdown('cc_samp_tab.md', index=None, tablefmt='grid', numalign="left")

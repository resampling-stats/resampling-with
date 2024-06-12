#!/usr/bin/env python3
""" Build draft correlation table
"""

import numpy as np
import pandas as pd

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

out2.to_markdown('cc_tab.md', index=None, tablefmt='grid', numalign="left")

#!/usr/bin/env python3
""" Make fruitfly data
"""

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent

# Seed to give same random result.
rnd = np.random.default_rng(1937)

n = 100

counts = np.zeros(n, dtype=int)
for i in range(n):
    flies = rnd.choice(['heads', 'tails'], size=20)
    counts[i] = np.sum(flies == 'heads')

strange = np.array(['No'] * n, dtype=object)
strange[(counts >= 14) | (counts <= 6)] = 'Yes'

fruitfly_trials = pd.DataFrame(
    {'Trial no': np.arange(1, n + 1),
     '# of heads': counts,
     '>=14 or <= 6': strange})

fruitfly_trials.to_csv(HERE / 'fruitfly_trials.csv', index=None)

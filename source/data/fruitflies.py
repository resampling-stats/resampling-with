#!/usr/bin/env python3
""" Make fruitfly data
"""

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent

# Seed to give same random result.
rnd = np.random.default_rng(1937)

# First table, for testing_counts_1 sec-fruitfly
n = 100
counts = np.zeros(n, dtype=int)
for i in range(n):
    flies = rnd.choice(['heads', 'tails'], size=20)
    counts[i] = np.sum(flies == 'tails')

strange = np.array(['No'] * n, dtype=object)
strange[(counts >= 14) | (counts <= 6)] = 'Yes'

fruitfly_trials = pd.DataFrame(
    {'Trial no': np.arange(1, n + 1),
     '# of tails': counts,
     '>=14 or <=6': strange})

fruitfly_trials.to_csv(HERE / 'fruitfly_trials.csv', index=None)

# Second table, for testing_counts_2
# Seed to give same random result.
rnd = np.random.default_rng(1937)

n = 6
group_names = list('ABCD')
n_groups = len(group_names)
counts = np.zeros((n, n_groups), dtype=int)
for i in range(n):
    for j, group in enumerate(group_names):
        flies = rnd.choice(['heads', 'tails'], size=20)
        counts[i, j] = np.sum(flies == 'tails')

strange = np.array(['No'] * n, dtype=object)
strange[np.any(counts >= 14, axis=1)] = 'Yes'

fruitfly_trials4 = pd.DataFrame(
    data=np.stack([
        np.arange(1, n + 1),
        *counts.T,
        strange], axis=1),
    columns=
    ['Trial no'] +
    [f'Count for group {n}' for n in group_names] +
    ['Any >=14 or any <=6']
)

fruitfly_trials4.to_csv(HERE / 'fruitfly_trials4.csv', index=None)

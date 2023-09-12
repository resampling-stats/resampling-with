#!/usr/bin/env python3
""" Generate reorganized Congress table
"""

from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent

GITHUB_DATASETS = 'https://raw.githubusercontent.com/odsti/datasets/main/'
url = GITHUB_DATASETS + 'congress_118/processed/congress_118.csv'
df = pd.read_csv(url).sort_values('Median_Income')
df.insert(0, 'Ascending_Rank', range(1, len(df) + 1))
df.to_csv(HERE / 'congress_districts.csv', index=None)

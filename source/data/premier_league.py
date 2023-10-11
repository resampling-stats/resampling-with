#!/usr/bin/env python3
""" Generate simplified Premier League table
"""

from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent

GITHUB_DATASETS = 'https://raw.githubusercontent.com/odsti/datasets/main/'

url = GITHUB_DATASETS + 'premier_league/processed/premier_league_2021.csv'
df = pd.read_csv(url)[['team', 'points', 'wages_year']]
df = df.rename(columns={'wages_year': 'wages'})
df.to_csv(HERE / 'premier_league.csv', index=None)

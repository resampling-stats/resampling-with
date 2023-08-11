#!/usr/bin/env python3
""" Generate simplified Premier League table
"""

import pandas as pd

raw_github = 'https://raw.githubusercontent.com'
url = (raw_github +
       '/odsti/datasets/main/premier_league/processed/premier_league_2021.csv')
df = pd.read_csv(url)[['team', 'points', 'wages_year']]
df = df.rename(columns={'wages_year': 'wages'})
df.to_csv('premier_league.csv', index=None)

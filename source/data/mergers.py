#!/usr/bin/env python3
""" Write mergers table ranks
"""

import pandas as pd

import scipy.stats as sps

mergers = pd.read_csv('mergers.csv')
mergers.loc[:, 'Merged':] = sps.rankdata(mergers.loc[:, 'Merged':], axis=1)
mergers.loc[:, 'Merged':] = mergers.loc[:, 'Merged':].astype(int)

mergers.to_csv('merger_ranks.csv', index=None)

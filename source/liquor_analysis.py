#!/usr/bin/env python3
""" Processing for liquor prices

Used in:

* probability_theory_3.Rmd
* testing_measured.Rmd
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


IN_DATA = pd.read_csv('data/liquor_prices.csv').groupby('state_type')['price']
GOVT, PRIV = [np.array(values) for label, values in IN_DATA]


def md_table():
    df = pd.DataFrame()
    df['Private'] = PRIV
    row_labels = df.index[:len(GOVT)]
    df.loc[row_labels, 'Government'] = GOVT
    df.index = [''] * len(df)
    blank_row = pd.DataFrame(data=[[np.nan] * 2], columns=list(df),
                            index=[''])
    counts = df.count().rename('**Count**')
    means = df.mean().rename('**Mean**')
    with_means = pd.concat([df,
                            blank_row,
                            counts.to_frame().T,
                            means.to_frame().T])
    with_means = with_means.round(2).astype(object).fillna('')
    with_means.loc['**Count**'] = with_means.loc['**Count**'].astype(int).astype(object)
    return with_means.to_markdown(tablefmt="grid")


def price_plots():
    fig, axes = plt.subplots(1, 3)
    bins = np.arange(3.5, 5.5, 0.1)
    axis_lims = [np.min(bins), np.max(bins), 0, 8]
    priv_col, gov_col = 'indianred', 'cornflowerblue'

    def histo(ax, data, label, color, alpha=1):
        ax.hist(data, color=color, alpha=alpha);
        ax.axis(axis_lims)
        ax.set_title(label)
        ax.set_xlabel('Prices')

    histo(axes[0], PRIV, 'Private', priv_col)
    histo(axes[1], GOVT, 'Government', gov_col)
    histo(axes[2], PRIV, 'Private', priv_col, alpha=0.5)
    histo(axes[2], GOVT, 'Private & government', gov_col, alpha=0.5);

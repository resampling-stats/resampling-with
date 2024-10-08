""" Script run before every notebook
"""

import numpy.random as _npr

_default_rng = _npr.default_rng


def _make_default_seeded_rng(default_seed):

    def dsrng(*args, **kwargs):
        """ Use original default_rng if any arguments, else use given seed
        """
        if args or kwargs:
            return _default_rng(*args, **kwargs)
        # Seed injected from _common.R script.
        return _default_rng(default_seed)

    return dsrng


_npr.default_rng = _make_default_seeded_rng(_QUARTO_SEED)


# Python variable in Python edition else R variable.
def get_var(name):
    if name in globals():
        return globals()[name]
    return getattr(r, name)


def print_tab(tab_md, caption, label):
    """ Print Markdown table, caption, label with suitable formatting.
    """
    print(f'{tab_md}\n\n: {caption} {{#tbl-{label}}}')

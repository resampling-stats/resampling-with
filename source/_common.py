""" Script run before every notebook
"""

import numpy.random as _npr

_default_rng = _npr.default_rng


def _default_seeded_rng(*args, **kwargs):
    """ Use original default_rng if any arguments, else use given seed
    """
    if args or kwargs:
        return _default_rng(*args, **kwargs)
    # Seed injected from _common.R script.
    return _default_rng(_QUARTO_SEED)


_npr.default_rng = _default_seeded_rng


# Python variable in Python edition else R variable.
def get_var(name):
    if name in globals():
        return globals()[name]
    return getattr(r, name)

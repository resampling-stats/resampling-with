#!/usr/bin/env python3
""" Wrap noteout filter.

Link to this file with appropriate filename to make executable file for filter.

For example, to make an executable filter `write_notebooks.py`:::

    ln -s wrap_noteout.py write_notebooks.py
"""

from pathlib import Path
from importlib import import_module

if __name__ == "__main__":
    mod = import_module('noteout.' + Path(__file__).stem)
    mod.main()

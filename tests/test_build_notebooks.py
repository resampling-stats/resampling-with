""" Tests for build_notebooks script
"""

import os.path as op
import sys
import json

HERE = op.dirname(__file__)
DATA = op.join(HERE, 'data')
SCRIPTS = op.join(HERE, '..', 'scripts')
sys.path.append(SCRIPTS)

import build_notebooks as bn

FIRST_MD = op.join(DATA, 'first.md')
FIRST_CONTENTS = bn.read_fname(FIRST_MD)

def test_extract_notebooks():
    assert FIRST_CONTENTS.startswith('---\ntitle: "A title"')
    notebooks = bn.extract_nb_md(FIRST_CONTENTS)
    assert len(notebooks) == 2
    assert sorted(notebooks) == ['first_notebook.ipynb',
                                 'second_notebook.ipynb']


def test_text2nb_text():
    notebooks = bn.extract_nb_md(FIRST_CONTENTS)
    nb1_json = bn.text2nb_text(notebooks['first_notebook.ipynb'])
    nb = json.loads(nb1_json)
    cells = nb['cells']
    assert len(cells) == 3
    assert [c['cell_type'] for c in cells] == ['markdown', 'code', 'markdown']
    nb2_json = bn.text2nb_text(notebooks['second_notebook.ipynb'])
    nb = json.loads(nb2_json)
    cells = nb['cells']
    assert len(cells) == 4
    assert [c['cell_type'] for c in cells] == ['markdown',
                                               'code',
                                               'markdown',
                                               'code']

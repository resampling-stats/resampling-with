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
    assert sorted(notebooks) == ['first_notebook',
                                 'second_notebook']

def test_proc_text():
    assert bn.proc_text('') == ''
    assert bn.proc_text('Foo bar') == 'Foo bar'
    assert bn.proc_text('Foo <!--bar-->\nbaz') == 'Foo \nbaz'
    assert bn.proc_text('Foo <!-- bar-->\nbaz') == 'Foo \nbaz'
    assert bn.proc_text('Foo <!--bar --->\nbaz') == 'Foo \nbaz'
    assert bn.proc_text('Foo <!--\n\n  bar \n\n--->\nbaz') == 'Foo \nbaz'
    assert bn.proc_text('Foo\n``` python\nbaz') == 'Foo\n```{python}\nbaz'


def test_text2nb_text_rmd():
    notebooks = bn.extract_nb_md(FIRST_CONTENTS)
    nb1_rmd = bn.text2nb_text(notebooks['first_notebook'], 'Rmd')
    assert nb1_rmd == """\
This is some explanation about the notebook.

It can use macros: Python.


```{python}
import matplotlib.pyplot as plt
plt.plot([0, 2, 1, 4])
plt.show()
```

A normal paragraph.
"""
    nb2_rmd = bn.text2nb_text(notebooks['second_notebook'], 'Rmd')
    assert nb2_rmd == """\
This is some explanation about the second notebook.


```{python}
import matplotlib.pyplot as plt
plt.plot(range(10))
plt.show()
```

Some unrelated text.



Again, text.

```{python}
a = 1
a
```
"""


def test_text2nb_text_ipynb():
    notebooks = bn.extract_nb_md(FIRST_CONTENTS)
    nb1_json = bn.text2nb_text(notebooks['first_notebook'], 'ipynb')
    nb = json.loads(nb1_json)
    cells = nb['cells']
    assert len(cells) == 3
    assert [c['cell_type'] for c in cells] == ['markdown', 'code', 'markdown']
    nb2_json = bn.text2nb_text(notebooks['second_notebook'], 'ipynb')
    nb = json.loads(nb2_json)
    cells = nb['cells']
    assert len(cells) == 5
    assert [c['cell_type'] for c in cells] == ['markdown',
                                               'code',
                                               'markdown',
                                               'markdown',
                                               'code']

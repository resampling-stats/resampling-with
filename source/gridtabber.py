""" Routines for working with grid tables
"""

# We need to catch warnings, as these break up the generated Markdown.
import warnings

warnings.filterwarnings("error")


def replace_val(part, val):
    vs = f' {val}'
    if len(vs) > len(part) - 1:
        raise ValueError(f'{vs} is too long to replace in {part}')
    return vs + ' ' * (len(part) - len(vs))


def extend_with_row(tab_md, vals, where='before'):
    lines = tab_md.splitlines()
    lines = lines[::-1] if where == 'after' else lines
    assert lines[0].startswith('+')
    L1 = lines[1]
    assert (L1[0], L1[-1]) == ('|', '|')
    parts = lines[1].split('|')[1:-1]
    new_parts = []
    for part, val in zip(parts, vals):
        new_parts.append(replace_val(part, val))
    L1 = '|'.join(new_parts)
    lines = lines[::-1] if where == 'after' else lines
    return '\n'.join([lines[0], f'|{L1}|'] + lines)


def footerize_table(tab_md, indices=(-2, -1)):
    lines = tab_md.splitlines()
    line_indices = [i for i, line in enumerate(lines)
                    if line[:2] in ('+-', '+=')]
    for to_footerize in indices:
        LI = line_indices[to_footerize]
        lines[LI] = lines[LI].replace('-', '=')
    return '\n'.join(lines)


def to_md(df, prepended=None, extended=None):
    tab_md = df.to_markdown(index=None, tablefmt='grid', numalign="left")
    if prepended is not None:
        tab_md = extend_with_row(tab_md, prepended)
    if extended is not None:
        tab_md = extend_with_row(tab_md, extended, where='after')
    return tab_md

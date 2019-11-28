#!/usr/bin/env python
import panflute as pf


def only_header(elem, doc):
    if type(elem) is pf.Header:
        txt = pf.stringify(elem).strip()
        if elem.level == 1:
            out = f'\n\n\n## {txt}\n\n'
        else:
            indent = '    ' * (elem.level - 2)
            indent = indent[:-1] + '*'
            out = f'{indent} {txt}\n'
        pf.debug(out)


def main(doc=None):
    return pf.run_filter(only_header, doc=doc)


if __name__ == "__main__":
    main()

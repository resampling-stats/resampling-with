#!/bin/bash
rm toc_dump.md
touch toc_dump.md
for fname in ls source/*.Rmd; do
    pandoc -f markdown -s ${fname} -t markdown --filter ./scripts/show_headers.py -o foo.md >& tmp.md
    cat tmp.md >> toc_dump.md
done

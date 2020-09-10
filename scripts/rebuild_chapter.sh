#!/bin/bash
# Rebuild single chapter
# Useage example:
#  rebuild_chapter.sh probability_theory_1a.Rmd r
#  rebuild_chapter.sh sampling_variability.Rmd python

rmd=$1
if [ -z "$rmd" ]; then
    echo Specify Rmd filename e.g. 05-Chap-1.Rmd
    exit 1
fi
shift
edition=${1:-python}
echo "Building $rmd for $edition edition."

MY_DIR=$(dirname "${BASH_SOURCE[0]}")
book_build_dir=${MY_DIR}/../${edition}-book/
if ! [ -f "${book_build_dir}/index.md" ]; then
    echo "You need a full book build before building single chapters."
    echo "Run 'make ${edition}-book' first."
    exit 1
fi

cd $MY_DIR/../source
rmd_root="${rmd%.*}"
rm -rf _bookdown_files/${rmd_root}_cache/*
config="_${edition}_bookdown.yml"
Rscript -e "bookdown::preview_chapter('${rmd_root}.Rmd', config_file='${config}')"

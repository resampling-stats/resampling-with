rmd=$1
if [ -z "$rmd" ]; then
    echo Specify Rmd filename e.g. 05-Chap-1.Rmd
    exit 1
fi
MY_DIR=$(dirname "${BASH_SOURCE[0]}")
cd $MY_DIR/../source
rmd_root="${rmd%.*}"
rm -rf _bookdown_files/${rmd_root}_cache/*
Rscript -e "bookdown::preview_chapter('${rmd_root}.Rmd')"

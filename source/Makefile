.PHONY: python-html-book python-pdf-book r-html-book r-pdf-book python-nb \
	r-nb serve-python serve-r clean

# Markdown files generated during build.
BUILD_MDS:=$(patsubst %.Rmd,%.md,$(wildcard *.Rmd))

python-all: python-html-book python-nb python-pdf-book

r-all: r-html-book r-nb r-pdf-book

vector_images := $(wildcard diagrams/*.svg)

diagrams := $(vector_images:.svg=.png)

%.png : %.svg
	inkscape --export-area-drawing --export-png=$@ --export-dpi=300 $<

html-book-%:
	../scripts/build_book.R -e $* -f html

pdf-book-%:
	../scripts/build_book.R -e $* -f pdf
	mv ../$*-book/_main.pdf ../$*-book/resampling_with_$*.pdf

python-html-book: $(diagrams) html-book-python

python-pdf-book: $(diagrams) pdf-book-python

r-html-book: $(diagrams) html-book-r

r-pdf-book: $(diagrams) pdf-book-r

nb-%:
	# Build notebooks for given version
	Rscript ../scripts/build_nb_book.R -e $* -o _nb_$*
	python ../scripts/build_notebooks.py _nb_$*/_main.md \
		--out-path=../$*-book \
		--out-fmt=$*

python-nb: nb-python

r-nb: nb-r

serve-%:
	# Requires 'servr' R package
	cp _$*_bookdown.yml _bookdown.yml
	Rscript -e 'bookdown::serve_book(dir = ".")'

clean:
	rm -rf _main.md _bookdown_files _notebooks *.rds $(BUILD_MDS)

check-simon-refs :
	biber --tool -V simon_refs.bib

check-ds-refs :
	biber --tool -V data-science-bib/data_science.bib

check-refs: check-simon-refs check-ds-refs

# See ../scripts/rebuild_chapter.py for single chapter rebuild.

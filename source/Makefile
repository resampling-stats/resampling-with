.PHONY: python-html-book python-pdf-book r-html-book r-pdf-book \
	clean

python-all: python-html-book python-pdf-book

r-all: r-html-book r-pdf-book

vector_images := $(wildcard diagrams/*.svg)

diagrams := $(vector_images:.svg=.png)

%.png : %.svg
	inkscape --export-area-drawing --export-png=$@ --export-dpi=300 $<

set-version-%:
	../scripts/set_version.py $*

html-book-%:
	$(MAKE) set-version-$*
	quarto render .

pdf-book-%:
	$(MAKE) set-version-$*
	quarto render . --to pdf

python-html-book: $(diagrams) html-book-python

python-pdf-book: $(diagrams) pdf-book-python

r-html-book: $(diagrams) html-book-r

r-pdf-book: $(diagrams) pdf-book-r

clean:
	rm -rf *_cache/ .quarto/

check-simon-refs :
	biber --tool -V simon_refs.bib

check-ds-refs :
	biber --tool -V data-science-bib/data_science.bib

check-refs: check-simon-refs check-ds-refs

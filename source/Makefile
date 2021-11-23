.PHONY: python-html-book python-pdf-book r-html-book r-pdf-book \
	clean

vector_images := $(wildcard diagrams/*.svg)

diagrams := $(vector_images:.svg=.png)

%.png : %.svg
	inkscape --export-area-drawing --export-png=$@ --export-dpi=300 $<

set-version-%:
	../scripts/set_version.py $*

html-book-%:
	$(MAKE) set-version-$*
	quarto render . --to html

pdf-book-%:
	$(MAKE) set-version-$*
	quarto render . --to pdf

all-book-%:
	# Since 0.2.260, quarto renders all formats by default.
	$(MAKE) set-version-$*
	quarto render .

python-html-book: $(diagrams) html-book-python

python-pdf-book: $(diagrams) pdf-book-python

python-all: $(diagrams) all-book-python

r-html-book: $(diagrams) html-book-r

r-pdf-book: $(diagrams) pdf-book-r

r-all: $(diagrams) all-book-r

clean:
	rm -rf *_cache/ .quarto/

check-simon-refs :
	biber --tool -V simon_refs.bib

check-ds-refs :
	biber --tool -V data-science-bib/data_science.bib

check-refs: check-simon-refs check-ds-refs

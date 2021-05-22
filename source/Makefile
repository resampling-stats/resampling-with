.PHONY: python-book r-book python-nb r-nb serve-python serve-r

# Markdown files generated during build.
BUILD_MDS:=$(patsubst %.Rmd,%.md,$(wildcard *.Rmd))

python-all: python-book python-nb

r-all: r-book r-nb

vector_images := $(wildcard diagrams/*.svg)

diagrams := $(vector_images:.svg=.png)

%.png : %.svg
	inkscape --export-area-drawing --export-png=$@ --export-dpi=300 $<

book-%:
	BOOK_ED=$* Rscript -e \
			'bookdown::render_book("index.Rmd", config_file="_$*_bookdown.yml")'

pdf-book-%:
	BOOK_ED=$* Rscript -e \
			'bookdown::render_book("index.Rmd", config_file="_$*_bookdown.yml", output_format="bookdown::pdf_book")'

python-book: $(diagrams) book-python

r-book: $(diagrams) book-r

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

# See ../scripts/rebuild_chapter.sh for single chapter rebuild.

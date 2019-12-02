.PHONY: python-book r-book python-nb r-nb serve-python serve-r

book-%:
	BOOK_ED=$* Rscript -e \
			'bookdown::render_book("index.rmd", config_file="_$*_bookdown.yml")'

python-book: book-python

r-book: book-r

nb-%:
	# Build notebooks for given version
	Rscript ../scripts/build_nb_book.R -e $* -o _nb_$*
	python ../scripts/build_notebooks.py _nb_$* \
		--out-path=../$*-book

python-nb: nb-python

r-nb: nb-r

serve-%:
	# Requires 'servr' R package
	cp _$*_bookdown.yml _bookdown.yml
	Rscript -e 'bookdown::serve_book(dir = ".")'

clean:
	rm -rf _main.md _bookdown_files _notebooks *.rds

check-simon-refs :
	biber --tool -V simon_refs.bib

check-ds-refs :
	biber --tool -V data-science-bib/data_science.bib

check-refs: check-simon-refs check-ds-refs

.PHONY: python-book r-book

R_CONFIG=_r_bookdown.yml
PY_CONFIG=_python_bookdown.yml

python-book:
	BOOK_ED=python Rscript -e \
			'bookdown::render_book("index.rmd", config_file="$(PY_CONFIG)")'

python-nb: nb-python

r-nb: nb-r

nb-%:
	# Build notebooks for given version
	Rscript ../scripts/build_nb_book.R -e $* -o ${OUT_DIR}
	python ../scripts/build_notebooks.py ${OUT_DIR}
		_notebooks/*.md --out-path=../$*-book

r-book:
	BOOK_ED=r Rscript -e \
		'bookdown::render_book("index.rmd", config_file="$(R_CONFIG)")'

serve-py:
	# Requires 'servr' R package
	cp $(PY_CONFIG) _bookdown.yml
	Rscript -e 'bookdown::serve_book(dir = ".")'

serve-r:
	# Requires 'servr' R package
	cp $(R_CONFIG) _bookdown.yml
	Rscript -e 'bookdown::serve_book(dir = ".")'

clean:
	rm -rf _main.md _bookdown_files _notebooks *.rds

check-simon-refs :
	biber --tool -V simon_refs.bib

check-ds-refs :
	biber --tool -V data-science-bib/data_science.bib

check-refs: check-simon-refs check-ds-refs

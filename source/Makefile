.PHONY: python-book r-book

python-book:
	BOOK_ED=python Rscript -e \
			'bookdown::render_book("index.rmd", config_file="_python_bookdown.yml")'

python-nb:
	BOOK_ED=python-nb Rscript -e \
			'bookdown::render_book("index.rmd", output_format="bookdown::gitbook", config_file="_python_bookdown.yml", output_dir="_notebooks")'
	python ../scripts/build_notebooks.py _notebooks/*.md --out-path=python-book

r-book:
	BOOK_ED=r Rscript -e \
		'bookdown::render_book("index.rmd", config_file="_r_bookdown.yml")'

serve:
	# Requires 'servr' R package
	Rscript -e 'bookdown::serve_book(dir = ".")'

clean:
	rm -rf _main.md r-book python-book _bookdown_files _notebooks *.rds

check-simon-refs :
	biber --tool -V simon_refs.bib

check-ds-refs :
	biber --tool -V data-science-bib/data_science.bib

check-refs: check-simon-refs check-ds-refs

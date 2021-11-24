.PHONY: python-html-book python-pdf-book r-html-book r-pdf-book \
	clean

python-all: python-html-book python-pdf-book

r-all: r-html-book r-pdf-book

Rmd_sources := $(shell python -c "import yaml; print(' '.join(yaml.load(open('_quarto.yml.template'),Loader=yaml.FullLoader)['book']['chapters']))")
config_templates := _quarto.yml.template _variables.yml.template

vector_images := $(wildcard diagrams/*.svg)

diagrams := $(vector_images:.svg=.png)

%.png : %.svg
	inkscape --export-area-drawing --export-png=$@ --export-dpi=300 $<

set-version-%: $(config_templates)
	@../scripts/set_version.py $*

../%-book/index.html: $(Rmd_sources) $(diagrams) | set-version-%
	quarto render . --to html

../python-book/resampling-with-python.pdf: $(Rmd_sources) $(diagrams) $(config_templates) | set-version-python
	quarto render . --to pdf

../r-book/resampling-with-r.pdf: $(Rmd_sources) $(diagrams) $(config_templates) | set-version-r
	quarto render . --to pdf

python-html-book: ../python-book/index.html

python-pdf-book: ../python-book/resampling-with-python.pdf

r-html-book: ../r-book/index.html

r-pdf-book: ../r-book/resampling-with-r.pdf

clean:
	rm -rf *_cache/ .quarto/

check-simon-refs :
	biber --tool -V simon_refs.bib

check-ds-refs :
	biber --tool -V data-science-bib/data_science.bib

check-refs: check-simon-refs check-ds-refs

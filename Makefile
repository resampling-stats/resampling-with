WEB_DIR=_www
SOURCE_DIR=source
PYTHON_BOOK_DIR=python-book
R_BOOK_DIR=r-book
PIP_INSTALL_CMD ?= "pip install"

.PHONY: python-book r-book

python-all:
	cd $(SOURCE_DIR) && make python-all

r-all:
	cd $(SOURCE_DIR) && make r-all

landing-page:
	cd website && make landing-page

website: webclean python-all r-all landing-page
	mkdir $(WEB_DIR)
	cp website/*.html $(WEB_DIR)
	cp requirements.txt $(WEB_DIR)
	cp -r $(PYTHON_BOOK_DIR) $(WEB_DIR)
	cp -r $(R_BOOK_DIR) $(WEB_DIR)

github: website
	ghp-import -n _www
	git push origin gh-pages:gh-pages --force
	@echo
	@echo "Published to Github"

webclean:
	rm -rf $(WEB_DIR)

r-build-requirements:
	Rscript -e "source('scripts/install_r_requirements.R')"

python-build-requirements:
	$(PIP_INSTALL_CMD) -r build-requirements.txt

build-init: r-build-requirements python-build-requirements
	git submodule update --init --recursive

clean:
	rm -rf $(PYTHON_BOOK_DIR) $(R_BOOK_DIR)
	cd $(SOURCE_DIR) && make clean

bibcheck: source/simon_refs.bib
	# Obviously needs biber installed, which is not so on Travis-CI by default.
	biber --tool source/simon_refs.bib

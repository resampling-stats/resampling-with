WEB_DIR=_www
SOURCE_DIR=source
PYTHON_BOOK_DIR=python-book
R_BOOK_DIR=r-book
PYTHON ?= python
PIP_INSTALL_CMD ?= $(PYTHON) -m pip install

landing-page:
	cd website && make landing-page

website: clean python-all r-all landing-page
	mkdir -p $(WEB_DIR)
	cp website/*.html $(WEB_DIR)
	cp requirements.txt $(WEB_DIR)
	cp -r $(PYTHON_BOOK_DIR) $(WEB_DIR)
	cp -r $(R_BOOK_DIR) $(WEB_DIR)

github: website
	ghp-import -n $(WEB_DIR)
	git push origin gh-pages:gh-pages --force
	@echo
	@echo "Published to Github"

webclean:
	rm -rf $(WEB_DIR)

r-build-requirements:
	Rscript -e "source('scripts/install_r_requirements.R')"

python-build-requirements:
	$(PIP_INSTALL_CMD) -r build-requirements.txt

submodule-update:
	git submodule update --init --recursive

build-init: submodule-update r-build-requirements python-build-requirements

clean: source-clean
	rm -rf $(PYTHON_BOOK_DIR) $(R_BOOK_DIR)

source-clean:
	cd $(SOURCE_DIR) && make clean

bibcheck: source/simon_refs.bib
	# Obviously needs biber installed, which is not so on Travis-CI by default.
	biber --tool source/simon_refs.bib

%:
	@$(MAKE) -C source $@

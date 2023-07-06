.PHONY: build-init python-book r-book website github

WEB_DIR=_www
SOURCE_DIR=source
PYTHON_BOOK_DIR=python-book
R_BOOK_DIR=r-book
PYTHON ?= python
PIP_INSTALL_CMD ?= $(PYTHON) -m pip install

_submodule-update:
	git submodule update --init --recursive

r-build-requirements:
	Rscript -e "source('scripts/install_r_requirements.R')"

_python-build-requirements:
	$(PIP_INSTALL_CMD) -r build-requirements.txt

build-init:  ## Install build dependencies
build-init: _submodule-update _r-build-requirements _python-build-requirements

_landing-page:
	cd website && make landing-page

python-book:  ## Build the Python version of the book
	cd $(SOURCE_DIR) && python generate-ninja.py && ninja python-book

r-book:  ## Build the R version of the book
	cd $(SOURCE_DIR) && python generate-ninja.py && ninja r-book

website:  ## Build the book (R/Python) as well as the website
website: _python-book r-book _landing-page
	mkdir -p $(WEB_DIR)
	cp website/*.html $(WEB_DIR)
	cp requirements.txt $(WEB_DIR)
	cp -r $(PYTHON_BOOK_DIR) $(WEB_DIR)
	cp -r $(R_BOOK_DIR) $(WEB_DIR)

github:   ## Publish the website to GitHub
github: website
	ghp-import -n $(WEB_DIR)
	git push origin gh-pages:gh-pages --force
	@echo
	@echo "Published to Github"

webclean:
	rm -rf $(WEB_DIR)

_source-clean:
	cd $(SOURCE_DIR) && ninja clean

clean: _source-clean
	rm -rf $(PYTHON_BOOK_DIR) $(R_BOOK_DIR)

.DEFAULT_GOAL := help
help:
	@sed \
		-e '/^[a-zA-Z0-9_\-]*:.*##/!d' \
		-e 's/:.*##\s*/:/' \
		-e 's/^\(.\+\):\(.*\)/$(shell tput setaf 6)\1$(shell tput sgr0):\2/' \
		$(MAKEFILE_LIST) | column -c2 -t -s :

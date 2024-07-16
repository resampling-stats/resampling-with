.PHONY: build-init python-book r-book website github

WEB_DIR=_www
SOURCE_DIR=source
BUILD_NINJA=$(SOURCE_DIR)/build.ninja
PYTHON_BOOK_DIR=python-book
R_BOOK_DIR=r-book
PYTHON ?= python
PIP_INSTALL_CMD ?= $(PYTHON) -m pip install

_submodule-update:
	git submodule update --init --recursive

_r-build-requirements:
	Rscript -e "source('scripts/install_r_requirements.R')"

_python-build-requirements:
	$(PIP_INSTALL_CMD) -r build-requirements.txt

$(BUILD_NINJA): $(SOURCE_DIR)/generate-ninja.py
	(cd $(SOURCE_DIR) && $(PYTHON) generate-ninja.py)

ninja-config:  ## Configure ninja for source builds
ninja-config: $(BUILD_NINJA)

build-init:  ## Install build dependencies
build-init: _submodule-update _r-build-requirements _python-build-requirements

_landing-page:
	cd website && make landing-page

python-book:  ## Build the Python version of the book
python-book: ninja-config
	cd $(SOURCE_DIR) && ninja clean && ninja python-book

python-book-jl: python-book
	# Jupyter-lite files for book build.
	$(PIP_INSTALL_CMD) -r py-jl-requirements.txt
	$(PYTHON) ./scripts/process_notebooks.py \
		$(SOURCE_DIR)/_quarto-python.yml \
		_py_notebooks
	$(PYTHON) -m jupyter lite build \
		--contents _py_notebooks \
		--output-dir $(PYTHON_BOOK_DIR)/interact \
		--lite-dir $(PYTHON_BOOK_DIR)

r-book:  ## Build the R version of the book
r-book: ninja-config
	cd $(SOURCE_DIR) && ninja clean && ninja r-book

r-book-jl: r-book
	$(PIP_INSTALL_CMD) -r r-jl-requirements.txt
	$(PYTHON) ./scripts/process_notebooks.py \
		$(SOURCE_DIR)/_quarto-r.yml \
		_r_notebooks
	$(PYTHON) -m jupyter lite build \
		--contents _r_notebooks \
		--output-dir $(R_BOOK_DIR)/interact \
		--lite-dir $(R_BOOK_DIR)

_source-clean:
	cd $(SOURCE_DIR) && ninja clean

clean: _source-clean
	rm -rf $(PYTHON_BOOK_DIR) $(R_BOOK_DIR) _r_notebooks _py_notebooks

.DEFAULT_GOAL := help
help:
	@sed \
		-e '/^[a-zA-Z0-9_\-]*:.*##/!d' \
		-e 's/:.*##\s*/:/' \
		-e 's/^\(.\+\):\(.*\)/$(shell tput setaf 6)\1$(shell tput sgr0):\2/' \
		$(MAKEFILE_LIST) | column -c2 -t -s :

.PHONY: build-init website github

WEB_DIR=_www
SOURCE_DIR=source
BUILD_NINJA=$(SOURCE_DIR)/build.ninja
PYTHON ?= python
PIP_INSTALL_CMD ?= $(PYTHON) -m pip install
JL_SDIR = interact

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

# See https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html#Automatic-Variables
%-book:  ## Build the given version of the book
%-book: ninja-config
	cd $(SOURCE_DIR) && ninja clean && ninja $*-book
	$(PYTHON) ./scripts/postprocess_site.py $(SOURCE_DIR)/_quarto-$*.yml

%-book-jl: %-book
	$(PIP_INSTALL_CMD) -r $*-jl-requirements.txt
	$(PYTHON) ./scripts/process_notebooks.py \
		$(SOURCE_DIR)/_quarto-$*.yml \
		_$*_notebooks
	$(PYTHON) -m jupyter lite build \
		--contents _$*_notebooks \
		--output-dir $*-book/$(JL_SDIR) \
		--lite-dir $*-book

_source-clean:
	cd $(SOURCE_DIR) && ninja clean

clean: _source-clean
	rm -rf *-book _*_notebooks

.DEFAULT_GOAL := help
help:
	@sed \
		-e '/^[a-zA-Z0-9_\-]*:.*##/!d' \
		-e 's/:.*##\s*/:/' \
		-e 's/^\(.\+\):\(.*\)/$(shell tput setaf 6)\1$(shell tput sgr0):\2/' \
		$(MAKEFILE_LIST) | column -c2 -t -s :

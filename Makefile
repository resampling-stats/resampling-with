WEB_DIR=_www
SOURCE_DIR=source

python-book:
	cd $(SOURCE_DIR) && make python-book

r-book:
	cd $(SOURCE_DIR) && make r-book

python-nb:
	cd $(SOURCE_DIR) && make python-nb
	# Extract notebooks.
	# Write into web directory.

landing-page:
	cd website && make landing-page

website: webclean python-book r-book landing-page python-nb
	mkdir $(WEB_DIR)
	cp website/*.html $(WEB_DIR)
	cp -r $(SOURCE_DIR)/python-book $(WEB_DIR)
	cp -r $(SOURCE_DIR)/r-book $(WEB_DIR)

github: website
	ghp-import -n _www
	git push origin gh-pages:gh-pages --force
	@echo
	@echo "Published to Github"

webclean:
	rm -rf $(WEB_DIR)

r-build-requirements:
	Rscript -e "source('scripts/install_r_requirements.R')"

clean:
	cd $(SOURCE_DIR) && make clean

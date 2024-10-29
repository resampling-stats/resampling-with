website: landing-page data

landing-page:
	Rscript -e 'rmarkdown::render("index.Rmd")'

# Now legacy.  Leave for a little while.
data:
	mkdir -p data
	cp ../source/data/*.csv data

clean:
	rm -rf *.html

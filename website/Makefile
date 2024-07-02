website: landing-page data

landing-page:
	Rscript -e 'rmarkdown::render("index.Rmd")'

data:
	mkdir -p data
	cp ../source/data/*.csv data

clean:
	rm -rf *.html

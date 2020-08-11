# Install requirements for book build
# Set default repo, if not set.
if (getOption('repos')["CRAN"] == "@CRAN@") {
   options(repos = c(CRAN = "http://cloud.r-project.org"))
}

# https://stackoverflow.com/questions/4090169/elegant-way-to-check-for-missing-packages-and-install-them
to_install <- c("servr", "bookdown", "devtools", "optparse")
to_install <- to_install[!(to_install %in% installed.packages()[,"Package"])]
if (length(to_install)) {
    install.packages(to_install)
}

# https://www.r-project.org/nosvn/pandoc/devtools.html
# "In this mode, R will install packages to ~/R-dev. This is useful to avoid
# clobbering the existing versions of CRAN packages that you need for other
# tasks."
devtools::dev_mode(on=TRUE)
# Always install reticulate from Github
# Reticulate is the package that allows execution of Python in the R notebook,
# and interaction between the R and Python workspace.
# We may be able to drop back to latest; this was to deal with a bug; I have
# forgotten which.
devtools::install_github("rstudio/reticulate")

# Install requirements for book build
# Force user install.
# This code adapted from install.packages function.
userdir <- unlist(strsplit(Sys.getenv("R_LIBS_USER"), .Platform$path.sep))[1L]
if (!file.exists(userdir)) {
    if (!dir.create(userdir, recursive = TRUE))
        stop(gettextf("unable to create %s", sQuote(userdir)),
             domain = NA)
    .libPaths(c(userdir, .libPaths()))
}

# Set default repo, if not set.
if (getOption('repos')["CRAN"] == "@CRAN@") {
   options(repos = c(CRAN = "http://cloud.r-project.org"))
}

# https://stackoverflow.com/questions/4090169/elegant-way-to-check-for-missing-packages-and-install-them
# "remotes" for dev version of reticulate - see below.
to_install <- c("optparse", "fs", "kableExtra", 'quarto', 'remotes')
to_install <- to_install[!(to_install %in% installed.packages()[,"Package"])]
if (length(to_install)) {
    install.packages(to_install, dependencies=TRUE)
}

# https://www.r-project.org/nosvn/pandoc/devtools.html
# "In this mode, R will install packages to ~/R-dev. This is useful to avoid
# clobbering the existing versions of CRAN packages that you need for other
# tasks."
fs::dir_create('~/R-dev')  # ?also correct for Windows

# Install our patched version of reticulate.
# https://github.com/rstudio/reticulate/pull/1401
remotes::install_github("rstudio/reticulate",
                        ref='a003118f',  # jupyter-compat fixes.
                        dependencies=TRUE)

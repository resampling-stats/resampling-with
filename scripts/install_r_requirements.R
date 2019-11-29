# Install requirements for book build

# https://stackoverflow.com/questions/4090169/elegant-way-to-check-for-missing-packages-and-install-them
to_install <- c("servr", "bookdown", "devtools", "optparse")
to_install <- to_install[!(to_install %in% installed.packages()[,"Package"])]
if (length(to_install)) {
    install.packages(to_install)
}

# Always install reticulate from Github
devtools::install_github("rstudio/reticulate")
devtools::dev_mode(on=TRUE)

#!/usr/bin/env Rscript
# Build single Markdown document from which to extract notebooks.
#
# Usage:
#   build_book.R --edition python

# Define, parse, check command line options.
# Define
opt_list <- list(
  optparse::make_option(c("-e", "--edition"),
                        type="character",
                        default='python',
              help="edition (python or r)",
              metavar="character"),
  optparse::make_option(c("-f", "--format"),
                        type="character",
                        default='html',
              help="format (html or pdf)",
              dest='format',
              metavar="character")
)

# Parse
opt_parser <- optparse::OptionParser(option_list=opt_list)
opt__ <- optparse::parse_args(opt_parser)

# Check
opt__$edition <- tolower(opt__$edition)
if (!is.element(opt__$edition, c('python', 'r'))) {
    optparse::print_help(opt_parser)
    stop("edition must be 'python' or 'r'", call.=FALSE)
}
if (opt__$format == 'html') {
    out_fmt__='bookdown::gitbook'
} else if (opt__$format == 'pdf') {
    out_fmt__='bookdown::pdf_book'
} else {
    out_fmt__=opt__$format
}

# BOOK_ED environment variable defines book edition.
# _common.R uses BOOK_ED to define various bits of code used inside the book
# Rmd chapters.
Sys.setenv(BOOK_ED=opt__$edition)
# Configuration file for build.
opt__$config <- stringr::str_interp('_${opt__$edition}_bookdown.yml')
# Build document
# See https://github.com/rstudio/bookdown/issues/835
# for explanation of clean_envir
rm(opt_list, opt_parser)
bookdown::render_book('index.Rmd', out_fmt__, clean_envir=FALSE,
                      config_file=opt__$config)

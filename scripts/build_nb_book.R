#!/usr/bin/env Rscript
# Build single Markdown document from which to extract notebooks.
#
# Usage:
#   build_nb_book.R --edition python

# Define, parse, check command line options.
# Define
opt_list <- list(
  optparse::make_option(c("-e", "--edition"),
                        type="character",
                        default=NULL,
              help="edition (python or r)",
              metavar="character"),
  optparse::make_option(c("-o", "--out-dir"),
                        type="character",
                        default=NULL,
              help="output directory",
              dest='out_dir',
              metavar="character")
)

# Parse
opt_parser <- optparse::OptionParser(option_list=opt_list)
opt__ <- optparse::parse_args(opt_parser)

# Check
if (is.null(opt__$edition)){
  optparse::print_help(opt_parser)
  stop("Specify edition", call.=FALSE)
}
opt__$edition <- tolower(opt__$edition)
if (!is.element(opt__$edition, c('python', 'r'))) {
  optparse::print_help(opt_parser)
  stop("edition must be 'python' or 'r'", call.=FALSE)
}
if (is.null(opt__$out_dir)){
  optparse::print_help(opt_parser)
  stop("Specify output directory", call.=FALSE)
}

# BOOK_ED environment variable defines book edition.
# _common.R uses BOOK_ED to define various bits of code used inside the book
# Rmd chapters.
Sys.setenv(BOOK_ED=stringr::str_interp('${opt__$edition}-nb'))
# Configuration file for build.
opt__$config <- stringr::str_interp('_${opt__$edition}_bookdown.yml')
# Set Github-Flavored-Markdown as Markdown output config.
# See: https://github.com/rstudio/bookdown/issues/782
opt__$fmt <- bookdown::markdown_document2(base_format=rmarkdown::md_document,
                                          variant='gfm')
# Turn off citation links - they will invariably point outside the notebook.
opt__$fmt$pandoc$args <- c(opt__$fmt$pandoc$args,
                     '--metadata',
                     'link-citations=no')
# Build single Markdown output document.
rm(opt_list, opt_parser)
bookdown::render_book('index.Rmd', opt__$fmt,
                      config_file=opt__$config,
                      output_dir=opt__$out_dir)

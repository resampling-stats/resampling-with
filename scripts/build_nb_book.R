#!/usr/bin/env Rscript
library("optparse")

option_list <- list(
  make_option(c("-e", "--edition"), type="character", default=NULL,
              help="edition (python or r)",
              metavar="character"),
  make_option(c("-d", "--out-dir"), type="character", default=NULL,
              help="output directory",
              dest='out_dir',
              metavar="character")
)

opt_parser <- OptionParser(option_list=option_list)
opt <- parse_args(opt_parser)

if (is.null(opt$edition)){
  print_help(opt_parser)
  stop("Specify edition", call.=FALSE)
}
opt$edition <- tolower(opt$edition)
if (!is.element(opt$edition, c('python', 'r'))) {
  print_help(opt_parser)
  stop("out-dir must be 'python' or 'r'", call.=FALSE)
}
if (is.null(opt$out_dir)){
  print_help(opt_parser)
  stop("Specify output directory", call.=FALSE)
}

# Signal notebook version to _common.R
Sys.setenv(BOOK_ED=stringr::str_interp('${opt$edition}_nb'))
# Configuration file for build.
val <- stringr::str_interp('_${opt$edition}_bookdown.yml')
# Markdown output config.
# See: https://github.com/rstudio/bookdown/issues/782
fmt <- bookdown::markdown_document2(base_format=rmarkdown::md_document)
# Turn off citation links.
fmt$pandoc$args <- c(fmt$pandoc$args,
                     '--metadata',
                     'link-citations=no')
# Build single Markdown output document.
# This command raises an error - see:
# https://github.com/rstudio/bookdown/issues/835
bookdown::render_book('index.Rmd', fmt,
                      config_file=val,
                      output_dir=opt$out_dir)

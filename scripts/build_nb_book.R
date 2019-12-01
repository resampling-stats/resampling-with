#!/usr/bin/env Rscript

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

opt_parser <- optparse::OptionParser(option_list=opt_list)
opt__ <- optparse::parse_args(opt_parser)

if (is.null(opt__$edition)){
  print_help(opt_parser)
  stop("Specify edition", call.=FALSE)
}
opt__$edition <- tolower(opt__$edition)
if (!is.element(opt__$edition, c('python', 'r'))) {
  print_help(opt_parser)
  stop("edition must be 'python' or 'r'", call.=FALSE)
}
if (is.null(opt__$out_dir)){
  print_help(opt_parser)
  stop("Specify output directory", call.=FALSE)
}

# Signal notebook version to _common.R
Sys.setenv(BOOK_ED=stringr::str_interp('${opt__$edition}-nb'))
# Configuration file for build.
opt__$config <- stringr::str_interp('_${opt__$edition}_bookdown.yml')
# Markdown output config.
# See: https://github.com/rstudio/bookdown/issues/782
opt__$fmt <- bookdown::markdown_document2(base_format=rmarkdown::md_document)
# Turn off citation links.
opt__$fmt$pandoc$args <- c(opt__$fmt$pandoc$args,
                     '--metadata',
                     'link-citations=no')
# Build single Markdown output document.
# See https://github.com/rstudio/bookdown/issues/835
# for explanation of clean_envir
rm(opt_list, opt_parser)
bookdown::render_book('index.Rmd', opt__$fmt,
                      clean_envir=FALSE,
                      config_file=opt__$config,
                      output_dir=opt__$out_dir)

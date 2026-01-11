# Common options for all chapters

# Quarto variables for later use.
._variables <- yaml::yaml.load_file(input = '_variables.yml')
._lang <- tolower(._variables$lang);
._profile <- paste("_quarto-", ._lang, ".yml", sep="")
._spec <- yaml::yaml.load_file(input = ._profile)

# Code outputs
options(digits = 3)

knitr::opts_chunk$set(
  comment = ._spec$knitr_settings$`out_comment`,
  cache = TRUE,
  out.width = "70%",
  fig.align = 'center',
  fig.width = 6,
  fig.asp = 0.618,  # 1 / phi
  fig.show = "hold",
  # See:
  # https://stackoverflow.com/questions/76732162/is-there-a-way-to-detect-the-chunk-language-when-setting-knitr-chunk-options
  # and hooks below.
  eval = NA,
  echo = NA,
  # See: https://github.com/rstudio/reticulate/issues/1387
  jupyter_compat = TRUE  # Reticulate enable - only show repr for last expr
)

options(dplyr.print_min = 6, dplyr.print_max = 6)

# Book edition from notebook format in build spec
is_py_ed <- ._spec$processing$language == 'python'
is_r_ed <- !is_py_ed

knitr::opts_template$set(svg_fig = list(eval=TRUE, echo=FALSE,
                                        fig.align='center'))

# For Python code.
library(reticulate)

# Make code output more predictable.
._seed <- 1014
set.seed(._seed)
# For pick-up by Python initialization.
reticulate::py_run_string(paste("_QUARTO_SEED =", ._seed))
reticulate::source_python('_common.py')

# Nice-looking table.
ketable <- function(df, caption) {
  rt <- kableExtra::kable(df, caption = caption, booktabs = TRUE)
  if (knitr::is_latex_output()) { return(rt) }
  # See https://cran.r-project.org/web/packages/kableExtra/vignettes/awesome_table_in_html.html
  # Update table-style.html to match
  kableExtra::kable_paper(
    rt,
    lightable_options = c("striped", "hover"),
    latex_options = c("striped", "scale_down"),
    full_width = FALSE,
    position = "center"
  )
}


# Including SVG
# https://stackoverflow.com/a/56044642/1939576
# Notice need for `rsvg-convert` binary.
include_svg = function(path) {
  if (knitr::is_latex_output()) {
    output = xfun::with_ext(path, 'pdf')
    # you can compare the timestamp of pdf against svg to avoid conversion if necessary
    system2('rsvg-convert', c('-f', 'pdf', '-a', '-o', shQuote(c(output, path))))
  } else {
    output = path
  }
  knitr::include_graphics(output)
}

# Python variable in Python edition else R variable.
get_var = function(name) {
  if (is_py_ed) {
    return (py[[name]])
  }
  return (get(name))
}

._n2t <- c('zero', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine')

# Convert number to text word.
int2tw <- function(i) {
    if (i >= 0 & i <= 9) { return (._n2t[i + 1]) }
    return (paste(i))
}

# Ensure not exponential
# https://stackoverflow.com/a/25946211/1939576
not_e <- function(i) {
    return (format(i, scientific=FALSE))
}

# See: https://stackoverflow.com/questions/76732162/is-there-a-way-to-detect-the-chunk-language-when-setting-knitr-chunk-options
set_true_for_matching_lang <- function(options, field) {
    if (is.na(options[[field]])) {
      options[[field]] <- (tolower(options$engine) == ._lang)
    }
    return (options)
}

knitr::opts_hooks$set(
  echo = function(options) {
      return (set_true_for_matching_lang(options, 'echo'))
  },
  eval = function(options) {
      return (set_true_for_matching_lang(options, 'eval'))
  })

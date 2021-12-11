# Common options for all chapters

# Quarto variables for later use.
._spec <- yaml::yaml.load_file(input = '_quarto.yml')

# Code outputs
options(digits = 3)

knitr::opts_chunk$set(
  comment = ._spec$knitr$`out-comment`,
  cache = TRUE,
  out.width = "70%",
  fig.align = 'center',
  fig.width = 6,
  fig.asp = 0.618,  # 1 / phi
  fig.show = "hold"
)

options(dplyr.print_min = 6, dplyr.print_max = 6)

# Book edition from notebook format in build spec
is_py_ed <- ._spec$noteout$`nb-format` == 'ipynb'
is_r_ed <- !is_py_ed

knitr::opts_template$set(r_ed = list(eval=is_r_ed, echo=is_r_ed),
                         py_ed = list(eval=is_py_ed, echo=is_py_ed))

# For Python code.
library(reticulate)

# Make code output more predictable.
._seed <- 1014
set.seed(._seed)
py_set_seed(._seed)

# Nice-looking table.
ketable <- function(df, caption) {
  rt <- kableExtra::kable(df, caption = caption, booktabs = T)
  if (knitr::is_latex_output()) { return(rt) }
  # See https://cran.r-project.org/web/packages/kableExtra/vignettes/awesome_table_in_html.html
  # Update table-style.html to match
  kableExtra::kable_paper(
    rt,
    lightable_options = c("striped", "hover"),
    latex_options = c("striped", "scale_down"),
    full_width = F,
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

# Common options for all chapters
set.seed(1014)
options(digits = 3)

knitr::opts_chunk$set(
  comment = "#>",
  collapse = TRUE,
  cache = TRUE,
  out.width = "70%",
  fig.align = 'center',
  fig.width = 6,
  fig.asp = 0.618,  # 1 / phi
  fig.show = "hold"
)

options(dplyr.print_min = 6, dplyr.print_max = 6)

# Book edition from environment variable
book_edition <- Sys.getenv('BOOK_ED')

# Default is Python edition
if (book_edition == "") {
    book_edition <- 'python'
}

# Can be notebook edition, as in 'python-nb'
._parts <- strsplit(book_edition, '-')[[1]]
book_edition <-._parts[1]
._nb_part <- ._parts[2]
is_nb <- if (!is.na(._nb_part) & ._nb_part == 'nb') TRUE else FALSE

is_r_ed <- book_edition == 'r'
is_py_ed <- book_edition == 'python'
eval_r_ed = is_r_ed & !is_nb
eval_py_ed = is_py_ed & !is_nb

# For conditional inclusion of text blocks.
comment_start <- "<!---"
comment_end <- "-->"
begin_ispy <- function () { return ( if (!is_py_ed) { comment_start } ) }
end_ispy <- function () { return ( if (!is_py_ed) { comment_end } )  }
begin_isr <- function () { return ( if (!is_r_ed) { comment_start } ) }
end_isr <- function () { return ( if (!is_r_ed) { comment_end } ) }
begin_isnb <- function (nb_fname) { return ( if (!is_nb) { comment_start } ) }
end_isnb <- function () { return ( if (!is_nb) { comment_end } ) }
nb_ext <- if (is_py_ed) 'ipynb' else 'Rmd'

begin_nb <- function(nb_fname) {
    nb_path <- stringr::str_interp('${nb_fname}.${nb_ext}')
    if (!is_nb) {
        return (stringr::str_interp('[Download ${nb_fname} notebook](${nb_path})'))
    }
    return (stringr::str_interp('${comment_start} nb:${nb_path} ${comment_end}'))
}

end_nb <- function() {
    if (is_nb) {
        return (stringr::str_interp('${comment_start} nb:end ${comment_end}'))
    }
}

# Language for use inside Markdown text.
# Use with:
#  Now some code in the `r book_lang` language.
book_lang <- paste(toupper(substring(book_edition, 1,1)),
                   substring(book_edition, 2), sep="")
# Shortcut, it's boring to type.
BL <- book_lang

knitr::opts_template$set(r_ed = list(eval=is_r_ed, echo=is_r_ed),
                         py_ed = list(eval=eval_py_ed, echo=is_py_ed))

# For Python code.
library(reticulate)

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

other_edition <- if (book_edition == 'python') 'r' else 'python'

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
py_or_r <- function(is_py, is_r, backticks=TRUE) {
    result <- if (is_py_ed) is_py else is_r
    if (backticks) stringr::str_interp("`${result}`") else result
}

nb_ext <- if (is_py_ed) 'ipynb' else 'Rmd'

binder_url__ ='https://mybinder.org/v2/gh/resampling-stats/resampling-with/gh-pages?filepath=python-book/'

# Parsing somehow fails for multiline strings, so split and join.
nb_template__ <- paste('<div class="rmdcomment">\n',
                       '<p>Start of <code>${nb_fname}</code> notebook.</p>\n',
                       '<p>',
                       '<div class="nb-links">',
                       '<a class="notebook-link" href=${nb_path}>Download notebook</a>',
                       if (is_py_ed) '<a class="interact-button" href="${binder_url__}${nb_path}">Interact</a>' else NULL,
                       '</p>',
                       '</div>',
                       '</div>\n',
                       sep='\n')

nb_begin__ <- function(nb_fname, nb_path) {
    # Omit notebook links unless HTML-like format.
    if (knitr::is_html_output()) {
        return (stringr::str_interp(nb_template__))
    }
}

begin_nb <- function(nb_fname) {
    assign("nb_fname__", nb_fname, envir = .GlobalEnv)
    nb_path <- stringr::str_interp('${nb_fname}.${nb_ext}')
    if (!is_nb) {
        return (nb_begin__(nb_fname, nb_path))
    }
    return (stringr::str_interp('${comment_start} nb:${nb_path} ${comment_end}'))
}

begin_callout <- function(title) {
    if (knitr::is_latex_output()) {
        return (stringr::str_interp(paste(
':::: {.tcolorbox data-latex=""}\n',
'**${title}**\n',
sep='\n')))
    }
    return (stringr::str_interp(paste(
':::: {.callout}',
'::: {.title}',
'${title}',
':::\n',
sep='\n')))
}

end_callout <- function() {
    '\n::::\n'
}

end_nb <- function() {
    if (is_nb) {
        return (stringr::str_interp('${comment_start} nb:end ${comment_end}'))
    } else {
        # Parsing fails for multiline strings, use paste instead.
        return (stringr::str_interp(paste(
'<div class="rmdcomment">\n',
'<p>End of <code>${nb_fname__}</code> notebook.</p>\n',
'</div>\n',
sep='\n')))
    }
    assign("nb_fname__", NULL, envir = .GlobalEnv)
}

# Language for use inside Markdown text.
# Use with:
#  Now some code in the `r book_lang` language.
book_lang <- paste(toupper(substring(book_edition, 1,1)),
                   substring(book_edition, 2), sep="")
other_lang <- paste(toupper(substring(other_edition, 1,1)),
                   substring(other_edition, 2), sep="")
# Shortcut, it's boring to type.
BL <- book_lang

knitr::opts_template$set(r_ed = list(eval=is_r_ed, echo=is_r_ed),
                         py_ed = list(eval=eval_py_ed, echo=is_py_ed))

# For Python code.
library(reticulate)

# Nice-looking table.
ketable <- function(df, caption) {
    rt <- kableExtra::kable(df, caption = caption, booktabs = T)
    if (knitr::is_latex_output()) {
        return(kableExtra::kable_styling(rt, latex_options = 'scale_down'))
    }
    # See https://cran.r-project.org/web/packages/kableExtra/vignettes/awesome_table_in_html.html
    # Update table-style.html to match
    kableExtra::kable_paper(rt,
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

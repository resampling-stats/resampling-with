# To do

## Binderhub setup for Python version

Need something to embed link to BinderHub notebook.

Maybe Javascript in CSS?

Or Macro of form:

~~~
`r binderhub()`
~~~

Where:

```{r}
binderhub <- function() {
    fname <- knitr::current_input()
    # Maybe generate outputs
    # etc
}
```

[SO question about Bookdown output directory](https://stackoverflow.com/questions/57737225/programmatic-way-to-get-output-directory-in-bookdown).

Will need to generate notebooks.  Maybe use `.md` processed
files, convert back to notebook.  Could do this crudely by
looking for python code blocks, restoring the `{python}` header
and removing output.

Conditional chunks depending on output format:
<https://github.com/rstudio/bookdown/issues/168>.

Chase up Hollander and Wolfe reference from end of chapter 18, p295.



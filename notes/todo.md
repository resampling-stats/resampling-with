# To do

## Gently work up to using `choice` with `p`

We want to get to using `choice(['foo', 'bar'], p=[0.7, 0.3])`

Start with say using random integers, or choice with the correct proportion of
inputs (`choice(['foo'] * 7 + ['bar'] * 3])`). Work up to probability, and the
`p=` form above.

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



# Resampling statistics, third edition

Material for updated (third) edition of [Resampling: The New Statistics,
second edition](http://www.resample.com/intro-text-online) by Julian L. Simon.

The new edition is by Julian L. Simon with Matthew Brett, Stéfan van der Walt
and Ian Nimmo-Smith.

The latest version will always be at the [book
website](https://resampling-stats.github.io/resampling-with).

We release the material in this repository under
a [CC-BY-ND](https://creativecommons.org/licenses/by-nd/4.0) license, unless
otherwise specified. See `LICENSE.md` in this directory for details.

The source text that we build to the book is in the `source` directory.

There are source (Markdown) versions of chapters from the second edition in the
`unported` directory.  As we fill out the third edition, we move these files
into the `source` directory, and edit them there.

## Setup for editing and proofing

```{bash}
export PIP_INSTALL_CMD="pip install"
make build-init
```

For a full build, you will also need the `rsvg-convert` program.   On Mac I (MB) installed that with:

```
brew install librsvg
```

See [the Pandoc installation guide](https://pandoc.org/installing.html) for
suggestions to install `rsvg-convert` on other platforms.

Make sure that your `rmarkdown` package is sufficiently up to date to work
with your `pandoc` version.  Versions of `pandoc` >= 2.11 use `--citeproc` and
not `--filter pandoc-citeproc`; if your `rmarkdown` version is older than 2.5
(`library(rmarkdown); sessionInfo()`), it won't know that, and therefore will
raise an error on book build - see [RMarkdown release
notes](https://github.com/rstudio/rmarkdown/releases).  Upgrade with
`install.packages('rmarkdown')`.

### Quarto

We use [Quarto](https://quarto.org) as the build machinery for the website and for PDF.

See [the Quarto installation instructions](https://quarto.org/docs/getting-started/installation.html).  Afterwards, install the matching R package.

```
Rscript -e 'install.packages("quarto")'
```

If it complains about the CRAN mirror not set, add the following to `~/.Rprofile` and try again:

```
local({r <- getOption("repos")
       r["CRAN"] <- "http://cran.r-project.org"
       options(repos=r)})
```

The process may fail if it cannot find curl and openssl development headers.
The error message explains how to install those headers on the various systems.
For example, on Fedora it'd be:

```
sudo dnf install libcurl-devel openssl-devel
```

Finally, check the installation:

```
quarto check install
quarto check knitr
```

Quarto uses various [Pandoc markdown
extensions](https://linux.die.net/man/5/pandoc_markdown), as do we (Div and
Span elements for custom inline elements and blocks).

# Writing and updating the text

First follow the build instructions above.

Activate your virtual environment for the book, if you are using one.  In my
(MB's) case, I use [Virtualenvs](https://virtualenv.pypa.io) and
[VirtualenvWrapper](https://virtualenvwrapper.readthedocs.io) to do this:

```
workon resampling-with
```

This activates my installed virtualenv environment for the book.

Make sure you can build the whole book in your current environment with:

```
make clean && make python-book
make clean && make r-book
```

Be careful - and note the `make clean`s above - it seems that caching can trip
up the build.  In general, try `make clean` if you run into puzzling build
problems with data frames not defined, that are clearly defined, or missing
imports that are not missing.

from the top-level repository directory.   If this doesn't work, make an [Issue
on Github](https://github.com/resampling-stats/resampling-with/issues).

After you've confirmed you can build both the Python and the R edition, you may
want to work on only one of these editions — say the Python book, and clean up
the R book later (or the other way round).

Matthew and Peter know R reasonably well — we can help with R cleanup.

## Starting work on a new chapter

See the `./source/_quarto.yml.template` file for
a list of the chapters currently in the book build.

Let's say you want to start work on one of the chapters, and you've see this in the `_quarto.yml.template` file:

```
    - reliability_average.Rmd
```

The procedure is:

Before you start:

* Make a new Git branch, and check out the branch.
* `cd source`

*   Choose which edition of the book you are going
    to work on, and set the build to that edition
    with:

    ```
    make set-version-python
    ```

    or

    ```
    make set-version-r
    ```

    from the `./source` directory.

Editing:

* Edit the matching file - here `source/reliability_average.Rmd`.
* You might find it useful to have the original PDF
  chapter open; see [the
  original book in
  PDF](https://resample.com/intro-text-online).  The
  PDFs are also in the `./unported` directory of the
  repository.  To see which original chapter
  corresponds to your current `.Rmd` file, have
  a look at the YAML fragment at the file, it should
  have something like: `ed2_fname: 26-Chap-22`. See
  also the chapter mappings at the end of this page.
* Rebuild the file you're working on from time to time with e.g.
  `../scripts/rebuild_chapter reliability_average.Rmd` from the `source`
  directory. Check the contents by opening e.g.
  `../python-book/reliability_average.Rmd` (Quarto will show the correct
  filename after the rebuild step).
* When in some kind of shape that is ready for other people to look at, make
  your commits with the changes, and do a pull-request to the main repository,
  for us to look at.
* In due course you may want to remove the boilerplate warning text at the top
  of the page.

## Notebooks

Make a notebook section with e.g.

~~~
::: {.notebook name="ambulances" title="Ambulances"}

Stuff

```{python, opts.label="py_ed"}
# A Python cell - it only gets run in the Python edition.
k = 1
```

```{r, opts.label="r_ed"}
# An R cell - it only gets run in the R edition
k <- 1
```

The value of `k` is `r get_var('k')`.

:::
~~~

## Content that should go only in the output notebooks

The notebooks (above) get written out as separate documents.  By default, they may lack some context, if the reader can't see the preceding text in the chapter.  So, sometimes it's useful to put an introductory paragraph at the top of the notebook to give the context, but where that paragraph does not appear in the main text, like this:

~~~
::: {.notebook name="another_notebook" title="Another Notebook"}

::: nb-only
This appears only in the output notebook file, and not in the main text.
:::

```{python, opts.label="py_ed"}
# A Python cell.
k = 1
```

```{r, opts.label="r_ed"}
# An R cell.
k <- 1
```
:::
~~~

## Edition-specific content

You have inline and block markup to put content into just the R edition, or just the Python edition:

~~~
::: r

This only appears in the R edition
:::

::: python

This only appears in the Python edition
:::

This content appears [only in the R edition]{.r}[just in the Python
book]{.python}.
~~~

If you find yourself doing that often, you can define a version-dependent variable in the `text_variables.yml` file.  This gets built out into the `_variables.yml` file with your `make set-version-r` or `make set-version-python`.  Use it with e.g.

~~~
Here I have text that depends on the version of the book — {{< var my_var >}}
— as determined by the `text_variables.yml` file.
~~~

## Citations

Citations are in [Pandoc format](https://pandoc.org/MANUAL.html#citations), as
implemented in [Quarto's
citations](https://quarto.org/docs/authoring/footnotes-and-citations.html).

Check that the reference is not already in `source/simon_refs.bib`.  Add it if
so, following reference name standard in that file (e.g.
`@article{christensen2005fisher,`).  Cite with e.g. `This is a terrible idea
[@christensen2005fisher]` or `As Christensen notes [-@christensen2005fisher]`,
or `There are many good ways to do this [see @knuth1984, pp. 33-35; also
@wickham2015, chap. 1]`.  See Quarto link above for other examples.

## Footnotes

See [Quarto footnotes](https://quarto.org/docs/authoring/footnotes-and-citations.html#footnotes))

Examples (from that page):

```
Here is a footnote reference,[^1] and another.[^longnote]

[^1]: Here is the footnote.

[^longnote]: Here's one with multiple blocks.

    Subsequent paragraphs are indented to show that they
    belong to the previous footnote.

Here is an inline note.^[Inlines notes are easier to write,
since you don't have to pick an identifier and move down to
type the note.]
```

**Notice that you'll need full 4-space indentation to keep the footnote
paragraphs within the footnote**.

## Writing notes for the reader (callout)

See [Quarto callouts](https://quarto.org/docs/authoring/callouts.html)

```
:::{.callout-note}
## A title for the note

Some text
:::
```

Also `.callout-warning`, `-tip`, `-important`, `-caution`.

## Comments to your fellow authors

HTML comments:

```
<!---
More here on something and something else
-->
```

Note the triple dash in the first line, as in `<!---`.

## Cross-references

See [Cross-references in
Quarto](https://quarto.org/docs/authoring/cross-references.html).  Summary for
section reference: add `{#sec-name-for-your-ref}` to the target section title,
reference with `Please see section @name-for-your-ref for details`.

## Useful links

* [The original book in PDF](https://resample.com/intro-text-online). MB has
the print book.

## Notes for concepts in other discussions in the book

See [the notes repository](https://github.com/resampling-stats/resampling-roam)
for more discussions of various concepts in the book, and how we are thinking
about them.

## Chapter mappings

These are the mappings between the files in the `./source` directory, and the
original chapters from the [second edition
website](https://resample.com/intro-text-online).  You can find basic Markdown
ports of the original second edition PDF chapters in the `./unported` directory
of the repository.

See also `./source/_quarto.yml.template` for files making up chapters in current
built book.

| Third edition file | Second edition file(s) | Third edition chapter title |
| ------------------ | ------------------- | ---------- |
| preface_third.Rmd | N/A | Preface to the third edition |
| preface_second.Rmd | 01-Preface | Preface to the second edition |
| intro.Rmd | 02-Intro, 04-Afternote-2 | Introduction |
| monty_hall.Rmd | N/A | N/A |
| dramatizing_resampling.Rmd | 03-Afternote-1 | N/A |
| resampling_method.Rmd | 05-Chap-1 | The resampling method |
| about_technology.Rmd | N/A | Introducing Python ... |
| resampling_with_code.Rmd | N/A | Resampling with code |
| resampling_with_code2.Rmd | N/A | More resampling with code |
| what_is_probability.Rmd | 06-Chap-2, 07-Chap-3 | What is probability? |
| probability_theory_1a.Rmd | 08-Chap-4 | NA |
| probability_theory_1b.Rmd | 09-Chap-5 | NA |
| probability_theory_2_compound.Rmd | 10-Chap-6 | NA |
| probability_theory_3.Rmd | 11-Chap-7 | NA |
| probability_theory_4_finite.Rmd | 12-Chap-8 | NA |
| sampling_variability.Rmd | 13-Chap-9 | NA |
| monte_carlo.Rmd | 14-Chap-10 | NA |
| inference_ideas.Rmd | 15-Chap-11 | NA |
| inference_intro.Rmd | 16-Chap-12 | NA |
| point_estimation.Rmd | 17-Chap-13 | NA |
| framing_questions.Rmd | 18-Chap-14 | NA |
| testing_counts_1.Rmd | 19-Chap-15 | NA |
| significance.Rmd | 20-Chap-16 | NA |
| testing_counts_2.Rmd | 21-Chap-17 | NA |
| testing_measured.Rmd | 22-Chap-18 | NA |
| testing_procedures.Rmd | 23-Chap-19 | NA |
| confidence_1.Rmd | 24-Chap-20 | NA |
| confidence_2.Rmd | 25-Chap-21 | NA |
| reliability_average.Rmd | 26-Chap-22 | NA |
| correlation_causation.Rmd | 27-Chap-23 | NA |
| how_big_sample.Rmd | 28-Chap-24 | NA |
| bayes_simulation.Rmd | 29-Chap-25 | NA |
| exercise_solutions.Rmd | 30-Exercise-sol | NA |
| acknowlegements.Rmd | acknow | NA |
| technical_note.Rmd | Technical | NA |

Initial text for this table generated using:

```
grep ed2_fname *.Rmd | grep -v _main | sed 's/:.*ed2_fname//' | sort -t ':' -k 2 -
```

# Notes for writing and updating the text

First follow the build instructions in the top-level README : `../README.md`.

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

from the top-level repository directory.   If this doesn't work, make an [Issue
on Github](https://github.com/resampling-stats/resampling-with/issues).

After you've confirmed you can build both the Python and the R edition, you may
want to work on only one of these editions — say the Python book, and clean up
the R book later (or the other way round).

Matthew and Peter know R reasonably well — we can help with R cleanup.

## Starting work on a new chapter

See the `./source/_quarto.yml.template` file for a list of the chapters
currently in the book build.  You may see that there are commented-out chapters
from the original book; these do not get built to the online version of the
book.

Let's say you want to start work on one of the chapters, and you've see this in the `_quarto.yml.template` file:

```
#   - reliability_average.Rmd
```

The procedure is:

Before you start:

* Make a new Git branch, and check out the branch.
* `cd source`
* Do (for Python) `make clean && make python-book`.

Editing:

* Edit the matching file - here `source/reliability_average.Rmd`.
* You might find it useful to have the original PDF chapter open; see [the
original book in PDF](https://resample.com/intro-text-online).  To see which
original chapter corresponds to your current `.Rmd` file, have a look at the
YaML fragment at the file, it should have something like: `ed2_fname:
26-Chap-22`.
* Rebuild the file you're working on from time to time with e.g. `quarto render
reliability_average.Rmd --to html` from the `source` directory (note the `--to
html` _after_ the chapter filename).  Check the contents by opening e.g.
`../python-book/reliability_average.Rmd` (Quarto will show the correct filename
after the `quarto render` step).
* When in some kind of shape that is ready for other people to look at,
uncomment the filename in `_quarto.yml.template`.
* Make your commits with the changes, and do a pull-request to the main
repository, for us to look at.

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

## Cross-references

See [Cross-references in
Quarto](https://quarto.org/docs/authoring/cross-references.html).  Summary for
section reference: add `{#sec-name-for-your-ref}` to the target section title,
reference with `Please see section @name-for-your-ref for details`.

## Useful links

* [The original book in PDF](https://resample.com/intro-text-online). MB has
the print book.

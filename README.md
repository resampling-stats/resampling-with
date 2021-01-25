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

Make sure that your `rmarkdown` package is sufficiently up to date to work
with your `pandoc` version.  Versions of `pandoc` >= 2.11 use `--citeproc` and
not `--filter pandoc-citeproc`; if your `rmarkdown` version is older than 2.5
(`library(rmarkdown); sessionInfo()`), it won't know that, and therefore will
raise an error on book build - see [RMarkdown release
notes](https://github.com/rstudio/rmarkdown/releases).  Upgrade with
`install.packages('rmarkdown')`.

## A build

For Python (*mutatis mutandis* for R):

```
make python-all
```

Then, to rebuild an individual chapter:

```
./scripts/rebuild_chapter.sh source/bayes_simulation.Rmd
```

*You need to do a full build first before the individual chapter build will work*.  The script should warn you about this if you forget.

If you get errors you weren't expecting, try:

```
make clean
make python-all
```

It seems that caching can trip up the build.


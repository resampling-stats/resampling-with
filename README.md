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

## Building the book

See `source/README.md`.

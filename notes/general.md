# Notes

## Operational definition

See [Stanford dictionary of philosophy article](https://plato.stanford.edu/entries/operationalism):

> We evidently know what we mean by length if we can tell what the length of
> any and every object is, and for the physicist nothing more is required. To
> find the length of an object, we have to perform certain physical operations.
> The concept of length is therefore fixed when the operations by which length is
> measured are fixed: that is, the concept of length involves as much as and
> nothing more than the set of operations by which length is determined. In
> general, we mean by any concept nothing more than a set of operations; the
> concept is synonymous with the corresponding set of operations. (Bridgman
> 1927, 5)

Reference is:

> Bridgman, Percy Williams. 1927. The Logic of Modern Physics. New York:
> Macmillan.

An *operational definition* of *X* is a definition of *X* in terms of the
procedure used to measure *X*.

## Julian Simon and the origin of the bootstrap

> The idea of resampling from the empirical distribution to form a Monte Carlo
> approximation to the bootstrap estimate may have been thought of and used prior
> to Efron. Simon (1969) has been referenced by some to indicate his use of the
> idea as a tool in teaching elementary statistics prior to Efron. Bruce and
> Simon have been instrumental in popularizing the bootstrap approach through
> their company Resampling Stats Inc. and their associated software. They also
> continue to use the Monte Carlo approximation to the bootstrap as a tool for
> introducing statistical concepts in a first elementary course in statistics
> [see Simon and Bruce (1991, 1995)]. Julian Simon died several years ago; but
> Peter Bruce continues to run the company and in addition to teaching resampling
> in online courses, he has set up a faculty to teach a variety of online
> statistics courses.
>
> It is clear, however, that widespread use of the methods (particularly by
> professional statisticians) along with the many theoretical developments
> occurred only after Efron's 1979 work. That paper (Efron, 1979a) connected the
> simple bootstrap idea to established methods for estimating the standard error
> of an estimator, namely, the jackknife, cross-validation, and the delta method,
> thus providing the theoretical underpinnings that that were then further
> developed by Efron and other researchers.

See [Bootstrap Methods: A Guide for Practitioners and
Researchers](http://www.dmmserver.com/DialABook/978/047/175/9780471756217.html)
Michael R. Chernick (2008) John Wiley & Sons.

Check in chapter 2 of Good (2006ish) Resampling Methods for references to
Simon.

> In 1969, his pro- motion of resampling methods for testing statistical
> hypotheses must have seemed only moderately practical. Nevertheless, his
> prediction that this approach "holds great promise for the future" (Simon,
> 1969) cannot be faulted.

Hall (2003) [A short prehistory of the
bootstrap](https://www.jstor.org/stable/pdf/3182845.pdf). Statistical Science,
Vol. 18, No. 2, Silver Anniversary of the Bootstrap (May, 2003), pp. 158-167

<http://statistics101.net> has a clone of ResamplingStats, with extensions, and
a tutorial.

Graunt and some statistical errors:

Page 168 in original

* http://www.edstephan.org/Graunt/11-12.html#twelve
* http://www.edstephan.org/Graunt/bills.html

## Fisher, Neyman-Pearson

Some references on Fisher and Neyman-Pearson:
<https://stats.stackexchange.com/questions/23142/when-to-use-fisher-and-neyman-pearson-framework>.

## Confidence intervals

* <https://www.statsdirect.com/help/basics/confidence_interval.htm>
* Citation in [credible
  intervals](https://www.statisticshowto.datasciencecentral.com/credible-interval/)
  page: Jaynes, E. T. (1976). “Confidence Intervals vs Bayesian
  Intervals”, in Foundations of Probability Theory, Statistical
  Inference, and Statistical Theories of Science, pp. 175 et
  seq. Retrieved from
  <http://bayes.wustl.edu/etj/articles/confidence.pdf> on February 17, 2018 
* [Confidence intervals
  page](https://www.stat.berkeley.edu/~stark/SticiGui/Text/confidenceIntervals.htm)
  in
  [SticiGui](https://www.stat.berkeley.edu/~stark/SticiGui/index.htm)
  by Philip Stark.

## Thoughts

### Do we need to introduce the normal distribution?

How about approximations based on the normal distribution?

Mentioned in chapters 3, 12, 15, 16, 18-23, 25.

[Discussion of capitalization of normal](https://stats.stackexchange.com/questions/173458/should-i-capitalise-the-n-in-normal-distribution-in-british-english) as in "normal distribution".

### Standard deviation

Standard deviation mentioned in a quote by Kinsey in the introduction, and a footnote in chapter 6, but not thereafter until chapter 18, where it is defined, with variance, very briefly.  Then mentioned as measure of spread in chapter 19, and used to make Z scores.

Thence mentioned a couple of times in chapters 20 and 21 (confidence intervals).

## Central Limit Theorem

* Mentioned as to be explained in Chapter 3, with Normal
  distribution, but not explained later.

## Bootstrap

Mentioned in preface, thence chapters 7, 12, 14, 15, 18, 21, 24, 25.  Check definition.

## Bibtex references

* [Examples](https://www.verbosus.com/bibtex-style-examples.html)

## Bookdown etc

* [Bookdown](https://bookdown.org/yihui/bookdown)
* [RMarkdown](https://rmarkdown.rstudio.com)
* [Knitr](https://yihui.name/knitr)
* [Reticulate](https://rstudio.github.io/reticulate)
* [R for data science](https://r4ds.had.co.nz)

I got going with Bookdown starting from the [R4DS
repo](https://github.com/hadley/r4ds).

## Definitions

* Statistic
* Probability statistic
* Probability, odds, chances

## Julian Simon sites

* [Julian Simon's website](http://juliansimon.com)
* Archive.org backup of [Resampling
  Intro](https://web.archive.org/web/19990224190319/http://www.inform.umd.edu/EdRes/Topic/Statistics/Resampling_Statistics).

## Citations

See <https://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html>

## Code topics

* Comments after code lines - as in `print(a)  # Print the result`
  (sampling_tools).
* strings (sampling_tools)
* arrays and data types (sampling_tools)
* lists (done in sampling_tools)
* indentation (maybe in resampling_with_code2 and for loops)
* bincount / tabulate (probability_theory_2_compound).
* Maybe more on Boolean arrays.
* (a == 1) & (b == 3) (in `more_sampling_tools`)
* Python `range` cf `np.arange` (`resampling_with_code`)
* `np.all` (done in `probabality_theory_4_finite`).
* `hist` / `plt.hist`, at least by `probabality_theory_3` (in
  `probability_theory_3`), covering plotting, bins, bin edges.  We might
  consider a chapter on histograms.
* Need slicing with slices — done in `more_sampling_tools`.
  Also used in `standard_scores` around line 319.
* Introduce the idea of objects and classes.  First obviously needed in
  `standard_scores.Rmd` page, see line that currently reads:

  > data from that column, returning a new type of value called a Pandas
  > *Series*.

* Underscores in Python integers by `testing_counts_1` (done in
  `testing_counts_1`).
* `seq` / `np.arange` with floats done in `testing_counts_1`.
* `paste` and f-strings done in `testing_counts_1` (sec-building-strings).
* `or` / `|` in `testing_counts_2` (sec-logical-operators).
* `if` statements in `probability_theory_1a` (sec-if-statements).
* `abs` covered in `standard_scores`, around line 1060.
* `**` or `^` for squaring values, `standard_scores` around line 1141.
* Concatenation covered in
  `probability_theory_3.Rmd`. (`np.concatenate` and
  `c` for vectors).

## Data

Maybe from [Beer,
mosquitoes](https://github.com/odsti/datasets/tree/main/mosquito_beer)

> If we have data, let’s look at data. If all we have are opinions, let’s go
> with mine. – Jim Barksdale, former Netscape CEO - for example at [this book](https://www.oreilly.com/library/view/analytics-and-dynamic/9781118919774/9781118919774c05.xhtml)

## resampling stats commands

### SAMPLE

This is resampling _with_ replacement.

---
jupyter:
  jupytext:
    metadata_filter:
      notebook:
        additional: all
        excluded:
        - language_info
    text_representation:
      extension: .Rmd
      format_name: rmarkdown
      format_version: '1.0'
      jupytext_version: 0.8.6
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
resampling_with:
    ed2_fname: 02-Intro
    # Also:
    # "04-Afternote-2.Rmd" - incorporated into intro.Rmd
---

# Introduction

## Uses of Probability and Statistics

This chapter introduces you to probability and statistics. First come
examples of the kinds of practical problems that this knowledge can
solve for us. Next this Introduction discusses the relationship of
probabilities to decisions. Then comes a discussion of the two general
types of statistics, descriptive and inferential. Following this is a
discussion of the limitations of probability and statistics. And last is
a discussion of why statistics can be such a difficult subject. Most important,
this chapter describes the types of problems the book will tackle.

Because the term "statistic" often scares and confuses people--- and
indeed, the term has several sorts of meanings---the chapter includes a
short section on "Types of Statistics." Descriptive statistics are
numbers that summarize the information contained in a group of data.
Inferential statistics are procedures to estimate unknown quantities;
that is, these procedures infer estimates and conclusions based on
whatever descriptive statistics are available.

At the foundation of sound decision-making lies the ability to make
accurate estimates of the probabilities of future events. Probabilistic
problems confront everyone---from the business person considering plant
expansion, to the scientist testing a new wonder drug, to the individual
deciding whether to carry an umbrella to work.

## What kinds of problems shall we solve? {#what-problems}

These are some examples of the kinds of problems that we can handle with
the methods described in this book:

1.  *You are a doctor* trying to develop a cure for cancer. Currently
    you are working on a medicine labeled CCC. You have data from
    patients to whom medicine CCC was given. You want to judge on the
    basis of those results whether CCC really cures cancer or whether it
    is no better than a sugar pill.

2.  *You are the campaign manager* for the Republicrat candidate for
    President of the United States. You have the results from a recent
    poll taken in New Hampshire. You want to know the chance that your
    candidate would win in New Hampshire if the election were held
    today.

3.  *You are the manager and part owner* of one of several contractors
    providing ambulances to a hospital. You own 12 ambulances. The chance that
    any one ambulance will be unfit for service on any given day is about one
    in ten. You want to know the chance on a particular day--- tomorrow---that
    three or more of them will be out of action.

4.  *A machine gauged to produce screws* 1.000 inches long produces a
    batch on Tuesday that averaged 1.010 inches. Given the record of
    screws produced by this machine over the past month, we want to know
    whether something about the machine has changed, or whether this
    unusual batch has occurred just by chance.

The core of all these problems, and of the others that we will deal with
in this book, is that you want to know the "chance" or
"probability"---different words for the same idea---that some event will
or will not happen, or that something is true or false. To put it
another way, we want to answer questions about "What is the probability
that\...?", given the body of information that you have in hand.

The question "What is the probability that\...?" is usually not the
ultimate question that interests us at a given moment.

Eventually, a person wants to use the estimated probability to help make
a *decision* concerning some action one might take. These are the kinds
of decisions, related to the questions about probability stated above,
that ultimately we would like to make:

1.  *Should you (the researcher) advise doctors to prescribe medicine
    CCC* for patients, or, should you (the researcher) continue to study
    CCC before releasing it for use? A related matter: should you and
    other research workers feel sufficiently encouraged by the results
    of medicine CCC so that you should continue research in this general
    direction rather than turning to some other promising line of
    research? These are just two of the possible decisions that might be
    influenced by the answer to the question about the probability that
    medicine CCC cures cancer.

2.  *Should you advise the Republicrat presidential candidate to go to
    New Hampshire* to campaign? If the poll tells you conclusively that
    he or she will not win in New Hampshire, you might decide that it is
    not worthwhile investing effort to campaign there. Similarly, if the
    poll tells you conclusively that he or she surely will win in New
    Hampshire, you probably would not want to campaign further there.
    But if the poll is not conclusive in one direction or the other, you
    might choose to invest the effort to campaign in New Hampshire.
    Analysis of the chances of winning in New Hampshire based on the
    poll data can help you make this decision sensibly.

3.  *Should your firm buy more ambulances* ? Clearly the answer to this
    question is affected by the probability that a given number of your
    ambulances will be out of action on a given day. But of course this
    estimated probability will be only one part of the decision.

4.  *Should we adjust the screw-making machine* after it produces the
    batch of screws averaging 1.010 inches? If its performance has not
    changed, and the unusual batch we observed was just the result of
    random variability, adjusting the machine could render it more
    likely to produce off-target screws in the future.

The kinds of questions to which we wish to find probabilistic and
statistical answers may be found throughout the social, biological
and physical sciences; in business; in politics; in engineering
(concerning such spectacular projects as the flight to the moon);
and in most other forms of human endeavor.

## Probabilities and decisions

There are two differences between questions about probabilities and
the ultimate decision problems:

1.  Decision problems always involve *evaluation of the
    consequences* ---that is, taking into account the benefits and
    the costs of the consequences---whereas pure questions about
    probabilities are estimated without evaluations of the
    consequences.

2.  Decision problems often involve a *complex combination* of *sets
    of probabilities and consequences*, together with their
    evaluations. For example: In the case of the contractor's
    ambulances, it is clear that there will be a monetary loss to the
    contractor if she makes a commitment to have 9 ambulances available for
    tomorrow and then cannot produce that many. Furthermore,
    the contractor must take into account the further consequence
    that there *may* be a loss of goodwill for the future if she
    fails to meet her obligations tomorrow---and then again there
    *may not* be any such loss; and if there is such loss of
    goodwill it might be a loss worth \$10,000 *or* \$20,000 *or*
    \$30,000. Here the decision problem involves not only the
    probability that there will be fewer than 9 ambulances tomorrow but
    also the immediate monetary loss and the subsequent possible
    losses of goodwill, and the valuation of all these consequences.

Continuing with the decision concerning whether to do more research on
medicine CCC: If you do decide to continue research on CCC, (a) you may,
or (b) you may not, come up with an important general cure within, say,
the next 3 years. If you do come up with such a general cure, of course
it will have very great social benefits. Furthermore, (c) if you decide
not to do further research on CCC now, you can direct your time and that
of other people to research in other directions, with some chance that
the other research will produce a less-general but nevertheless useful
cure for some relatively infrequent forms of cancer. Those three
possibilities have different social benefits. The probability that
medicine CCC really has some curative effect on cancer, as judged by
your prior research, obviously will influence your decision on whether
or not to do more research on medicine CCC. But that judgment about the
probability is only one part of the overall web of consequences and
evaluations that must be taken into account when making your decision
whether or not to do further research on medicine CCC.

Why does this book limit itself to the specific probability questions
when ultimately we are interested in decisions? A first reason is
division of labor. The more general aspects of the decision-making
process in the face of uncertainty are treated well in other books. This
book's special contribution is its new approach to the crucial process
of estimating the chances that an event will occur.

Second, the specific elements of the overall decision-making process taught in
this book belong to the interrelated subjects of *probability theory* and
*inferential statistics* . Though probabilistic and inferential-statistical
theory ultimately is intended to be part of the general decision-making
process, often only the estimation of probabilities is done systematically, and
the rest of the decision-making process---for example, the decision whether or
not to proceed with further research on medicine CCC---is done in informal and
unsystematic fashion. This is regrettable, but the fact that this is standard
practice is an additional reason why the treatment of inferential statistics
and probability in this book is sufficiently complete.

A third reason that this book covers only inferential statistics and not
decision statistics is because most college and university statistics
courses and books are limited to inferential statistics.

## Types of statistics

The term *statistics* sometimes causes confusion and therefore needs
explanation.

A statistic is a *number* . There are two kinds of statistics, *summarization*
(descriptive) statistics and *probability* statistics. The most important
summarization statistics are the *total*, the *distribution*, measures of the
center of a distribution such as the *mean* and *median*, the *range*, and
other measures of variation.

Such statistics are nothing new to you; you have been using many of them all
your life. Inferential statistics, which this book deals with, uses descriptive
statistics as its input.

Inferential statistics can be used for two purposes: to aid scientific
*understanding* by estimating the probability that a statement is true
or not, and to aid in making *sound decisions* by estimating which
alternative among a range of possibilities is most desirable.

## Limitations of probability and statistics

Statistical testing is not equivalent to research, and research is not the same
as statistical testing. Rather, statistical inference is a handmaiden of
research, often but not always necessary in the research process.

A working knowledge of the basic ideas of statistics, especially the
elements of probability, is unsurpassed in its general value to everyone
in a modern society. Statistics and probability help clarify one's
thinking and improve one's capacity to deal with practical problems and
to understand the world. To be efficient, a social scientist or
decision-maker is almost certain to need statistics and probability.

On the other hand, important research and top-notch decision-making have
been done by people with absolutely no formal knowledge of statistics.
And a limited study of statistics sometimes befuddles students into
thinking that statistical principles are guides to research design and
analysis. This mistaken belief only inhibits the exercise of sound
research thinking. Kinsey long ago put it this way:

> ... no statistical treatment can put validity into generalizations which are
> based on data that were not reasonably accurate and complete to begin with.
> It is unfortunate that academic departments so often offer courses on the
> statistical manipulation of human material to students who have little
> understanding of the problems involved in securing the original data. ...
> When training in these things replaces or at least precedes some of the
> college courses on the mathematical treatment of data, we shall come nearer
> to having a science of human behavior. [@kinsey1948sexual, p 35].

In much---even most---research in social and physical sciences,
statistical testing is not necessary. Where there are large differences
between different sorts of circumstances---for example, if a new
medicine cures 90 patients out of 100 and the old medicine cures only 10
patients out of 100---we do not need refined statistical tests to tell
us whether or not the new medicine really has an effect. And the best
research is that which shows large differences, because it is the large
effects that matter. If the researcher finds that s/he must use refined
statistical tests to reveal whether there are differences, this
sometimes means that the differences do not matter much.

To repeat, then, some or even much research---especially in the physical and
biological sciences---does not need the kind of statistical manipulation that
will be described in this book. But most decision problems *do* need the kind
of probabilistic and statistical input that is described in this book.

Another matter: If the raw data are of poor quality, probabilistic and
statistical manipulation cannot be very useful. In the example of the
contractor and her ambulances, if the contractor's estimate that a given
ambulance has a one-in-ten chance of being unfit for service out-of-order on
a given day is very inaccurate, then our calculation of the probability that
three or more ambulances will be out of order on a given day will not be
helpful, and may be misleading. To put it another way, one cannot make bread
without flour, yeast, and water. And good raw data are the flour, yeast and
water necessary to get an accurate estimate of a probability. The most refined
statistical and probabilistic manipulations are useless if the input data are
poor---the result of unrepresentative samples, uncontrolled experiments,
inaccurate measurement, and the host of other ways that information gathering
can go wrong. (See @simon1985basic for a catalog of the obstacles to obtaining
good data.) Therefore, we should constantly direct our attention to ensuring
that the data upon which we base our calculations are the best it is possible
to obtain.

## Why is Statistics Such a Difficult Subject?

Why is statistics such a tough subject for so many people?

"Among mathematicians and statisticians who teach introductory
statistics, there is a tendency to view students who are not skillful in
mathematics as unintelligent," say two of the authors of a
popular introductory text [@mccabe1989instructors, p 2]. As these authors
imply, this view is out-and-out wrong; lack of general intelligence on the
part of students is *not* the root of the problem.

Scan this book and you will find almost no formal mathematics. Yet
nearly every student finds the subject very difficult--- as difficult as
anything taught at universities. The root of the difficulty is that the
*subject matter* is extremely difficult. Let's find out *why* .

It is easy to find out with high precision which movie is playing
tonight at the local cinema; you can look it up on the web or call the cinema
and ask. But consider by contrast how difficult it is to determine with
accuracy:

a. what will be the result of more than a hundred million Americans voting for
   president a month hence; the best attempt usually is a sample of 2000
   people, selected in some fashion or another that is far from random, weeks
   before the election, asked questions that are by no means the same as the
   actual voting act, and so on;

b. to assess, on the basis of the data on the prices of a single brand of
   liquor in 42 states, 16 of which have liquor distribution systems run by
   state government and 26 run privately, whether prices will be higher in
   a state newly admitted to the union if it chooses the private system; or

c. how men feel about women and vice versa.

The cleverest and wisest people have pondered
for thousands of years how to obtain answers to questions like these,
and made little progress. Dealing with uncertainty was completely
outside the scope of the ancient philosophers. It was not until two or
three hundred years ago that people began to make any progress at all on
these sorts of questions, and it was only about one century ago that we
began to have reasonably competent procedures---simply because the problems are
inherently difficult. So it is no wonder that the body of these methods is
difficult.

So: The bad news is that the subject is extremely difficult. The good
news is that you---and that means *you* ---can understand it with hard
thinking, even if you have no mathematical background beyond arithmetic
and you think that you have no mathematical capability. That's because
the difficulty lies in such matters as pin-pointing the right question,
but not in any difficulties of mathematical manipulation.

# Preface to the third edition {-}

One of the pleasures of writing a new edition of someone else's book is that we
get some freedom to say good things about the earlier editions.  We get to
praise a version of our own book.   We will do that, in the next section.  In
the rest of the preface, we will say what we have changed, and why, and say
a little about where this book sits in your learning and teaching about data
analysis and statistics.

## What Simon saw

The book in your hands, or on your screen, is the third edition of a book
originally called "Resampling: the new statistics", by Julian Lincoln Simon
[-@simon1992resampling]. You will see some history of the book in Simon's
original preface, that follows this one.  Please do read that preface; it is an
excellent overview of what Simon was trying to do, and why.  What Simon could
not know, when he wrote that preface, was that the method he had discovered
would become the foundation of a revolutionary change in the teaching of data
analysis, that we now call "data science".

Simon published the first edition in 1992, but the ideas behind the book
started much earlier, when he noticed a major problem that is familiar to
almost every teacher of research methods - his students had a very shallow
understanding of statistics.  The typical response to this typical insight is
the "cookbook" method.  We try to minimize the damage by teaching recipes for
common situations. We apply warning labels to the recipes, in the hope
that our students will later do the right tests, even if they have little
understanding of what those tests mean.  Of course, this is a miserable way to
learn, and a miserable way to teach.  Our better students see that we are not
teaching for understanding, but rehearsal, and they suffer the most.  As you
will soon see, this book is for the teacher as well as the student.  It may be
no comfort, but we teachers also suffer when we have to teach this way.

Because this is such a common problem, many people have asked why statistics is
hard to teach, and hard to understand, and they have come to the same insight
as Simon; our standard statistics use a lot of mathematics, and this
mathematics is far beyond the level that we can reasonably teach to most of our
students [@cobb2007introductory].  As Wallis and Roberts
[-@wallis1957statistics] point out in an early textbook, the large majority of our
students are not fluent in mathematics, and teaching statistics by way of
mathematics is like teaching rhetoric in a foreign language.

Simon went two steps further than this, although, as you will see, those two
steps can also be one giant leap.  If he made two steps, the first was to see
that mathematics was not the only thing that made statistics difficult. He
realized, with great clarity, that statistical inference --- drawing
conclusions from noisy data --- involves a lot of hard, clear thinking about
the data, and the process that made the data.  This hard thinking remains, even
if you can strip out the mathematics (you can!).   He writes eloquently about
this in the introduction of this book, in a section "Why is statistics such
a difficult subject".   Because statistics is inherently difficult, it is all
the more important to strip away the extra difficultly that comes from teaching
through mathematics.  This second, inherent difficulty of statistics is much
more compelling than the first, incidental and unnecessary difficulty of
understanding the mathematics, because the inherent difficulty is just that of
thinking clearly about the problem, and designing a solution.  It is the
difficultly of thinking logically about data, and noise.

Simon's second step, was to see what he needed to do to bypass the mathematics,
and go directly to the inherent, interesting problem.  His deep insight was
this (from the original preface): "Beneath the logic of a statistical inference
there necessarily lies a physical process".  He saw, remarkably clearly, that
drawing conclusions from noisy data means *building* a *model* of the noisy
world, and seeing how that model behaves. That model can be physical, where we
generate noise with physical devices like dice and spinners and coin-tosses.
In fact, Simon used and taught exactly these kinds of devices in his first
experiments in teaching these methods [@simon1969basic].  He very quickly
realized that it was much more efficient to build these models with simple
computer code, and the result was the first and second editions of this book,
with their associated software, the *Resampling Stats* language. That language
had many good qualities, but, as you will see, technology and practice has come
far since 1997, and we can now replace this specialized language with much more
powerful and general languages, such as `r BL` and `r other_lang`, that are now
in very wide use in real-life data analysis.

## Resampling and data science

Simon's book, written in 1992, has found itself in the center of the modern
movement of *data science*.  We discuss the meaning of data science below, for
for now, let us say it is some fusion of modern statistics and computing.

In the section above, we described Simon's path in discovering physical models as a way of teaching and explaining statistical tests.  This led him very quickly to realize the power of simple code to express these physical models, and therefore, to build and explain statistical tests.

Other teachers of statistics have come to the same conclusion, and for similar
reasons.  Cobb [-@cobb2007introductory] argued strongly that there was too much
mathematics in statistics teaching.  In the age before ubiquitous computing, we
needed mathematics to simplify calculations that we could not practically do by
hand.  Now we have great computing power in our phones and laptops, we do not
have this constraint, and we can resampling methods to solve the same problems.
As Simon showed, these are much easier to describe and understand.  A later
discussion paper and responses made similar points [@cobb2015mere,
@horton2015mere_responses].

Meanwhile, the wider world of data analysis has been coming to the same
conclusion, but from the opposite direction.  Simon saw the power of resampling
for explanation, and then that code was the right way to express these
explanations.  Modern data science discovered first that code was essential for
data analysis, and then that code made it much easier to explain statistics.

The current use of the phrase "data science" comes from the technology
industry.  From around 2007, companies such as LinkedIn and Facebook began to
notice that there was a new type of data analyst that were much more effective
than their predecessors.  They came to call these data analysts "data
scientists", because they had learned how to deal with large difficult data
while working in scientific fields such as ecology, biology, or astrophysics.
They had done this by learning to use code:

> Data scientists’ most basic, universal skill is the ability to write code --
> @davenport2012data

Further reflection [@donoho201550] suggested that something deep was going on
--- that *data science* was the expression of a radical change in the way we
analyze data, in academia, and in industry.  At the center of this change ---
was code.  Code is language that allows us to tell the computer what it should
do with data; it is the native language of data analysis.

This insight transforms the way with think of code.  In the past, we have
thought of code as a separate, specialized skill, that some of us learn.  We
take coding courses --- we "learn to code".   If code is the fundamental
language for analyzing data, then we need code to express what data analysis
does, and explain how it works.  Here we "code to learn".  Code is not an aim
in itself, but a language we can use to express the simple ideas behind data
analysis and statistics.

Thus the data science movement came around from code as the foundation for data
analysis, to using code to explain statistics.  They end at the same place as
this book, from the other side of the problem.

## What we changed

This diversion, through data science, leads us to the changes that we have made
for the new edition.  The previous edition of this book is still excellent, and
you can read it free, online, at <http://www.resample.com/intro-text-online>.
It continues to be ahead of its time, and ahead of our time.  Its one major
drawback is that Simon bases much of the book around code written in a special
language that he developed with Dan Weidenfeld, called *Resampling Stats*.
Resampling Stats is well designed for expressing the steps in simulating worlds
that include elements of randomness, and it was a useful contribution at the
time it, and the book, were written.  Since then, and particularly in the last
decade, there have been many improvements in much more powerful and general
languages, such as `r BL` and `r other_lang`.  These languages are particularly
suitable for beginners in data analysis, and they come with a huge range of
tools and libraries for a very wide range of tasks in data analysis, including
the kinds of models and simulations you will see in this book.  We have
therefore updated the book to use `r BL`, instead of *Resampling Stats*.  If
you already know `r BL` or a similar language, such as `r other_lang`, you will
have a big head start in reading this book, but even if you do not, we have
written the book so it will be possible to pick up the `r BL` code that you
need to understand and build the kind of models that Simon uses.  The advantage
to us, your authors, is that we can use the very powerful tools associated with
`r BL` to make it easier to run and explain the code.  The advantage to you,
our readers, is that you can also learn these tools, and the `r BL` language,
and continue to use these tools, and this language for the rest of your career
in data analysis.

<!---
* The true novelty of resampling as teaching method
* Statistics without the agonizing pain
* Simon's insight
* The rise of resampling in data science
* Programming and statistics
-->

The second major change that we have made, is that we have added some content
to the book that Simon specifically left out.   Simon knew that his approach
was radical for its time, and wisely designed his book as a commentary,
correction, and addition to traditional courses in statistics.  He assumes some
familiarity with the older world of normal distributions, t-tests, Chi-squared
tests, analysis of variance, and correlation.  In the time that has passed
since he wrote the book, for the reasons we discuss above, his tools and
explanation have reached the mainstream.  It now perfectly possible to teach an
introductory statistics course without referring to the older statistical
methods.  This means that Simon's book can now serve on its own as an
introduction to statistics --- but, used this way, at the time we write, this
will leave our readers with some gaps to fill.  They should have a full, deep
understanding of the method of comparing measures from two groups, using
resampling methods, but they still be likely to come across other teachers and
researchers using more traditional methods such as t-tests.  To bridge this
gap, we have added material to many chapters that explain how the resampling
methods relate to the traditional methods, such as t-tests.  Luckily, we find
these explanations add deeper understanding to the traditional methods.
Teaching resampling is the best way to teach t-tests, and other traditional
methods.

Lastly, we have extended Simon's explanation Bayesian probability and
inference.   This is partly Bayesian methods have become so important in
statistical inference, and partly because Simon's approach has such obvious
application in explaining how and why Bayesian methods work.

## Who should read this book, and when

As you have seen in the previous sections, this book uses a radical approach to
explaining *statistical inference* --- the science of drawing conclusions from
noisy data.  This approach is quickly becoming the standard in teaching of data
science, partly because it is so much easier to explain, and partly because of
the increasing role of code in data analysis, as part of data science.

This book teaches the basics of using the `r BL` language, basic probability,
statistical inference through simulation and resampling, confidence intervals,
and basic Bayesian reasoning, all through the use of model building in simple
code.

Statistical inference is an important part of research methods for many
subjects; so much so, that research methods courses may even be called
"statistics" courses, or include "statistics" components.  This book covers the
basic ideas behind statistical inference, and how you can apply these ideas to
drawing practical statistical conclusions.  We recommend it to you as an
introduction to statistics.  If you are a teacher, we suggest you consider this
book as a primary text for first statistics courses.  We hope you will find,
like us, that this method of explaining through building is much more
productive and satisfying than the traditional method of trying to convey some
"intuitive" understanding of fairly complicated mathematics.  As we describe
above, we have added sections to many parts of the book to explain the
relationship of these resampling techniques to traditional methods.  Even if
you do need to teach your students t-tests, and analysis of variance, we hope
you will agree, that this way of explaining is much more compelling than our
traditional courses.

Simon wrote this book for students and teachers who were interested to discover
a radical new method of explanation in statistics and probability.  The book
will still work well for that purpose.  If you have done a statistics course,
but you kept feeling that you did not really understand it, or there was
something wrong, that you could not put your finger on, please, read this book.
There is a good chance that this book will give you deeper understanding, and
reveal the logic behind the often arcane formulations of traditional
statistics.

Our book is only part of a data science course.  There are several important
aspects to data science. A data science course needs all the elements we list
above, but it should also cover the process of reading, cleaning, and
reorganizing data using `r BL`, or another language, such as `r other_lang`. It
may also go into more detail about the experimental design, and cover
prediction techniques, such as classification with machine learning, and data
exploration with plots, tables, and summary measures.  We do not cover those
here.

## Welcome to resampling

We hope you will agree that the Simon's insights for understanding and
explaining are --- really extraordinary.  Our best educators are only slowly
catching up with his insights.  If you are like us, your humble authors of this
edition, you will find that Simon has succeeded in explaining what statistics
is, and *exactly* how it works, to anyone with the patience to work through the
examples, and think hard about the problems.  If you have that patience, the
rewards are great.  Not only will you understand statistics down to the
foundations of its biggest ideas, but you will have the tools to think of your
own tests, for your own, new problems, and build those tests yourself.


Matthew Brett

Stéfan van der Walt

Ian Nimmo-Smith

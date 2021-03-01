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
    ed2_fname: 05-Chap-1
---

# The Resampling method {#resampling-method}

This chapter is a brief introduction to the resampling method of solving
problems in probability and statistics. A simple illustrative problem is
stated, and then the step-by-step solution with resampling is shown,
using both by-hand methods and a computer program. The older conventional
formulaic approach to such a problem is then discussed. The conventional
analytic method requires that you understand complex formulas, and too often
one selects the wrong formula. In contrast, resampling requires that you first
understand the physical problem fully. Then you simulate a statistical model of
the physical problem with techniques that are intuitively obvious, and you
estimate the probability with repeated random sampling.

## The resampling approach in action

Recall the problem from section \@ref(what-problems) in which the contractor
owns 20 ambulances. The chance that any one ambulance will be unfit for
service on any given day is about 1 in 10, based on past experience. You want
to know the probability that on a particular day---tomorrow--- *three or more*
ambulances will be out of action. The resampling approach produces the
estimate as follows.

### Randomness from physical methods

We collect 10 coins, and mark one of them with a pen or pencil or tape
as being the coin that represents "out-of-order;" the other nine coins
stand for "in operation." This set of 10 coins is a "model" of a
situation where there is a one-in-ten chance---a probability of .10 (10
percent)---of *one* particular ambulance being out-of-order on a given day.
Next, we put the coins into a little jar or bucket, draw out one coin, and
mark down whether or not that coin is the coin marked "out-of-order."
That drawing of the single coin from the bucket represents the chance that
any one given ambulance among our 20 ambulances (perhaps the one with the
lowest license-plate number) will be out-of-order tomorrow.

Then we put the drawn coin back in the bucket, shake all the coins, and
again draw out a coin. We mark down whether that second-drawing coin is
or is not the "out-of-order" coin, and that outcome stands for a second
ambulance in the fleet. We do this *20* times to represent our 20
ambulances, replacing the coin after each drawing, of course. Those 20 drawings
represent one day.

At the end of the 20 draws we count how many out-of-orders we have got for that
"day," checking whether there are *three or more* out-of-orders. If there are
three or more, we write down in another column "yes"; if not, we write "no."
The work we have done up to now represents one experimental trial of the model
for a single day.

Then we repeat perhaps 50 or 100 times the entire experiment described
above. Each of those 50 or 100 experimental trials represents a single
day. When we have collected evidence for 50 or 100 experimental days, we
determine the proportion of the experimental days on which three or more
ambulances are out of order. That proportion is an estimate of the
probability that three or more ambulances will be out of order on a given
day---the answer we seek. This procedure is an example of Monte Carlo
simulation, which is the heart of the resampling method of statistical
estimation.

A more direct way to answer this question would be to examine the firm's
actual records for the past 100 days or 500 days to determine how many
days had three or more ambulances out of order. But the resampling procedure
described above gives us an estimate even if we do not have such
long-term information. This is realistic; it is frequently the case in
the workaday world that we must make estimates on the basis of
insufficient history about an event.

A quicker resampling method than the coins could be obtained with 20 ten-sided
dice or spinners. Each one of the dice, marked with one of its ten sides as
"out-of-order," would indicate the chance of a single ambulance being out of
order on a given day. A single pass with the 20 dice or spinners allows us to
count whether three or more ambulances turn up out of order. So in a single
throw of the 20 dice we can get an experimental trial that represents a single
day. And in a hundred quick throws of the 20 dice---which probably takes less
than 5 minutes---we can get a fast and reasonably-accurate answer to our
question. But getting hold of ten-sided dice might be a nuisance.

## Randomness from your computer

Computers make it easy to generate random numbers for resampling.  Random
numbers are numbers were it is effectively impossible to predict which number
is coming next.  For example, let's say I ask for a random number between 1 and
10 inclusive.  We accept that number is random if I have no way of doing better
than chance in predicting what that number is going to be.  We will go into
more detail about what we mean by *random* and *chance* later in the book.

<!--
Press Your Luck
The Michael Larsen Incident

https://web.archive.org/web/20170712041017/http://www.rotten.com/library/conspiracy/press-your-luck/
-->

We can use random numbers from the computer to simulate our problem.  For
example, we can ask the computer to make us a random number between 1 and 10
(inclusive) to represent one ambulance. If we say that the digit 0 represents
"out-of-order" and the digits 2 through 10 represent "in operation," then any
one random digit gives us a trial observation for a single ambulance.  To get
an experimental trial for a single day we look at 20 digits and count the
number of ones. If the number of ones is three or more, then we write "yes."
We then look at one hundred or two hundred sets of 20 digits and count the
proportion of sets whose 20 digits show three or more ambulances being
"out-of-order." Once again, that proportion estimates the probability that
three or more ambulances will be out-of-order on any given day.

Soon we will do all these steps with some Python code, but for now,
please take in on faith that we have made 20 random numbers, each from 1
through 10, and we have done that 25 times, to simulate 25 days of 20
ambulances. We could arrange those numbers in a table like table
\@ref(tab:veh-numbers):


Table: (\#tab:veh-numbers)25 simulations of 20 ambulances

|   | T1| T2| T3| T4| T5| T6| T7| T8| T9| T10| T11| T12| T13| T14| T15| T16| T17| T18| T19| T20|
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1  |  7|  5|  6|  4|  6|  9|  5|  5|  8|   2|   7|   5|   5|   2|   6|   4|   2|   3|   9|   6|
|2  |  7|  5|  6|  9|  6| 10|  5|  2|  1|   4|   8|   6|   1|   6|   2|   3|   1|   9|   2|   5|
|3  |  8|  1|  3| 10|  3|  2|  7| 10|  3|   6|   4|  10|   1|   7|   6|   6|   3|   9|   2|   8|
|4  |  1|  1|  7|  6|  9| 10|  2|  6|  7|  10|   6|   5|   7|   3|   1|   5|   1|   6|   1|   1|
|5  |  2|  5|  7|  1|  4|  7|  7|  8|  2|   8|   9|   3|   9|   6|   9|   5|   3|   2|   7|   4|
|6  |  4|  2|  9|  2|  3|  3|  1| 10|  7|   5|   4|   1|   3|   7|   1|   6|   7|  10|   8|   6|
|7  |  1|  4|  2|  6|  5| 10| 10|  3|  4|   6|   2|   9|   5|   3|   2|   5|  10|   4|   3|   8|
|8  |  4|  9|  1|  7|  4|  8| 10|  8|  7|   9|   9|  10|   9|   3|   9|   3|   1|   7|   5|   9|
|9  |  4|  6|  8|  7|  3|  8|  3|  8|  8|   2|   7|   2|  10|   1|   5|  10|   2|   9|   9|   1|
|10 |  7|  4|  1|  9|  9| 10|  4|  6|  2|  10|   2|  10|  10|   2|   5|   3|   4|   2|   5|   5|
|11 |  6|  3|  1|  8|  8|  6|  8|  3|  2|   8|   7|  10|   5|   8|  10|   5|   3|   4|   1|   9|
|12 |  2|  7|  3| 10|  8|  3|  1|  1|  9|  10|  10|   5|   2|  10|   8|   2|   4|   5|   7|   4|
|13 |  4|  4|  3|  5|  6|  5|  3|  4|  9|   5|   6|   7|   7|  10|   6|   5|   8|   2|  10|   8|
|14 |  2|  6|  6|  1|  5|  5|  6|  9|  1|   1|   9|   4|   2|   8|   7|   7|  10|   7|   6|   5|
|15 | 10|  9|  6|  8|  3| 10| 10|  2| 10|   7|   7|   4|   7|  10|   2|   9|  10|   6|  10|   2|
|16 |  2|  9|  1|  1|  1|  1|  9|  2|  3|   9|   5|   8|   6|   1|   4|  10|   3|   2|   7|  10|
|17 | 10|  2|  5|  6| 10|  7|  6|  3|  4|   3|   6|   4|  10|   7|   9|   9|   1|   2|   3|  10|
|18 |  1| 10|  5|  5|  7|  7|  8|  5|  6|   2|   5|   5|   1|   5|   9|  10|   4|   6|  10|   3|
|19 |  3|  1|  8|  5|  9|  4|  3|  9| 10|   9|   1|   8|   6|  10|   6|   8|   3|   5|   9|   6|
|20 | 10|  1|  9|  4|  6|  6|  1|  3|  1|   9|   1|  10|   2|   8|  10|  10|   1|   4|   9|   1|
|21 |  2|  3|  2|  1|  8|  9|  7|  5|  2|   7|  10|   7|  10|  10|   2|   4|  10|   2|   8|   8|
|22 |  4|  8|  9|  2|  4|  5|  8|  5|  8|   4|   6|   4|   8|   6|   6|   9|   7|   7|   2|   4|
|23 |  4|  7|  9|  4|  5|  7| 10|  2|  5|   2|   8|   5|   4|   3|   4|   1|   7|   1|   5|   6|
|24 | 10|  7|  3|  8|  7|  2|  1|  1|  9|  10|   3|  10|   4|   8|   8|   5|   7|   1|   2|   9|
|25 |  8|  3|  2|  4|  5|  3|  1|  1|  3|   9|   4|   3|   1|   1|   8|   4|   6|  10|   2|   1|

To get the answer for each day, we count the number of zeros in each row.  The
counts go in the final column called "#0" (for "number of zeros").


Table: (\#tab:veh-numbers-counts)25 simulations of 20 ambulances, with counts

|   | T1| T2| T3| T4| T5| T6| T7| T8| T9| T10| T11| T12| T13| T14| T15| T16| T17| T18| T19| T20| #0|
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|--:|
|1  |  7|  5|  6|  4|  6|  9|  5|  5|  8|   2|   7|   5|   5|   2|   6|   4|   2|   3|   9|   6|  0|
|2  |  7|  5|  6|  9|  6| 10|  5|  2|  1|   4|   8|   6|   1|   6|   2|   3|   1|   9|   2|   5|  3|
|3  |  8|  1|  3| 10|  3|  2|  7| 10|  3|   6|   4|  10|   1|   7|   6|   6|   3|   9|   2|   8|  2|
|4  |  1|  1|  7|  6|  9| 10|  2|  6|  7|  10|   6|   5|   7|   3|   1|   5|   1|   6|   1|   1|  6|
|5  |  2|  5|  7|  1|  4|  7|  7|  8|  2|   8|   9|   3|   9|   6|   9|   5|   3|   2|   7|   4|  1|
|6  |  4|  2|  9|  2|  3|  3|  1| 10|  7|   5|   4|   1|   3|   7|   1|   6|   7|  10|   8|   6|  3|
|7  |  1|  4|  2|  6|  5| 10| 10|  3|  4|   6|   2|   9|   5|   3|   2|   5|  10|   4|   3|   8|  1|
|8  |  4|  9|  1|  7|  4|  8| 10|  8|  7|   9|   9|  10|   9|   3|   9|   3|   1|   7|   5|   9|  2|
|9  |  4|  6|  8|  7|  3|  8|  3|  8|  8|   2|   7|   2|  10|   1|   5|  10|   2|   9|   9|   1|  2|
|10 |  7|  4|  1|  9|  9| 10|  4|  6|  2|  10|   2|  10|  10|   2|   5|   3|   4|   2|   5|   5|  1|
|11 |  6|  3|  1|  8|  8|  6|  8|  3|  2|   8|   7|  10|   5|   8|  10|   5|   3|   4|   1|   9|  2|
|12 |  2|  7|  3| 10|  8|  3|  1|  1|  9|  10|  10|   5|   2|  10|   8|   2|   4|   5|   7|   4|  2|
|13 |  4|  4|  3|  5|  6|  5|  3|  4|  9|   5|   6|   7|   7|  10|   6|   5|   8|   2|  10|   8|  0|
|14 |  2|  6|  6|  1|  5|  5|  6|  9|  1|   1|   9|   4|   2|   8|   7|   7|  10|   7|   6|   5|  3|
|15 | 10|  9|  6|  8|  3| 10| 10|  2| 10|   7|   7|   4|   7|  10|   2|   9|  10|   6|  10|   2|  0|
|16 |  2|  9|  1|  1|  1|  1|  9|  2|  3|   9|   5|   8|   6|   1|   4|  10|   3|   2|   7|  10|  5|
|17 | 10|  2|  5|  6| 10|  7|  6|  3|  4|   3|   6|   4|  10|   7|   9|   9|   1|   2|   3|  10|  1|
|18 |  1| 10|  5|  5|  7|  7|  8|  5|  6|   2|   5|   5|   1|   5|   9|  10|   4|   6|  10|   3|  2|
|19 |  3|  1|  8|  5|  9|  4|  3|  9| 10|   9|   1|   8|   6|  10|   6|   8|   3|   5|   9|   6|  2|
|20 | 10|  1|  9|  4|  6|  6|  1|  3|  1|   9|   1|  10|   2|   8|  10|  10|   1|   4|   9|   1|  6|
|21 |  2|  3|  2|  1|  8|  9|  7|  5|  2|   7|  10|   7|  10|  10|   2|   4|  10|   2|   8|   8|  1|
|22 |  4|  8|  9|  2|  4|  5|  8|  5|  8|   4|   6|   4|   8|   6|   6|   9|   7|   7|   2|   4|  0|
|23 |  4|  7|  9|  4|  5|  7| 10|  2|  5|   2|   8|   5|   4|   3|   4|   1|   7|   1|   5|   6|  2|
|24 | 10|  7|  3|  8|  7|  2|  1|  1|  9|  10|   3|  10|   4|   8|   8|   5|   7|   1|   2|   9|  3|
|25 |  8|  3|  2|  4|  5|  3|  1|  1|  3|   9|   4|   3|   1|   1|   8|   4|   6|  10|   2|   1|  5|

Each value in the last column of \@ref(tab:veh-numbers-counts) is the count of
zeros in that row, and therefore, the result from our simulation of one day.

We can estimate how often three or more ambulances would break down by looking
for values of three or greater in the last column.  We find there are `r
sum(df_counts['#0'] >= 3)` rows with three or more in the last column. Finally
we divide this number of rows by the number of trials (25) to get an
estimate of the *proportion* of days with three or more breakdowns. The result
is 0.32.

## Building the problem using Python

Here we rush ahead to show you how to do this simulation in Python.

In the text that follows we go through the Python code for the
simulation.  Please don't expect to understand this code right away.  The rest
of this book goes into more detail about how Python code works, and how
you can use Python to build your own simulations.  Here we want to show
you what this code looks like, to give you an idea of where we are headed.

For each line of the code below, we give a detailed explanation, but you can
also *run* the code yourself, to see it in action.  The link below allows you
to open this code as a *notebook*, and run it.  But, you may want to read the
next chapter [About the technology], to learn more about how to run this
notebook.  For now, we encourage you read the text here carefully, without
using the technology to run the code.  The text explains what the code means.
Later, after you have read more about the technology, you might consider coming
back to the links here to *run* the code.

<div class="rmdcomment">

<p>Start of <code>ambulances</code> notebook.</p>

<p>
<div class="nb-links">
<a class="notebook-link" href=ambulances.ipynb>Download notebook</a>
<a class="interact-button" href="https://mybinder.org/v2/gh/resampling-stats/resampling-with/gh-pages?filepath=python-book/ambulances.ipynb">Interact</a>
</p>
</div>
</div>


The first thing to say about the code below is there are many lines in these
bits of code that don't do anything.  These are the lines beginning with the
`#` character (read `#` as "hash").  Lines beginning with `#` are called
*comments*.  When Python sees the `#` at the start of the line, it
realizes that it should ignore everything else on that line, and skips on the
next line. Here's an example of a comment in Python:


```python
# Python will completely ignore this text.
```



Because Python ignores lines beginning with `#`, the text comments is
just for us, the humans that are reading the code.  We often use comments in code to explain what the other parts of the code are doing, to make the rest of the code easier for humans to read and understand.

Our next task is to use Python to simulate a single day of ambulances.
We will represent each ambulance by a random number from 1 through 10.  20 of
these numbers represents a simulation of all 20 ambulances available to the
contractor.  We will call a simulation of 20 ambulances --- one *trial*.


Before we begin our first trial, we need to load some helpful routines from the
Numpy library.  Numpy is a Python library that has many important functions for
creating and working with data.  We will use routines from Numpy in almost all
our examples.


```python
# Get the Numpy library, and call it "np" for short.
import numpy as np
```


The core of the program to simulate one trial of ambulances problem above
begins with this command to the computer:


```python
# Use Numpy ("np") to generate 20 random integers from 1 up to, but *not
# including* 11.  Therefore, this generates 20 numbers from 1 through 10
# inclusive.
# Store the 20 numbers as an "array" with the name "a"
a = np.random.randint(1, 11, size=20)
```



This command orders the computer to randomly generate 20 numbers from `1`
through `10`. Inasmuch as each ambulance has a 1 in 10 chance of being
defective, we decide arbitrarily that a `1` stands for a defective ambulance,
and the other nine numbers (from `2` to `10`) stand for a non-defective
ambulance. The command orders the computer to store the results of the random
drawing in a location in the computer's memory to which we give a name such as
"a" or "ambulances" or "aardvark" --- the name is up to us.

The next key element in the core of the program is:


```python
# Count the number of ones among the random numbers, using the Numpy ("np")
# "count_nonzero" function.
b = np.count_nonzero(a == 1)
```



This is a *counting* operation. The command orders the computer to *count* the
number of `1`s among the twenty numbers that are in location `a` following the
random drawing carried out by the `randint` operation.
The result of the `count_nonzero` operation will be
somewhere between 0 and 20, the number of ambulances that might be out-of-order
on a given day. The result is then placed in another location in the computer's
memory that we label `b`.

Now let us place the  `randint`and `r
py_or_r('count_nonzero', 'sum')` commands within the entire program that we use
to solve this problem, which is:


```python
# Make an array of 1000 numbers to store our 1000 counts.
# These all start off as 0, but we fill them in below as we do 1000 trials.
z = np.zeros(1000)
# Repeat one trial of the simulation 1000 times.
for i in np.arange(1000):
    # Everything in the indented block is part of one trial.
    # We run everything in the indented block for each trial.
    # Therefore, Python runs all these commands 1000 times.

    # Generate 20 numbers, each between 1 through 10 and put them in array a.
    # Each number will represent an ambulance, and we let 1 represent a
    # defective ambulance.
    a = np.random.randint(1, 11, size=20)
    # Count the number of defective ambulances, and put the result in "b".
    b = np.count_nonzero(a == 1)
    # Keep track of each trial's results in "counts".
    z[i] = b
    # End this trial, then go back and repeat the process until all 1000 trials
    # are complete, then proceed.

# This part runs after all 1000 trials have finished.

# Determine how many trials resulted in more than 3 ambulances out of order.
k = np.count_nonzero(z > 3)

# Convert to a proportion.
kk = k / 1000

# Print the result.
print(kk)
#> 0.124
```



The `z[i] = b` statement that follows the `r
py_or_r('np.count_nonzero', 'sum')` *counting* operation simply keeps track of
the results of each trial, placing the number of defective ambulances that
occur in each trial in a location that we usually call `z`. This is done in
each of the 1000 trials that we make, and the result eventually is an "array"
with 1000 numbers in it.

In order to make 1000 repetitions of our experiment --- we could have decided
to make ten thousand or some other number of repetitions --- we surround each trial with the `for` *loop*, that has the effect of repeating the operations for one trial 1000 times.  We identify the operations to repeat with the

indentation level.  All the indented statements are statements we repeat for
each time through the `for` loop.

<!---
opening --- `{` --- and closing --- `}` --- curly brackets.
-->

Since our aim is to count the number of days in which more than 3 (4 or
more) defective ambulances occur, we use another *counting* command
(`count_nonzero`) at the end of the 1000 trials.  This
counting command *counts* how many times more than 3 defects occurred in the
1000 days recorded in our `z` array, and we place the result in still another
location `k`. This gives us the total number of days where 4 or more defective
ambulances are seen to occur. Then we divide the number in `k` by 1000, the
number of trials. Thus we obtain an estimate of the chance, expressed as a
probability between 0 and 1, that 4 or more ambulances will be defective on a
given day. And we store that result in a location that we decide to call `kk`,
so that it will be there when the computer receives the next command to `print`
that result on the screen.

Please don't worry about the details of how each of these commands works --- we
will cover those details gradually, over the next few chapters.  But, we hope
that you can see in principle, how each of the operations that the computer
carries out are analogous to the operations that you yourself executed when you
solved this problem using a ten-sided spinner or a random-number table. This is
exactly the procedure that we will use to solve every problem in probability
and statistics that we must deal with. Either we will use a device such as
coins or a random number table as an analogy for the physical process we are
interested in (ambulances becoming defective, in this case), or we will
simulate the analogy on the computer using some Python code like the code
above.

The Python STATS program called "ambulances" may not seem simple to you at
first glance. But please believe us when we say that it is vastly simpler than
the older conventional approach to such problems that has routinely been taught
to students for decades.


## How resampling differs from the conventional approach

In the standard approach the student learns to choose and solve a
formula. Doing the algebra and arithmetic is quick and easy. The
difficulty is in choosing the correct formula. Unless you are a
professional mathematician, it may take you quite a while to arrive at
the correct formula---considerable hard thinking, and perhaps some
digging in textbooks. More important than the labor, however, is that
you may come up with the wrong formula, and hence obtain the wrong
answer. Most students who have had a standard course in probability and
statistics are quick to tell you that it is not easy to find the correct
formula, even immediately after finishing a course (or several courses)
on the subject. After leaving school, it is harder still to choose the
right formula. Even many people who have taught statistics at the
university level (including this writer) must look at a book to get the
correct formula for a problem as simple as the ambulances, and then we are
not always sure of the right answer. This is the grave disadvantage of
the standard approach.

In the past few decades, resampling and other Monte Carlo simulation
methods have come to be used extensively in scientific research. But in
contrast to the material in this book, simulation has mostly been used
in situations so complex that mathematical methods have not yet been
developed to handle them. Here are examples of such situations:

<!---
Better examples.  These are out of date.
-->

1.  For a spaceship that will travel to Mars, calculating the correct flight
    route involves a great many variables, too many to solve with formulas.
    Hence, the Monte Carlo simulation method is used.

2.  The Navy might want to know how long the average ship will have to
    wait for dock facilities. The time of completion varies from ship to
    ship, and the number of ships waiting in line for dock work varies
    over time. This problem can be handled quite easily with the
    experimental simulation method, but formal mathematical analysis
    would be difficult or impossible.

3.  What are the best tactics in baseball? Should one bunt? Should one
    put the best hitter up first, or later? By trying out various
    tactics with dice or random numbers, Earnshaw Cook (in his book
    *Percentage Baseball* ), found that it is best never to bunt, and
    the highest-average hitter should be put up first, in contrast to
    usual practice. Finding this answer would have been much more difficult
    with the analytic method.

4.  Which search pattern will yield the best results for a ship
    searching for a school of fish? Trying out "models" of various
    search patterns with simulation can provide a fast answer.

5.  What strategy in the game of Monopoly will be most likely to win?
    The simulation method systematically plays many games (with a
    computer) testing various strategies to find the best one.

But those five examples are all complex problems. This book and its
earlier editions break new ground by using this method for *simple
rather than complex problems* , especially in statistics rather than
pure probability, and in teaching *beginning rather than advanced*
students to solve problems this way. (Here it is necessary to emphasize
that the resampling method is used to *solve the problems themselves
rather than as a demonstration device to teach the notions found in the
standard conventional approach* . Simulation has been used in elementary
courses in the past, but only to demonstrate the operation of the
analytical mathematical ideas. That is very different than using the
resampling approach to solve statistics problems themselves, as is done
here.)

Once we get rid of the formulas and tables, we can see that statistics
is a matter of *clear thinking, not fancy mathematics* . Then we can get
down to the business of learning how to do that clear statistical
thinking, and putting it to work for you. *The study of probability* is
purely mathematics (though not necessarily formulas) and technique. But
*statistics has to do with meaning* . For example, what is the meaning
of data showing an association just discovered between a type of
behavior and a disease? Of differences in the pay of men and women in
your firm? Issues of causation, acceptability of control, design of
experiments cannot be reduced to technique. This is "philosophy" in the
fullest sense. Probability and statistics calculations are just one
input. Resampling simulation enables us to get past issues of
mathematical technique and focus on the crucial statistical elements of
statistical problems.

If you intend to go on to advanced statistical work, the older standard
method can be learned alongside resampling methods. Your introduction to
the conventional method may thereby be made much more meaningful.


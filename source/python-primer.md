# Python Primer

We will now take a brief tour of the Python language. If you are
already familiar with programming, you may find the [SciPy lecture
notes](https://scipy-lectures.org/) more suitably paced.  You may
download and install Python from https://www.python.org/downloads/.

Python is an interpreted language.  This means that it reads code line
by line and executes each.  To see how this works, we run `python`
(search for "Python terminal" in your menu bar, or execute the
"python" command).

Inside of Python, you can type commands, like `print("Hello world!")` below.

```
$ python
Python 3.8.6 (default, Sep 30 2020, 04:00:38) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello world!")
Hello world!
>>> 
```

Type `exit()` the quit Python.

Usually, we do not use the Python terminal directly.  We ask it to
read code from a text file, or use interactive frontends such as
[Jupyter](https://jupyter.org/) or [IPython](https://ipython.org/).

Let's see how to load commands from a file.  Create a new file called
`hello.py` in a text editor (such as Spyder, VS Code, or PyCharm).
Inside of it, put the following:

```{python}
print("Hi!")
print("We can see that one plus one is", 1 + 1)
```

Now, run the program as follows from a terminal:

```
python hello.py
```

You should see:

```
Hi!
We can see that one plus one is 2
```

In the Jupyter notebook, you would get the same output by entering
this code into a cell and typing Ctrl-Enter.

For the purposes of this book, it does not matter which method you use
to run your Python code.  If unsure, use Spyder.

## Variables

Most computer languages have the notions of variables: named buckets used to
carry around values.  This is useful for attaching a name to a value:

```
my_birthday = "1 January 1980"
```

Here, the bucket "my_birthday" now contains a string, "1 January 1980".

When do we use variables?  Say you join your friends Jane and Joe for
dinner and split the bill ($60) three ways, after adding a 20%
tip. Joe forgot his wallet at home and, since you already owe him $10
from a previous dinner, you pay his portion.  How much does Joe owe
you?

The calculation, including tip, is:

```
(60 * 1.2) / 3 - 10
```

And the amount you have to pay in total:

```
(60 * 1.2) * 2 / 3
```

These expressions give us the correct amounts, but they are not very
descriptive.  We can describe the same calculations using variables:

```{python}
bill = 60
tip = 20 / 100
i_owe_joe = 10
people_at_dinner = 3

joe_owes_me = (bill * (1 + tip)) / people_at_dinner - i_owe_joe
my_bill = (bill * (1 + tip)) * 2 / 3
```

The variable names help us to understand what the quantities in
question mean, and also make it very easy to add different values in.
E.g., I could use the same program---but with different values for
`bill`, `tip`, etc.---the next week.

You see that the equal sign is used to assign a new value to a
variable (in other words, replace what is stored in the bucket).  A
variable can contain many different types of objects, such as numbers,
strings, lists, or dictionaries:

```
w = 5
x = "hello world"
y = [1, 2, 3]
z = {"once": "happens a single time"}
```

We'll discuss lists and dictionaries in more detail shortly.

An assignment replaces whatever is stored in the variable, but you can
use the variable itself along the way:

```
x = 3
x = x * x
```

The value of `x` is now 9.

## Displaying output

Above, you see some use of the `print` statement. Often, you want to
print variables as part of a sentence:

```{python}
print(f"Joe now owes me {joe_owes_me}")
```

Note the 'f' character before the string being printed---this tells us
it is a "formatted" string.  In such strings, variables surrounded by
`{` and `}` get replaced by their value.

You could also have written:

```{python}
print("Joe now owes me", joe_owes_me)
```

## Functions

Sometimes, it is convenient to group statements together. We do this
using functions.  Let's say you are part of a group of volunteers, and
need to send out tasks to three individuals.  You could do this:

```{python}
print("Hello, Jason!")
print("Your task for the weekend is to weed the lawn.")

print("Hello, Maria!")
print("Your task for the weekend is to prune the hedge.")

print("Hello, Tania!")
print("Your task for the weekend is to do the budget.")
```

It would be more convenient to group these into a single function:

```{python}
def send_reminder(name, task):
    print(f"Hello, {name}!")
    print(f"Your task for the weekend is to {task}.")

send_reminder("Jason", "weed the lawn")
send_reminder("Maria", "prune the hedge")
send_reminder("Tania", "do the budget")
```

Functions can send back their results too.  If we had a function that
multiplied a number by two, we could use it as follows:

```{python}
def double(x):
    return 2 * x

z = 1
y = double(z)
```

The value of `z`, after running the above, is 2.

## Other data structures

Python has two extremely powerful data structures: lists and
dictionaries.  Lists are collections of objects, and dictionaries are
mappings between a keyword and a value---very much like a dictionary
in real life!

Here are some lists:

```{python}
primes_under_30 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
simple_words = ["there", "is", "and", "the"]
mixed_bag = [1, "two", 3]
```

You access lists as follows:

```{python}
print(simple_words[2])
```

This returns the third element of `simple_words` (Python counts from
zero, so the first element is `simple_words[0]`).  You can also grab
more than one at a time:

```{python}
print(simple_words[2:5])
```

This returns elements from 2 up to (but not including) 5---so 2, 3, and 4.

A dictionary is written as follows:

```{python}
word_definitions = {"hello": "standard greeting", "there": "a place other than here"}
numbers_game = {1: "you win", 2: "you lose", 3: "it is a tie"}
```

And they are accessed with the key:

```{python}
print(word_definitions["hello"])
print(numbers_game[1])
```

## For-loops

The above worked well for a team of three, but what if you had twenty
team members?  For that, we need a loop.  Loops let us repeat
instructions many times over.

The for-loop is particularly useful.  You can think of it as a factory
robot: it runs along a track and, when it finds an object in front of
it, does something with that object.

Say, for example, we want to square all the integers between 1 and 10:

```{python}
factory_line = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in factory_line:
    print(number ** 2)
```

This takes each number in turn, squares it, and prints it out.  Note
the syntax here: every time we work with a new element, that element is
assigned to the variable `number`.

`factory_line` can be any list (in facy, any object in Python that
lets you step through it).  There is a particularly useful function
called "range(a, b)", which generates all numbers between a and b (but
excluding b itself).  For example:

```{python}
for i in range(5):
    print(i)
```

```{python}
for x in range(1, 6):
    print(x)
```

## if-clauses

Sometimes, we have to decide whether to execute a line or not.  If we
wanted to print out all the numbers between 1 and 100 divisible by
14, we would use the `if`-statement:

```
for i in range(1, 101):
    if i % 2 == 14:
        print(i)
```

We use the `%` operator above; it returns the remainder of a division.

## Built-in and external libraries

Python is often called a "batteries included" language because of the
useful utility functions that accompany it.  These functions live
inside the "[standard library](https://docs.python.org/3/library/)".
Let's compute the hypotenuse of a right-angled triangle:

```{python}
import math

a = 5
b = 10

print("Hypotenuse is", math.sqrt(a ** 2 + b ** 2))
```

To do this for multiple triangles, we could put it in a function:

```
import math

def hypot(a, b):
    return math.sqrt(a** 2 + b**2)

print(hypot(3, 4))
print(hypot(1, 3))
print(hypot(6, 2))
```

## Exercise: calculate the area of a circle

Write a function to calculate the area of a circle with given radius.
Calculate the area for circles of all integer radii between 10 and 50.

```{python}
import math

def circle_area(r):
    return math.pi * r**2

for r in range(10, 51):
    print(circle_area(r))
```

## Further reading

- [Python.org tutorial](https://docs.python.org/3/tutorial/)
- [SciPy lecture notes](https://scipy-lectures.org/)

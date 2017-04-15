"""
py.py - These are the notes that accompany my HackCWRU tutorial on Python. All
of the live demo code is here, along with most of the commentary. Hopefully
this should be enough to get you started with Python!

Table of Contents:
    1. Intro
    2. Math Operators
    3. Variables and data types
       a. Numbers
       b. Booleans
       c. Strings, string formatting.
       d. Lists, tuples, slicing
       e. Dicts
    4. Language Elements
       a. If statements, truthiness
       b. While loops
       c. For loops, iterators
       d. Functions, splats, kwargs, and more
       e. Classes: a brief intro
       f. List, set, and dict comprehensions.
       g. Exceptions, try, catch, finally, with
    5. Useful builtins
       a. Open files
       b. zip()
    6. Modules
    7. Resources - where to go next, where to find libraries, etc.
"""

### 1. INTRO

# This tutorial is meant to be interactive, so before anything else, you should
# start by installing Python. For Mac OS and Windows, this should be as simple
# as visiting the following site and using the download link:
#
# https://www.python.org
#
# Please be sure to pick Python 3 (at the time of writing, 3.6.1)! I will only
# be teaching Python 3 in this tutorial, so if you want Python 2... sorry.
#
# For Linux users, a Python interpreter is probably already installed on your
# computer. Try running the command `python -V`. If that gives you Python 3, you
# should be set! If it's Python 2, you'll want to try running the command
# `python3`, and if that doesn't exist, use your package manager to install the
# python3 package.


# While you download and install Python, I'll take this opportunity to talk
# about why you may want to learn it.
#
# 1. Python is quite good for "getting shit done." It is powerful enough that
#    don't need to write hundreds of lines of code to get something to work, and
#    it has enough "batteries included" to make common tasks easy.
#
# 2. Python has libraries for everything! You'll find quality code already
#    exists to help you do almost anything: make a web app, make a desktop app,
#    do efficient data analytics & machine learning, write and run Hadoop map
#    reduce jobs easily, use AWS, build your own Internet (seriously.), scrape
#    data from websites, or construct and send any type of Internet packet.
#
#    And those are just the things I know about off the top of my head!


# Now that you have Python installed, let's get started. You may be used to
# programming languages that require compiling before running (e.g. Java or C).
# Python is an interpreted language, so there's no compiling. In fact, you can
# run Python's interpreter interactively, so that you can type code and execute
# it by hitting enter.
#
# The easiest way to do this is to open up a terminal and run the command
# `python` (or maybe `python3` on some Linuxes). Windows users may prefer to run
# the program `IDLE` from their start menu.
#
# You should be greeted by a prompt like this:
#
# >>>
#
# By tradition, we'll start with the "Hello world" program:

print('Hello, world!')
# Hello, World!

### 2. MATH OPERATORS

# Pretty simple, right? Of course, you can do more than math. For instance, you
# can do simple math:

1 + 1
# 2

12 - 9
# 3

5 / 3
# 1.666666666666667

10 * 10 * 10
# 1000

# Hopefully this all feels intuitive. Note that division will take an integer
# number and return a number with decimals. If you just wanted integer division,
# you can use the // operator:

5 // 3
# 1

# Exponentiation is NOT done with the ^ operator, as you might expect. Instead,
# it is done with the ** operator:

5 ** 3
# 125

# Order of operations is like you'd expect, and you can force things with
# parentheses:

5 + 3 * 5
# 20

(5 + 3) * 5
# 40

### 3. VARIABLES
#### 3a. Numbers

# Of course, Python is more than just a glorified calculator. For instance, you
# can start by declaring a variable:

my_variable = 5

my_variable
# 5

my_variable + 1
# 6

# You can use a variable like you would have used a number in the math above.
# Note that the declaration of my_variable has no type! In a language like Java,
# you'd expect something more like this:
#
# int my_variable = 5;
#
# Or this:
#
# float my_variable = 5.0;
#
# But in Python, you don't need to say what type your variable is -- the
# interpreter will figure it out. If you want to see what type it is, there's a
# handy type() function just for you:

type(my_variable)
# <class 'int'>

# Another interesting difference here is that variables don't have to stay the
# same type. For instance, we could make my_variable a floating-point number
# (i.e. a decimal):

my_variable = 5.5

type(my_variable)
# <class 'float'>

#### 3b. Strings, string formatting
# Not all Python variables contain numbers. You can make my_variable become
# something completely different by making it into a string:

my_variable = 'Hello, World!'

type(my_variable)
# <class 'str'>

# Strings can hold any sequence of characters! This one is the exact same one
# that we printed earlier. We can do lots of stuff with strings... here are some
# silly examples:

my_variable.upper()
# 'HELLO, WORLD!'

my_variable.lower()
# 'hello, world!'

my_variable.swapcase()
# 'hELLO, wORLD!'

# This is your first example of calling a function on an 'object'. Pretty much
# everything in Python is an object, and you can call their functions by using
# the dot operator. Strings happen to have lots of useful methods, which you can
# see in the Python documentation:
#
# https://docs.python.org/3/library/stdtypes.html#string-methods

# One last thing that will prove useful: formatting. You can use the special
# string formatting operotor `%` to put variables into a string. It uses a
# syntax similar to printf, so if you're familiar with that, this'll be quite
# convenient:

'Hello, World, my name is %s' % ('Stephen')
# 'Hello, World, my name is Stephen'

'the %s is %d' % ('answer', 42)
# 'the answer is 42'

#### 3c. Booleans
# Finally, there's the ever so boring boolean type:

am_i_the_best = True
is_the_sky_green = False

# Strangely, True and False are capitalized. That's just something to get used
# to. Thankfully, the boolean operators are easy:

not is_the_sky_green
# True

am_i_the_best and is_the_sky_green
# False

am_i_the_best or is_the_sky_green
# True

# You can get booleans by comparing things, which is quite easy to do in Python.
# For numbers:

15 < 20
# True

5 >= 6
# False

3 == 3.0
# True

# For strings, the == operator compares the value of the string (unlike Java).
# So it's completely correct to compare strings like this:

'foobar' == 'foobar'
# True

#### 3d. Lists, tuples, slicing
# We're almost done with data types, I promise. But since we've seen the
# numbers, the strings, and the booleans, I think it's now time to try to put
# these together into "collections" of numbers, strings, and booleans! First,
# let's look at lists:

my_list = []

# That's a list! It's empty right now. We could have made it not empty:

my_list = [5]

# Now it's a list with one number inside of it. We can tell by using the
# built-in len() function to ask how long it is:

len(my_list)
# 1

# If we wanted to get the first item out of it, we would do this:

my_list[0]
# 5

# This is called "indexing", and as you may be able to tell, Python indexes are
# zero based (as they should be :P). You can assign to indexes as well.

my_list[0] = 6
my_list
# [6]

# You're allowed to use negative indexes in order to count from the end of the
# list:

my_list = [1, 2, 3, 4]
my_list[-1]
# 4
my_list[-1] = 5
my_list
# [1, 2, 3, 5]

# Interestingly, just like variables can be whatever type they want (and change
# whenever they'd like), lists don't have to have any particular type in them.
# For instance, my_list could have a number and a string:

my_list = [5, 'five']
my_list
# [5, 'five']

# If you wanted to add a boolean to my_list, you can use its append() function:

my_list.append(False)
my_list
# [5, 'five', False]

# You can insert things at a particular index. This will shift everything over:

my_list.insert(1, '5')
my_list
# [5, '5', 'five', False]

# If you wanted to delete an item from my_list, you have a couple ways of doing
# it. When you know the index, you can simply use the keyword `del`. For
# example, to delete 'five', you can do:

del my_list[2]
my_list
# [5, '5', False]

# If you know that something is in the list, you can use the remove() function
# to delete the first instance of it:

my_list.remove('5')
my_list
# [5, False]

# But be careful, if it's not in the list, you'll get an error!

my_list.remove('5')
# ERROR!

# You can check whether something is in a list very easily:

'5' in my_list
# False

5 in my_list
# True

# You can also add two lists, or multiply a list by a number. It makes pretty
# intuitive sense:

[1, 2] + [3, 4]
# [1, 2, 3, 4]

[1, 2, 3] * 3
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Finally, I present the most exciting part of Python lists: slicing! Indexing
# is cool, if you just want one item out of the list. But what if you want to
# get a "sub-list"?  Maybe the first five, or the last five, or every other
# item. You can accomplish all of that with slicing, a feature that looks very
# similar to indexing.

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
len(l)
# 10

# Basically, you say 'I want the items starting at index X and ending at (but
# not including) index Y'. You separate X and Y with a colon. For example, to
# get 2, 3, 4 from the above list:

l[2:5]
# [2, 3, 4]

# You can omit the first index to start from the beginning:

l[:5]
# [0, 1, 2, 3, 4]

# You can omit the second index to go up to the end:

l[8:]
# [8, 9]

# Omitting both just gives you back a copy of the original:

l[:]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# You can use negative indices to start N from the end:

l[-3:]
# [7, 8, 9]

# Or you can use negative indices to end N from the end:

l[:-1]
# [0, 1, 2, 3, 4, 5, 6, 7, 8]

# These slices are useful not only for extracting a sub-list from an original
# list, but also for assigning to it, or even deleting it!

del l[-2:]
l
# [0, 1, 2, 3, 4, 5, 6, 7]

l[:5] = ['a', 'b']
l
# ['a', 'b', 5, 6, 7]

# The last awesome feature of slices is that you can specify a "step" parameter
# after an optional second colon. You can do some neat things with this:

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[::2]
# [0, 2, 4, 6, 8]

l[::3]
# [0, 3, 6, 9]

l[::-1]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# One final note on slicing... almost all of these slicing princples apply to
# strings too! You can index and slice strings just like lists, except that
# strings are immutable, so you cannot assign to slices.

abcs = 'abcdef'
abcs[2::2]
# 'ce'

# And speaking of how strings are immutable, there are immutable lists too.
# These are called tuples, and they use parentheses to enclose them.

tup = ('yo', 5)
type(tup)
# <type 'tuple'>

tup = ()
type(tup)
# <type 'tuple'>

tup = (5)
type(tup)
# <type 'int'>

# Uh-oh! Turns out that parentheses are already used for grouping, and so if you
# want a one-element tuple, you'll need to throw in a spare parenthesis.

tup = (5,)
type(tup)
# <type 'tuple'>

# There's not a ton to say about tuples... they're like lists, but you can't
# modify them. You can turn a list into a tuple:

tuple([1, 2, 3])
# (1, 2, 3)

# And you can turn a tuple into a list:

list((1, 2, 3))
# [1, 2, 3]

#### 4e. Dicts
# Let's talk dictionaries. These are simply hash tables, and it's very useful to
# have them implemented as part of the language. For example, if you wanted to
# map people's names to their ages, you could do this:

ages = {}

# It's empty!

ages = {'Stephen': 22, 'Brian': 21}

# It's initialized!  You can look things up by indexing.

ages['Stephen']
# 22

# You can also assign new values into the list like this:

ages['Joseph'] = 23

# And of course you can delete them in a way similar to list entries:

del ages['Brian']


### 4. LANGUAGE ELEMENTS
#### 4a. If statements, truthiness
# Okay, so we have a ton of data types and nothing to do with them. Let's talk
# ifs, fors, whiles, and functions! We can very easily use if statements like
# this:

if 5 < 3:
    print('pigs fly!')
elif 'a' == 'b':
    print('nope!')
else:
    print('this is the one!')

# First things first! Notice how there are no braces! Some people love it, some
# people hate it, but what are you going to do? Blocks are determined solely by
# indentation in Python. The standard is four spaces (NO TABS) defining a single
# block. If the indentation is inconsistent, you will get a syntax error!

# Python has the notion of "truthiness" -- a way to convert data types into
# booleans. If you use an expression that is not a boolean as the condition for
# an if-statement, Python will use this concept to convert to boolean first.
# We can see this in action with the bool() function:

bool('Stephen')
# True
bool('')
# False
bool([1, 2, 3])
# True
bool([])
# False
bool(12)
# True
bool(0)
# False

# The rules of truthiness are actually pretty simple. For numbers, 0 (of any
# type) is False, and all others are True. For containers, an empty container is
# False, and all others are True. Finally, the special value None (similar to
# null in other languages) is False. So now you can understand what this
# if-statement is testing:

l = [5]
if l:
    print('l has something in it')
else:
    print('l is empty')

#### 4b. While loops
# Python has while loops. You can do infinite loops like this:

while True:
    pass

# Note the use of `pass`. Since there are no braces, you can't do an empty block
# like this {}. So, `pass` is a no-op statement for places where you're required
# syntactically to have a block of code, but you have nothing to do there.

x = 0
while x < 5:
    x += 1

# Note something here. Many Java or C programmers might have used x++. However,
# there are no increment or decrement operators in Python! This is for an
# explicit reason: the language is designed so that numeric operations don't
# have side effects. For instance, in C, you can assign to a variable and use
# that as an expression:
#
# int x, y;
# x = (y = 5) + 3
#
# And of course the increment operators would look like this:
#
# x = x++ - x-- + (x = x - 3);
#
# To be sure, that's a stupid piece of code, but in general Python tries to
# avoid the confusion that arises from using assignment to variables within an
# expression.

# The other thing is that, while this is a perfectly fine loop, most Python
# programmers would turn their noses up at it. While C-style programmers are
# likely used to the loop index variable, Python has an alternative form of
# looping that ends up being much more convenient, pretty, and intuitive.

#### 4c. For loops, iterators
l = [1, 2, 3, 4]

for x in l:
    print(x)
# 1
# 2
# 3
# 4

i = 0
while i < len(l):
    print(l[i])
    i += 1

# Not only does the while loop have more lines (something that is usually
# avoided by having syntactic sugar in your for loop), it also has a lot more
# "moving parts". You need to use the len() function, do math with i, and index
# into the list. All of this is silly when you are simply trying to do something
# to each item in the list! This is the draw of the for-loop. It makes things
# which should be very obvious, obvious.
#
# So you are only allowed to loop over "iterables" in Python. So far we've seen
# lists, which are iterables. So are dicts and strings. Other things may be
# iterable in Python - they don't even need to be data structures. For instance,
# many functions return "generators". Let's see a useful example.

range(5)
# range(0, 5)

for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4

# As you can see, the range() function simply returns a "range object". This is
# an object which will produce the numbers we saw above when you iterate over
# it. It does NOT actually produce the list [0, 1, 2, 3, 4]. The reason why is
# actually pretty reasonable - you don't need the whole list in memory if you're
# just incrementing each number. You can convert things that would normally just
# be iterators (the range object being one of them) to lists using the list()
# function:

list(range(5))
# [0, 1, 2, 3, 4]

# Now, what if you want to modify the list as you iterate? Without the index,
# you can't update the list! That's where the enumerate() function comes in
# handy. It's another one that's like range() - it dynamically generates its
# results instead of creating a list.

l = ['a', 'b', 'c']
enumerate(l)
# <enumerate at 0xdeadbeef>

for index, character in enumerate(l):
    l[index] = 'a' + character
l
# ['aa', 'ab', 'ac']

# You can iterate over dicts as well. There are a couple ways you may want to do
# it, but all are fairly intuitive. If you want the pairs of items, do:

people = {'Stephen': 22, 'Ramon': 20}
for name, age in people.items():
    print('%s: %d' % (name, age))

# If you just want keys:

for name in people:
    pass

# Or, more explicitly (I recommend this):

for name in people.keys():
    print(name)

# Finally, if you just need the values:

for age in people.values():
    print(age)


#### 4d. Functions, splats, kwargs, and more
# Time to talk about functions! We've used them already - enumerate(), list(),
# range(), len(), and more. But those are built-in. How do we make our own? It's
# as simple as the def keyword.

def my_function(x):
    for i in range(x):
        print('hello world')

my_function(1)
# hello world

my_function(3)
# hello world
# hello world
# hello world

# This is pretty simple looking. Like normal variable declarations, function
# arguments have no type. They can be any type you'd like. So there's no
# guarantee that x would be a number - I could have done this:

my_function('oh heavens')
# TypeError: 'str' object cannot be interpreted as an integer

# So those of you who are used to the Java/C style of doing things might be
# screaming internally right now. After all, how can you be sure that your
# arguments are correct now? Will you check every argument to make sure it's the
# proper type?
#
# The answer to that is "please no". In Python, we rely on something we refer to
# kindly as "duck typing". As in, "if it looks like a duck, and it acts like a
# duck, then it's a duck". Your function shouldn't care what type it receives,
# so long as the argument behaves the way you expect. For instance, imagine a
# function that "adds up" the numbers in a list.

def addup(l):
    total = l[0]
    for val in l[1:]:
        total += val
    return total

addup([1, 2, 3, 4])
# 10

# Simple enough (although this expects the list to be non-empty). We could
# improve this in several ways but this is good enough. Now, what happens if we
# do this?

addup(['stephen ', 'is', ' the best'])
# 'stephen is the best'

# It works for strings too!  What about lists?

addup([[1, 2, 3], [4, 5, 6]])
# [1, 2, 3, 4, 5, 6]

# And the list (heh) goes on! As long as it supports the addition operation,
# this function will do something sensible with it. You could totally do this in
# a language like Java too - you would define an Addable interface, and your
# function would take a list of "addable" types, and then you would invoke the
# add() method that you had implemented for every type you wanted this to
# support. But this requires none of the boilerplate of declaring interfaces! We
# wrote a sensible function and got one that is generic, absolutely free! This
# is the power of duck typing.

# Now, let's talk more about function arguments. A common situation you will
# find is that functions should have a sane default, but a way to change odd
# parameters if you really want to. Python has keyword arguments to make this
# manageable:

def complex_function(arg, foo='bar'):
    print('arg=%r foo=%r' % (arg, foo))
complex_function('hello')
# arg=hello foo=bar

complex_function('hello', 'baz')
# arg=hello foo=baz

complex_function('hello', foo='bat')
# arg=hello foo=baz

# Note that there are two types of arguments here - keyword and positional. You
# can make functions that take *any* amount of positional arguments. You use a
# star before the name of the argument that collects them all. That argument
# will always be a list of args.

def echo_positional(*args):
    print(args)

echo_positional()
echo_positional(1)
# (1)
echo_positional(1, 'blah')
# (1, 'blah')

# You can do a similar thing with keyword arguments. Instead you use two stars,
# and you'll get a dict rather than a list.

def echo_keyword(**kwargs):
    for key, value in kwargs.items():
        print(key, '=', value)

# You can combine these, and also mix them with regular arguments:

def echo(*args, **kwargs):
    echo_positional(*args)
    echo_keyword(**kwargs)

def save_some(first, *args, mykey='hi', **kwargs):
    echo_positional(*args)
    echo_keyword(**kwargs)

# As you can see, the syntax works both ways. Use a star to take a list of items
# and unpack (splat) it as arguments to the function. Same with double star and
# dict. Finally, I use args, kwargs as variable names for these a lot. This is
# not required but it is convention.


#### 4e. Classes
# Like Java and many other languages, Python has classes. Unlike Java, you
# aren't required to use them for everything. Instead, you really only should
# use them when you need them. For everything else, functions are usually fine.
# There's a lot to be said about classes, so I'm just going to give you the high
# level overview.

class Foo(object):

    def __init__(self, arg):
        self.arg = arg

    def operation(self, arg):
        print('Foo(%r): operation(%r)' % (self.arg, arg))

# This simple example illustrates a lot of stuff. Declare the class with a
# class keyword. The `(object)` part states what your class inherits from. In
# Python 3, you don't explicitly need to put (object) there, but for historical
# and technical reasons that are out of scope, my advice is to just always put
# that.
#
# Methods are indented an extra level. They all receive the object instance (in
# Java terms, `this`) as their first argument. By convention, you REALLY should
# name this self. When you call these methods, you do NOT need to provide the
# self argument -- it is automatically filled out for you!
#
# __init__() is the constructor. In the constructor, you should initialize all
# your class's fields.
#
# Here is how you create a class instance:

foo = Foo('hello')

# And here is how you call a function on it:

foo.operation('world')
# Foo('hello'): operation('world')

# I'm going to leave my discussion of classes there. Theres a *lot* more to
# understand about them, but this will get you on your way towards creating and
# using the majority of classes.

#### 4f. List, set, and dict comprehensions.
# Many times you are doing a simple loop to create a list. It kind stinks to
# have to write a multiple line for loop to express a simple idea. So instead,
# you can use a list comprehension:

squares = [x ** 2 for x in range(10)]
squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# You can also do this for dictionaries:

square_dict = {x: x**2 for x in range(5)}
square_dict
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#### 4e. Exceptions and exception handling.
# It's important to be able to report and handle errors. Like Java, Python has
# exceptions.

raise Exception('you made a boo-boo')
# Exception: you made a boo-boo

# You can handle these with a try-except-finally clause:

try:
    raise Exception('you made a boo-boo')
except Exception:
    print('all better')

# You can get the actual exception instance like this:

except Exception as e:
    pass

# Finally clauses are executed regardless of whether an exception occurred.

try:
    raise Exception('oh no')
finally:
    print('finally')
# finally

try:
    pass
finally:
    print('finally')
# finally

# Finally clauses are great for cleanup that HAS to happen, regardless of
# whether an error happened. However, there is an even nicer way called context
# managers! Context managers are special objects that have built-in
# initialization and destruction logic. Use them inside a `with` block, and no
# matter how control leaves that block, the destruction logic will be executed.

with open('file.txt', 'w') as myfile:
    might_raise_an_error()
    # etc

# This is an example of opening a file. The operating system expects that you
# will close a file when you're done with it. In Python, you can do that
# manually by doing myfile.close(). But files are also context managers, and
# they will be closed automatically when you leave the with statement. Without
# context managers, this code would look a bit more gross:

try:
    myfile = open('file.txt', 'w')
    might_raise_an_error()
    # etc
finally:
    myfile.close()

# The context manager is a nice way to ensure cleanup happens without a finally
# clause.
#
# You can implement your own context manager, but that's a bit more of an
# advanced topic that we can talk about later.

### 5. Useful builtins
#### 5a. Files
# So we just saw how to open a file. The open function takes a filename and a
# mode string (r for read, w for write, a for append, and you can add on b for
# binary mode rather than text mode). The mode string can be omitted, in which
# case it is expected to be 'r'. Files can be read with the read() function and
# written with the write() function:

with open('file.txt') as txtfile:
    contents = txtfile.read()
print(contents)

# If you provide a 'size' argument, that will specify how many bytes to read.
#
# The write function writes a whole string:

with open('newfile.txt', 'w') as txtfile:
    txtfile.write('hello, file!\n')

# In Python, lots of things implement the file read()/write() interface, not
# just files. We call these file-like objects - it's similar to the reader and
# writer classes you find in Java.

#### 5b. zip()
# Many times you'll want to iterate over multiple lists. Here's an example:

one = ['a', 'b', 'c']
two = [1, 2, 3]

# Maybe you want to create a dictionary out of these. Maybe you want to do
# something else. Regardless, here is how you could do it (in a very clunky
# way):

for i in range(len(one)):
    print(one[i], two[i])

# But that's silly. Let's use zip! It takes two lists, and zips them into a list
# containing tuples (pairs) of items. It's actually pretty intuitive:

for first, second in zip(one, two):
    print(first, second)

# Zip will actually work with any number of lists:

zip(['a', 'b', 'c'], [1, 2, 3], ['do', 're', 'mi'])

# Zip is one of those generator type functions, as you can see, so if you want
# to get the whole list, use list() to get it:

list(zip(...))

### 6. MODULES
# So, how do you organize code in Python? This is a pretty big topic, and I
# could talk for a while about it, but I won't. Instead, I'll give you an
# overview of how modules work, and how you import them (along with standard
# libraries). Later I'll discuss how to install and use third-party modules.

# A module is just a python code file. Say you created a file named module.py.
# Then, you could import it with:
import module

# How does Python know where to look for module.py? It looks through a series of
# folders called your PYTHONPATH. Your PYTHONPATH always includes the directory
# you are currently in, so as long as you run your program/interpreter from the
# same directory as your custom module, you'll be able to import it.

# Now that you have module, you can use any functions you declared in it quite
# easily:
module.function()
module.variable = blah
instance = module.Class()

# There isn't really any notion of public/private in Python. That being said, by
# convention, anything that starts with a single underscore should be treated as
# private.

# If typing module every time is annoying you, you can shorten it up like this:

import module as m

# Now you can use things a bit more easily:

m.function()
m.variable = 'hi'
instance = m.Class()

# Finally, if you don't want to use the module object to access things, you can
# import right into your current namespace:

from module import Class
function()

# Something that can be useful when doing interactive shells is the "import *".
# This takes every symbol from a module and loads it into your current
# namespace:

from module import *
variable
instance = Class()

# Don't use this is real code (it makes it very difficult to discover where
# names came from). But inside of a REPL, it can be very convenient.

# Finally, let's talk about some standard libraries! Python comes with many of
# them, and they can all be imported quite easily:

import random
random.choice([1, 2, 3])
# ???

import os
os.listdir()
# ['all', 'your', 'files', 'are_here.py']

### 7. WHERE TO GET HELP
# At this point, you've learned most of the basics of Python, so
# congratulations! But of course there's plenty more to learn, that I didn't
# have time to cover. So here I'll point you to some resources where you can get
# more help.
#
# First, Python's tutorial. It should be your de-facto reference for getting
# started:
#
# https://docs.python.org/3/tutorial/index.html
#
# Second, Python's standard library documentation. This is a wonderful source of
# information! Python is FULL of a ton of useful libraries, and knowing what's
# available and how to use it is the first step to becoming a more competent
# Python programmer!
#
# https://docs.python.org/3/library/index.html
#
# Some highlighted modules you should check out:
#
# re (regular expressions)
# random (randomness)
# os (operating system)
# sys (Python "system" related stuff)
# collections (more useful data structures)
# socket (so much networking)
# multiprocessing, threading (for the concurrency)
# subprocess (call other programs)
#
# Finally, Python has just oodles and oodles of super high quality libraries for
# some really important tasks. You can find a little slide show full of
# recommendations right here:
#
# https://brennan.io/talks/2015/09/09/python-libraries/
#
# You'll be able to find the code for this talk right here:
#
# https://brennan.io/talks/

# As a final example, I'm going to just show how easy it is to use a Python
# library. One of my absolute favorite libraries is called "requests", and it
# makes web requests for you. It's brilliant.

# To install it, I just use:
# pip install requests

# Now, I can import it:

import requests
response = requests.get('https://brennan.io')
response.text
# lots of text from my website

# There's a lot more you can do with Python libraries, so don't hesitate to ask
# me about which ones you can/should use!

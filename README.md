# Python Training

```
>>> import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Topics:
* Basics
* Strings and Numbers
* Comparisons
* Control Flow
* Collections
* Iterators
* Loops
* Files
* Classes and Functions
* Pickling (Serializing)
* Exceptions
* Testing
* Debugging



## Basics
### Whitespace:
If you are coming from another programming lanaguage, the next directive may
strike you as a little odd, but it's imperitive to learning Python:

    Whitespace is everything!

Consider the following code block:
```python
>>> if 1 == 1: # Which it almost always will...
... print("One is equal to one.")

```

On the surface, it appears to be coherent code. We have a conditional if
clause and we follow it with an action to be taken, to print to STDOUT. If
you were to execute that code in Python, however, you would get the following:

```python
File "<stdin>", line 2
  print("One is equal to one.")
      ^
IndentationError: expected an indented block

```

The correct syntax for this example would be:
```python
>>> if 1 == 1:
...     print("One is equal to one.")
...
One is equal to one.
```

It's recommended that when you're coding in Python, you set
a default tab size in spaces. Personally, I set my tab to be interpreted as
four spaces. The current standard for Python styling (PEP 8) recommends that
a mixture of tabs and spaces be disallowed. This is enforcable by using the
-t and -tt CLI arguments to report warnings and errors respectively.

### Comments:
```python
>>> # Single line comment

>>> '''
... Multi-line comment
... Multi-line comment
... Multi-line comment
... '''
```

### Print to STDOUT:
```python
# Print a line that outputs, "Hello, World."
>>> print("Hello, World.")
```

### Importing from libraries:
When importing libraries, there are several ways to go about it. The most
common two ways are "import" and "from-import":
```python
>>> # An exmaple of an "import" statement
... import sys
>>> our_input = sys.argv[1] # assign the first argument from user input
>>>
>>> # An example of a "from-import" statement
... from sys import argv
>>> our_input = argv[1] # assign the first argument from user input
```

It is bad form to import all functions in a library with a "from-import"
statement. If you're going to import all of the functionality from a library,
it's recommended you follow the traditional "import" statement syntax.
```python
>>> from sys import *
>>> our_input = argv[1]
```

### Print to STDERR:

```python
# Import the 'sys' library from The Python Standard library
>>> import sys

'''
If we're running Python 3.X+, we don't need to fo the following done. If
not, we will need to import the "print_function" from the __future__
built-in library.

2.7.x:
print("Printing to standard error (stderr)", file=sys.stderr)
  File "<stdin>", line 1
    print("Printing to standard error (stderr)", file=sys.stderr)
                                                     ^
SyntaxError: invalid syntax

3.x:
print("Printing to standard error (stderr)", file=sys.stderr)
Printing to standard error (stderr)
'''
>>> import sysfrom __future__ import print_function

# Example of using the imported libraries
>>> import sysprint("Printing to standard error (stderr)", file=sys.stderr)
```


### Assigning variables:
```python
>>> '''
... Python is dynamically-typed language. Meaning, that a variable type doesn't
... need to be declared ahead of time or assigned specifically unless otherwise
... required through via casting.
... '''

>>> # Assign an integer to a var
>>> our_number = 1

>>> # Assign a string to a var
>>> our_string = "This is a string and such."

>>> # Perform math on "our_number"
>>> our_number * 5
5

>>> # Increment "our_number" by 1
>>> our_number += 1
>>> our_number
2

>>> # Decrement "our_number" by 1
>>> our_number -= 1
>>> our_number
1

>>> # Perform math on "our_string"
>>> our_string * 5
'This is a string and such.This is a string and such.This is a
string and such.This is a string and such.This is a string and such.'

```

### Constants:

Constants in Python are stylisticly defined as being ALL UPPERCASE with 
underscores separating multiple words. (e.g.: BUFFER_MIN, ACK_FLAG_SIZE)
```python
>>> BUFFER_MAX = 0x000040
>>>
>>> def get_current_buffer_track(self):
...     pass
```

## Strings and Numbers

```python
>>> alphabet = "ABCDEFGHI JKLMNOPQRSTUVWXYZ"
>>> integer = 123456789
>>> float = 3.14159
```

```python
Strings, in python, are immutable. To interact with strings, we can use a
variety of methods:
```

### Case and directionality:
```python
>>> # The case of our string can be modified easily using built-ins
>>> our_title = "an example of a title"
>>> our_title.title()
'An Example Of A Title'

>>> alphabet.capitalize()
'Abcdefghijklmnopqrstuvwxyz'

>>> len(alphabet)
26

>>> # Extended slicing allows us to reverse the directionality of the string
>>> # our_string[begin:end:step]
>>> alphabet[::-1]
'ZYXWVUTSRQPONMLKJIHGFEDCBA'

```

### Formatting:
The simplest example of formatting is string substitution:
```python
>>> # Assign values that we'll be subtituting below
>>> first_value = 70
>>> second_value = 1000
>>> # PEP 8 recommends that we break any line that is over 79 characters in 
>>> # length
>>> "This is test {0} out of {1} tests.".format(first_value, second_value)
'This is the 70th test out of 1000 tests.'
```

Furthermore, we can search through a string to find information we need:

### Find:
```python
>>> # Testing for content in a string; pythonic, simple
...
>>> 'Test' in 'Testing'
True

>>> our_string = "Example string called 'our_string'."
>>> find_string = "calle"
>>> print(our_string.find(find_string, 0, len(our_string)))
15
>>> print(our_string.find(find_string)) # simplified, /beg/ and /end/ are optional
15

```
### Slicing:
```python
>>> # Here we take the first index of a string and we slice it away from the rest
>>> # of the string
>>> alphabet[0]
'A'

>>> # We can do the same thing for the right side of the string by using
>>> # negative integers (i.e.: -3, -53, etc.)
>>> alphabet[-1]
'Z'

>>> 
>>> alphabet[1:]
'BCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> alphabet[:-1]
'ABCDEFGHIJKLMNOPQRSTUVWXY'

```
Note: Slicing applies not only to strings, but to lists as well!

### Split and join:
```python
>>> our_string = "This is an immutable string."
>>> print(our_string)
This is an immutable string.

>>> our_string = our_string.split()
>>> print(our_string)
['This', 'is', 'an', 'immutable', 'string.']

>>> our_string =  ' '.join(our_string)
>>> print(our_string)
This is an immutable string.

```

## Comparisons


### Comparison Operators
    <
    <=
    >
    >=
    ==
    != (<> (Deprecated as of 2.7 and removed in 3.0))
    is
    is not

```python
>>> our_int = 2
>>> our_bool = True
>>>
>>> if our_int > 1:
...     print("'our_int' is greater than 1.")
...
'our_int' is greater than 1.
>>> if our_int >=  2:
...     print("'our_int' is greater than or equal to 2.")
...
'our_int' is greater than or equal to 2.
>>> if our_int < 3:
...     print("'our_int' is less than 3.")
...
'our_int' is less than 3.
>>> if our_int <= 2:
...     print("'our_int' is less than or equal to 2.")
...
'our_int' is less than or equal to 2.
>>> if our_int == 2:
...     print("'our_int' is equal to 2.")
...
'our_int' is equal to 2.
>>> # When dealing with boolean values, you can use either == or 'is'
... if our_bool is True:
...     print("'our_bool' is True.")
...
'our_bool' is True.
>>> if our_bool is not False:
...     print("'our_bool' is not False.")
...
'our_bool' is not False.

```

### Boolean Operators
    or
    and

```python
>>> our_int = 100
>>>
>>> if our_int > 99 and our_int < 101:
...     print("This is an example of the 'and' operator.")
...
This is an example of the 'and' operator.
>>> if 99 < our_int < 101:
...     print("This is an abbreviation of the above operation.")
...
This is an abbreviation of the above operation.
>>>
>>> if our_int < 99 or our_int < 101:
...     print("This is an example of the 'or' operator.")
...
This is an example of the 'or' operator.

```

### Additional built-ins:
    any()
    all()

```python
>>> our_string = "This is a test 6er-ino!"
>>> our_rules = ["ino" in our_string,
...              our_string == "This is a test 6er-ino!",
...              len(our_string) > 100]
>>>
>>> print(our_rules)
[True, True, False]
>>>
>>> if any(our_rules):
...     print("Some of the rules matched.")
...
Some of the rules matched.
>>> our_rules = ["ino" in our_string,
...              our_string == "This is a test 6er-ino!",
...              len(our_string) > 10]
>>>
>>> print(our_rules)
[True, True, True]
>>>
>>> if all(our_rules):
...     print("All of the rules matched.")
...
All of the rules matched.
```

## Control Flow
```python
>>> condition = True
>>> another_condition = False
>>> statement = "Statement output."
>>>
>>> if condition:
...     statement
... elif another_condition:
...     statement
... else: # catch all
...     statement
...
'Statement output.'

```

## Collections
###Lists (aka "arrays")
```python
>>> our_list = ["This", "is", "an", "example", "example", "list", "."]
>>> our_string = "BANANA"
>>> our_converted_list = list(our_string)
>>> print(our_converted_list)
['B', 'A', 'N', 'A', 'N', 'A']
>>>
```
### Dictionaries (aka "hashmaps" and "associative arrays")
```python
>>> our_dict = {1: 'value_one', 'a': "value_fish"}
>>> our_dict['a']
'value_fish'
```
### Sets
```python
>>> our_list = ["This", "is", "an", "example", "example", "list", "."]
>>> set(our_list)
set(['This', 'is', 'list', '.', 'an', 'example'])
>>>
```

### Tuples
On the surface, a tuple is very similar to a list. The main difference between
the two is that a tuple is immutable.


    zip()

    map(operation, iterator) - Applies an operation to every iterable in
    /iterator/.
    filter(operation, iterator;) - Filters each iteraable in a iterator for which the filtering
    function returns True.
    reduce() - Applies a function or operation across all iterables in an
    iterator and returns a single output.


### Iterators
#### Enumerate
```python
>>> our_list
['This', 'is', 'an', 'example', 'example', 'list', '.']
>>> enumerate(our_list)
<enumerate object at 0x0235F760>
>>> for i in enumerate(our_list):
...     print(i)
...
(0, 'This')
(1, 'is')
(2, 'an')
(3, 'example')
(4, 'example')
(5, 'list')
(6, '.')

>>> for i in enumerate(our_list):
...     print(i)
...
0
1
2
3
4
5
6
```

#### range() (xrange() (Deprecated in 3.x+))
Here we use the xrange() function. This built-in is the preferred method of
listing a range in Python 2.X. In fact, in Python 3.X, range() has been
replaced by xrange() and xrange() is deprecated. The xrange() function takes
three arguments: xrange(start, end, step):

```python
>>> for i in xrange(100, 105, 2):
...     print(i)
...
100
102
104
```
#### len()
Returns the length of the passed object.
```python
>>> print(len(our_list))
7

```

## Loops
There are two main loop types in python: for loops and while loops. For loops
are best used for a finite sized collections (e.g.: a list of items) whereas 
while loops are best used for processing ambiguous data sets (e.g.: message 
bus request processing).

### For Loop
```python
>>> for i in xrange(0, 12):
...     if i >= 0 and i < 10:
...         print(i)
...         continue # Jumps to the next iteration of the loop
...     elif i >= 10:
...         print(i)
...         print("Never gonna get past 10.")
...         break # Terminates the loop
...     else:
...         pass # Does literally nothing; used as a placeholder when no code is to be executed
...
0
1
2
3
4
5
6
7
8
9
10
Never gonna get past 10.
```

### While Loop
```python
buff = []
message = 0x000001
while len(buff) < 100:
    buff.append(message)

print("The buffer contains {0} items.".format(len(buff)))
```

### Generators
(http://en.wikipedia.org/wiki/Generator_(computer_programming))

Generators are a form of iterator which allow us to deal with unwieldy data 
sets. A generator is comparable to a function in that it takes in arguments,
can be called, and can return values. The memory foot print of a generator is
much smaller than that of a function returning a large list of items. Yield
facilitates generator exhaustion by stepping through values. 

```python
>>> def isPrime(n):
...         n = abs(int(n))
...         if n % 2 == 0 and n > 2:
...                 return False
...         elif n < 2:
...                 return False
...         for i in range(3, int(math.sqrt(n))+1, 2):
...                 if n % i == 0:
...                         return False
...         return n
...
>>> def countUp(n):
...     while True:
...         yield n
...         n += 1
...
>>> for x in countUp(0):
...     if x <= 100000:
...         if isPrime(x):
...             print(x)
...     else:
...         break
...
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
# ...SNIP... #
```

## Files
```python
>>> with open('test.txt') as input_file
...     for i in input_file:
...         print(i)

```

In the following example, we are opening a file for "binary writing" in the
current working directory with the "filename.txt" file. The last line writes
a piece of JSON data out to the "input_file".

```python
with open(
            os.path.join(
                os.path.abspath(
                    os.path.dirname(__file__)
                    ), "filename.txt"
                ), "wb"
            ) as input_file:
            input_file.write(json.dumps(some_json_data)

```

## Classes and Functions

### Classes

A common structure in OO programming. There are two main types of operations
performed against Python classes: instantiation and object reference:

```python
class MyClass(object):
    def __init__(self):
        pass
        
    thing_list = []
    @classmethod
    def print_class_things(self):
        print self.thing_list
    @classmethod
    def write_class_things(self, *things):
        for i in things:
            self.thing_list.append(i)

testing = MyClass()
testing.print_class_things()
testing.write_class_things('thing_one', 'thing_two')
testing.print_class_things()

MyClass.print_class_things()
MyClass.write_class_things('thing_one', 'thing_two')
MyClass.print_class_things()
```


### Docstrings
```python
>>> """
... This is an example of a doc string. This commonly contains information about
... the class, function or top-level delcaration
... """

    def docStringExample(x):
    """ Takes an argument of 'x' and returns 'x' to the power of 'x'."""
    return x ** x

```

### 'args' vs 'kwargs'?
"args" and "kwargs" are a special type of function argument. These
arguments allow any number of variables to be passed in to the function. Let's
start with "*args":
```python
>>> def the_printer(*args):
...     for i in args:
...             print(i)
...
>>>
>>> the_printer(1, 2, 3, 4, 5, 6)
1
2
3
4
5
6

```

We don't specify the number of arguements up front. This can be helpful in
parsing a larger list of items without first knowing the number of items to
be passed up front. The last special argument is "**kwargs":

```python
>>> def parse_those_options(**kwargs):
...     print kwargs
...
>>>
>>> parse_those_options(start=10, end=100, dir='C:\\300\\impossible')
{'start': 10, 'end': 100, 'dir': 'C:\\300\\impossible'}


# The names are only by convention. You could juts as easily have *stuff and
# **stuff as names.

```


### Lambda Funtions:

Lambda functions are also known as anonymous functions, meaning that we can
use a function but not assign it a name. Lambda functions can be used to
perform simple one-line functions on the fly. This functionality was borrowed
from Lisp. 
```python
>>> def incrementor(n):
...   return lambda x: x + n
...
>>> main_incrementor = incrementor(10)
>>> main_incrementor(11)
21

```

## Pickling (Serializing)
### Pickle - Convert to byte stream
```python
#!/usr/bin/python
import pickle

data = {1: 'first data element',
        2: 'second data element',
        3: 'final data element'
        }

data2 = [x ** x for x in range(0, len(data))]

file_buff = open('barrel.pkl', 'wb')

# Pickle dictionary using index 0
pickle.dump(data, file_buff)

# Pickle the list using the highest index available.
pickle.dump(data2, file_buff, -1)

file_buff.close()

```

### Unpickle - Inverse operation of "pickle"
```python
#!/usr/bin/python

import pickle

file_buff = open('barrel.pkl', 'rb')

data = pickle.load(file_buff)
print(data)

data = pickle.load(file_buff)
print(data)

file_buff.close()

```

cPickle is an alternative to pickle. cPickle is approx. 1000x faster than
pickle. The largest issue is that since it is a purely C implementation of
the pickle library so there is no way to extend it natively in Python.


## Exceptions
### Try-Catch-Finally:
```python
>>> def ourFunction():
...     try:
...         raise KeyboardInterrupt
...     catch Exception as e:
...         print(e)
...         raise
...     finally: 
...         print("You're in the 'finally' block.")

```

## Testing


### Assertions:
```python
>>> class MyClass(object):
...     '''
...     This is a test
...     '''
...     def addEmUp(self, a, b):
...         x = a+ b
...         assert x - b == a 
...         return x
```

Assertions will produce an error assuming that the python application isn't
run with the -O (optimization) argument.

## Debugging
### PDB - The Python Debugger

Create the following python script:
```python
#!/usr/bin/python

import pdb

'''
Example script to show the the base functionality of the python debugger
(pdb)
'''


def setMyNumber():
    my_number = 1
    print("Setting 'my_number' to {0}...").format(my_number)

    print("""
Now we're trying to throw an AssertionError. This won't show when
run in optimized mode (-O). We do this by asserting that my_number
should be 2 when we hard-code it to be
""")

    assert my_number == 2


if __name__ == '__main__': # A conditional which doesn't run on import.
    pdb.set_trace() # breakpoint
    setMyNumber()

```

Using the script, we can illustrate the basics of Python's debugger (pdb).

    (n)ext - Next goes to the next function call, executing function calls at
    normal speed
    (s)tep - Steps in to the next function an debugs accordingly
    (j)ump - Accepts, one arg. Jumps to the line number provided
    (c)ontinue - Runs the app / script until a breakpoint is encountered
    (l)ist - Shows the current running line in context of the source code
    (a)rgs - Lists the args currently being passed
    (run) - Restart the app / script from the beginning with any args as args
    (q)uit - Quit

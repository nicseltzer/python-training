# FDC Python Training

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
Unordered list of topic titles

## Basics
Comments:
```python
>>> # Single line comment

>>> '''
... Multi-line comment
... Multi-line comment
... Multi-line comment
... '''
```

Print to standard out (stdout):
```python
# Print a line that outputs, "Hello, World."
>>> print("Hello, World.")
```

Importing from libraries:
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

Assigning variables:
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

>>> # Perform math on "our_string"
>>> our_string * 5
'This is a string and such.This is a string and such.This is a
string and such.This is a string and such.This is a string and such.'

```

## Strings and Numbers
```python
>>> alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
>>> integer = 0123456789
>>> float = 3.14159f
```python
Strings, in python, are immutable. To interact with strings, we can use a
variety of methods:

Slicing a string:
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
#>>> alphabet[1:]
'BCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> alphabet[:-1]
'ABCDEFGHIJKLMNOPQRSTUVWXY'
```

Case and directionality:
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

Formatting:
The simplest example of formatting is string substitution:
```
# Assign values that we'll be subtitutin below
>>> first_value = 70
>>> second_value = 1000
# PEP 8 recommends that we break any line that is over 79 characters in length
>>> "This is the {0}th test out of {1} tests.".format(first_value,\
... second_value)
'This is the 70th test out of 1000 tests.'
```

Furthermore, we can search through a string to find information we need:

Find:
```
>>> 'Test' in 'Testing'
True
```


Find, Replace, and Len
Formatting

## Comparisons

### Boolean Operators
    or
    and
    not

### Comparison Operators
    <
    <=
    >
    >=
    ==
    != (<> (Deprecated))
    is
    is not

## Control Flow
If-Then-Else

For Loop
    Break
    Continue
    Pass

Iterators
    Enumerate
    itertools
            itertools.permutations
    range() (xrange() (Deprecated in 3.x+))
    len()
    Generators
        Controlling generator exhaustion
        Yield

## Collections
    Lists
        list()
    Dicts
    Sets
    Tuples

    map() / zip()
    set()



## Loops
For loop
While loop

## Files
```
>>> with open(sys.argv[1]) as input_file

```

## Classes and Functions
```
>>> # Docstrings
>>> """
... This is an example of a doc string. This commonly contains information about
... the class delcaration that immediately precedes it.
... """
```

args vs kwargs

## Pickling (Serializing)
Pickle - Convert to byte stream
```
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
Unpickle - Inverse of pickle
```
#!/usr/bin/python

import pickle

file_buff = open('barrel.pkl', 'rb')

data = pickle.load(file_buff)
print(data)

data = pickle.load(file_buff)
print(data)

file_buff.close()

```

cPickle - 1000x faster than pickle


## Packaging
    __init__.py for imports and enforcing order for universal packages
        memory intensive for a large     number of imports across all modules

## JSON and XML and YAML

## Parsers

    JSON
    XML
    YAML
    BeautifulSoup - HTML


## Exceptions
Try-Catch-Finally:
```
>>> def ourFunction():
...     try:
...         raise KeyboardInterrupt
...     catch Exception as e:
...         print(e)
...         raise
...     finally: 
...         print("You're in the 'finally' block.")
```


Exception
    raise

## Testing

Unit Testing:
pyunit
```

```

Assertions:
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
The python debugger (pdb)

Create the following python script:
```
#!/usr/bin/python

import pdb

'''
Example script to show the the basal functionality of the python debugger
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


if __name__ == '__main__':
#    pdb.set_trace()
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

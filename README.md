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
```
>>> # Single line comment

>>> '''
... Multi-line comment
... Multi-line comment
... Multi-line comment
... '''
```

Print to standard out (stdout):
```
# Print a line that outputs, "Hello, World."
>>> print("Hello, World.")
```

Importing from libraries:
```
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
```
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
```
>>> alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
>>> integer = 0123456789
>>> float = 3.14159f
```
Strings, in python, are immutable. To interact with strings, we can use a
variety of methods:

Slicing a string:
```
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
```
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
```

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
Unpickle - Inverse of pickle
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
```
pyunit
```

Assertions:
```
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

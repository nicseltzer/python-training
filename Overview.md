# Python's Greatest Hits

Topics:
Unordered list of topic titles

## Basics
Comments:
```
# Single line comment

'''
Multi-line comment
Multi-line comment
Multi-line comment
'''
```

Print to standard out (stdout):
```
# Print a line that outputs, "Hello, World."
print("Hello, World.")
```

Importing from libraries:
```
# Import the 'sys' library from The Python Standard library
import sys

# If we're running Python 3.X+, we're done. If not...
from __future__ import print_function

# Example of using the imported libraries
print("Printing to standard out (stdout)", file=sys.stderr)
```

Assigning variables:
```
'''
Python is dynamically-typed language. Meaning, that a variable type doesn't
need to be declared ahead of time or assigned specifically unless otherwise
required through via casting.
'''

# Assign an integer to a var
our_number = 1

# Assign a string to a var
our_string = "This is a string and such."

# Perform math on "our_number"
our_number * 5
# Output: 5

# Perform math on "our_string"
our_string * 5
# Output: 'This is a string and such.This is a string and such.This is a
string and such.This is a string and such.This is a string and such.'

```

## Strings and Integers
```
```

Find, Replace, and Count
Formatting

## Comparisons

Boolean Operators
    or
    and
    not

Comparison Operators
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

## Files

## Classes and Functions
```
# Docstrings
"""
This is an example of a doc string. This commonly contains information about
the class delcaration that immediately precedes it.
"""
```

## Packaging
    __init__.py for imports and enforcing order for universal packages
        memory intensive for a large number of imports across all modules

## API

## Exceptions
Try-Catch-Finally
Exception
    raise

## Debugging

Assertions:
```
from types import StringType

class MyClass(object):
    '''
    This is a test
```

## Awesomeness
```
import this
```

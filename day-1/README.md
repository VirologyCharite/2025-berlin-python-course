# Day 1 (2025-08-25)

## Flow of control you encountered

* if / elif / else
* for loops
* while loops
* breaking out of a loop

## Data structures you encountered

* Dictionaries
* Lists
* Sets
* Numbers and strings

## Syntax you encountered

* `=` Used for assignment (`a = 3`).
* `==` Used for testing if two things are equal (`if a == 3:`).
* `()` To build a tuple (`a = (4, 5, 6)`) or to pass arguments to a function (`calculate("*", 3, 4)`).
* `[]` To access an element of a list or a tuple or a dictionary (e.g. `print(a[4])`). Or to build a list (`a = [4, 5, True]`).
* `{}` To build a set (`a = {"hello", 4}`) or to make a dictionary (`a = {}` or `a = {"name": "Joe", "age": 33}`).
* `,` Used to separate values in a tuple (`a = (3, 4)` or `calculate("*", 3, 4)`).
* `.` Used to access a function ("startswith") of an object ("line") (`line.startswith(">")`) or `line.lower()`.
* `"` Used to create a string. 
* `'` Used to create a string.

## Keywords you encountered

* `None` A special object (there is only one of them) used to set an non-existent or not initialized value or to return a special value to indicate that a function failed.
* `True` - Boolean (see also `False`).
* `break` - Gets you out of a loop.
* `def` - For defining a new function.
* `elif` - See `if`.
* `else` - See `if`.
* `for` - Starts a "for" loop (over a set of values of known size).
* `if` - Starts a conditional.
* `in` - Check if a value is in a `list`, `tuple`, `dict`, or `string`.
* `input` - Read a line (a string) from the user.
* `int` - Convert a string to an integer.
* `not` - Logical testing (`if answer is not "q"`).
* `pass` - Do nothing.
* `while` - Starts a while loop (over an uncertain number of things, terminated by a condition being false)

That's 14 of the
[35 keywords in Python](https://docs.python.org/3.12/reference/lexical_analysis.html#keywords)

![keywords](./images/keywords.png)

## Built-in functions you encountered

* `dict` - Make a dictioary
* `len` - Get the size (length) of something.
* `open` - Open a file (returns an open file object).
* `print` - Obvious.
* `set` - Make a set (`a = set((4, 5, 6))` or `a = set()`).

* `sum` - Add things up (`total = sum(4, 5, 6)`).

That's five of the
[71 builtins in Python](https://docs.python.org/3.12/library/functions.html#built-in-funcs). Of those, 
I only use 22 regularly.

![builtins](./images/builtins.png)

## String functions you encountered

* split
* startswith
* strip

Also:

* f-strings
* Single- versus double-quoted strings (and using backslash escapes)

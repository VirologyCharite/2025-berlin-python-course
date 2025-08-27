# Day 2 (2025-08-26)

## Flow of control you encountered

* try/except

## Exceptions you encountered

* `TypeError` - when doing an operation using an incorrect type (e.g., `3 + None`).
* `KeyError` - when trying to get a key that doesn't exist from a dictionary.

## Data structures you encountered

* Tuples - Just like a `list` but you cannot change it. `a = (3, 4, 5)`. Access elements with `[]`, e.g., `print(a[1])`.

## Syntax you encountered

Nothing new (yet)

## Keywords you encountered

* `False` - Boolean (see also `False`).
* `is` - Can be used to check if a variable refers to some exact object (e.g., `if a is None`).

## Built-in functions you encountered

* `all` - Returns True if all elements are true (`all(x for x in some_list)`).
* `any` - Returns True if any element is true (`any(x == 4 for x in (4, 5, 6))`).
* `list` - Turn something into a list (`list(reversed((3, 4, 6))` is `[6, 4, 3]`).
* `sum` - Add things up (`total = sum(4, 5, 6)`).
* `sorted` - Sort a series of things (returns a `list`).
* `reversed` - Reverse a series of things (list, tuple, etc)
* `range` - Returns a list of numbers. So `range(10)` gives you back 0, 1, .... 9.  Note that the return value is not actually a `list` but you can iterate over it and get the numbers. If you wanted a list all at once, you could say `numbers = list(range(10))`.


## String functions you encountered

* `string.join` to join a series of things into a single string, separated by the string. So `"-xxx-".join(("a", "b", "c")` gives `"a-xxx-b-xxx-c"` and `"".join(("a", "b", "c")` joins using the empty string and gives "abc".


## Dict functions you encountered

* `get` - gets the value for a dictionary key, and returns an alternate if
  the key isn't in the dictionary. `d.get("word", "default value")`. If you
  don't give a default, you get `None` back.


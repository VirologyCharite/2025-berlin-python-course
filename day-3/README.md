# Day 3 (2025-08-27)
## Data structures you encountered

* The `pandas` `DataFrame` (a very similar thing is used in `polars`). It's
  like an Excel spreadsheet, with rows and columns.

## Syntax you encountered

* `"\n"` - reprsents a newline in a string. We did `text.split("\n")` to
  split a bunch of text read from a page of a PDF into multiple lines.

## Keywords you encountered

* `as` - give a convenient (usually short) name to something you import (`import pandas as pd`).
* `from` - Indicate that you want to import something `from` a package (`from pypdf import PdfReader`).
* `import` - What you want to import (`import argparse`).
* `with` - Can be used to automatically close an opened file and has many other uses (`with open("file") as file_object:`).

## Built-in functions you encountered

* `str` - Can be used to turn anything into a string (`str(37)` is "37", `str(None)` is "None").
* `zip` - Extract items from multiple lists in parallel. Note: stops when the shortest list is exhausted.

## String functions you encountered

* `string.join` to join a series of things into a single string, separated by the string. So `"-xxx-".join(("a", "b", "c")` gives `"a-xxx-b-xxx-c"` and `"".join(("a", "b", "c")` joins using the empty string and gives "abc".

## New pacakges you encountered

* `pandas` - Can read Excel or CSV, gives you a `DataFrame`.
* `pprint` - Provides a function (also called `pprint`) for pretty printing
  of objects (`from pprint import pprint`).

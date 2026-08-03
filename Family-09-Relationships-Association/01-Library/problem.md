# Library

## Story

A library holds many books — that is a one-to-many relationship: one library,
many books.

The `Book` class is already written. Complete the `Library` class so it stores
books, reports how many it has, and finds a book by title.

## Task

The `Book` class is provided and complete. Do **not** modify it.

Complete the `Library` class. A library stores a list of `Book` objects, can add
a book, count how many books it holds, and find the first book with a given
title.

## Class Specification

### Book (provided, do not modify)

A `Book` object represents one book in a library.

It stores:

- the title (`title`)
- the author (`author`)

It provides `get_title` (returns the title) and `get_author` (returns the
author).

### Library

A `Library` object represents one library.

It stores:

- a list of books (`books`)

Initially the list is empty.

## Required Methods

### Library.__init__()

Create an empty list named `books`.

### Library.add_book(book)

Append the given book to the end of `books`.

### Library.count_books()

Return the number of books stored in the library.

### Library.find_by_title(title)

Loop over `books`. Return the first book whose title matches the given title. If
no book matches, return `None`.

## Constraints

- Titles and authors are non-empty strings
- Titles may repeat; `find_by_title` returns the first match
- All inputs are valid

## Example

```python
library = Library()
library.add_book(Book("Python Basics", "Ada"))
library.add_book(Book("Data Works", "Bo"))
print(library.count_books())

found = library.find_by_title("Python Basics")
print(found.get_author())

missing = library.find_by_title("No Book")
print(missing)
```

Output

```text
2
Ada
None
```

## Explanation

The library holds a list of books. `count_books` returns how many (2).
`find_by_title` loops over the books and returns the first book whose title
matches — `"Python Basics"` is by `"Ada"`. When no book matches (`"No Book"`),
it returns `None`. One library, many books: that is a one-to-many association.

## Hint

In `find_by_title`, loop over `self.books`, compare `book.get_title()` with the
given title, and return the book on the first match. After the loop, return
`None`.

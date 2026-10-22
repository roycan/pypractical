# Library Book

## Story

A school library keeps track of its publications. Every publication has a title
and an author. A book also has a page count, and the library must never record a
book with zero or negative pages — that would be garbage data.

## Task

The `Publication` class is provided and complete. Do **not** modify it.

Complete the `Book` class so a book inherits the publication's title and author
and protects its own page count.

## Class Specification

### Publication (provided, do not modify)

A `Publication` object represents one published item.

Each publication stores:

- the publication's title (`title`)
- the publication's author (`author`)

### Book

A `Book` object represents one book in the library. A book IS-A publication.

Each book should remember:

- the inherited publication's title and author
- a protected page count (`_number_of_pages`)

## Required Methods

### Book.\_\_init\_\_(title, author, number_of_pages)

Call `super().__init__(title, author)` so the book inherits the title and
author. Then assign the page count to `self.number_of_pages` so the setter
below validates and stores it.

### Book.number_of_pages (property)

Use the `@property` decorator so callers read the page count as
`book.number_of_pages` — no parentheses. Return the protected
`_number_of_pages`.

### Book.number_of_pages (setter)

Use the `@number_of_pages.setter` decorator. Validate the page count:

- if the value is zero or negative, print
  `"The number of pages must be positive"` and store `0` as the placeholder
  meaning "not recorded"
- otherwise store the value in the protected attribute `_number_of_pages`

## Constraints

- title is a non-empty string
- author is a non-empty string
- number_of_pages is an integer (it may be zero or negative — the constructor
  must handle that case)

## Example

```python
publication = Publication("Poems", "A. Cruz")
print(publication.display_info())

book = Book("Clean Code", "R. Martin", 464)
print(book.display_info())
print(book.number_of_pages)

bad_book = Book("Mystery", "J. Doe", -5)
print(bad_book.number_of_pages)
```

Output

```text
Title: Poems, Author: A. Cruz
Title: Clean Code, Author: R. Martin
464
The number of pages must be positive
0
```

## Explanation

`publication` is a plain `Publication`. The `book` is a `Book`, so it is also a
publication: its `title` and `author` come from the parent through
`super().__init__(title, author)`, and its `display_info()` is the parent's
method, reused unchanged. The page count is protected: `book.number_of_pages`
reads it through the `@property` getter, and the `@number_of_pages.setter`
validates every value before it is stored. `bad_book` is given a negative page
count, so the setter prints a warning and stores the placeholder `0` — its data
is rejected, not silently kept.

## Hint

Write `class Book(Publication):` so the book inherits from the parent. In
`__init__`, call `super().__init__(title, author)` first, then assign
`self.number_of_pages = number_of_pages` so the setter runs. Decorate the getter
with `@property` and the setter with `@number_of_pages.setter`. In the setter,
check the value with `<= 0` before storing it in `self._number_of_pages` — zero
pages is garbage data too.

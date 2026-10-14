# Book Borrowing

## Story

A software company is building a borrowing system for a digital library. The
borrowing management algorithm is already written and tested. Two important
classes are still incomplete, so the system cannot run yet.

## Task

Complete the `Book` and `Member` classes. The borrowing management algorithm is
provided and complete. Do **not** modify it.

A `Member` object interacts with `Book` objects: it checks a book before
borrowing it, remembers every borrowed book, and each borrowed book loses one
available copy.

## Class Specification

### Book

A `Book` object represents one library book.

It stores:

- the title (`title`)
- the author (`author`)
- the number of available copies (`copies`)

### Member

A `Member` object represents one library member.

It stores:

- the maximum number of books they may borrow (`limit`)
- every borrowed book (`borrowed_books`)

Initially `borrowed_books` is an empty list.

## Required Methods

### Book.__init__(title, author, copies)

Store the three values as instance variables.

### Member.__init__(limit)

Store the borrowing limit and create the empty list `borrowed_books`.

### Member.can_borrow(book)

Return `True` if the member may borrow the given book, otherwise return
`False`. A member may borrow a book when both conditions hold:

- `len(borrowed_books) < limit` — the borrowing limit is not reached
- `book.copies > 0` — at least one copy is available

### Member.borrow(book)

Add the book to `borrowed_books` and decrease `book.copies` by `1`.

### process_borrow_requests(requests) (provided, do not modify)

The borrowing management algorithm. It takes a list of requests, where each
request is a tuple:

- `("ADD_BOOK", title, author, copies)` — create a book
- `("ADD_MEMBER", member_id, limit)` — create a member
- `("BORROW", member_id, title)` — try to borrow a book

For a `BORROW` request the system calls `can_borrow(book)` first and calls
`borrow(book)` only when it returns `True`. The function returns two
dictionaries: the books keyed by title and the members keyed by member id.

You do not need to write this function. It is provided in the starter code and
the automatic tests use it.

## Constraints

- At most 100 books
- The number of copies is at least 0
- The borrow limit is at least 1
- Titles and author names are non-empty strings

## Example

```python
book = Book("Python Basics", "Smith", 3)
member = Member(2)

print(member.can_borrow(book))

member.borrow(book)
print(book.copies)
print(len(member.borrowed_books))
```

Output

```text
True
2
1
```

## Explanation

The member starts with no borrowed books, so `0 < 2` is true, and the book has
copies — `can_borrow` returns `True`. After borrowing, the member's list holds
one book and the book has `3 - 1 = 2` available copies. One member connects to
many borrowed books: that is the association between the two objects.

## Hint

In `can_borrow`, check `len(self.borrowed_books) < self.limit` and
`book.copies > 0`. In `borrow`, append the book to `self.borrowed_books` and
subtract 1 from `book.copies`. Objects can interact with other objects: a
`Member` method may read and change a `Book` object's attributes.

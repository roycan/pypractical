# Teacher Notes — Book Borrowing

> Family 090 · Relationships - Association · Assessment 09 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students model a two-class association: a `Member` object holds references to
the `Book` objects it borrows. Both classes are incomplete; students write the
attributes, a boolean check that reads another object's state, and a mutator
that changes another object's state. The borrowing management algorithm is
provided, so the graded surface is exactly the interaction between the two
classes.

## Concepts Reinforced

- Object relationships
- Association (a "has-a" relationship)
- One-to-many multiplicity (one member, many borrowed books)
- Objects interacting: reading and changing another object's attributes
- Classes and objects
- Lists as instance state
- Boolean logic with two conditions (`and`)

## Common Student Mistakes

- Checking the limit but forgetting the copies, or the reverse.
- Using the comparison in the wrong direction, for example
  `len(borrowed_books) < limit` written as `>` or replaced with `<=`.
- Appending the book's title instead of the book object.
- Forgetting to decrease `book.copies` in `borrow`.
- Creating `borrowed_books` inside `borrow` instead of initializing it in
  `__init__`.

## Suggested Teaching Strategy

1. Draw one `Member` box connected to many `Book` boxes — the same one-to-many
   shape as Assessment 01, now with interaction between the two sides.
2. Trace `can_borrow` by hand: two conditions decide everything, the member's
   limit and the book's copies.
3. Emphasize that `borrow` changes another object: `book.copies` belongs to the
   `Book`, not to the `Member`.
4. Show the provided `process_borrow_requests` function briefly: it only calls
   the two methods students wrote. Their classes are what make the system work.

## Automatic Assessment

`tests.py` runs 17 equal-weight behavior tests grouped into Book, Member, the
provided borrowing system, and hidden cases. Hidden tests check only documented
behavior and add no new requirements. A student's score is the percentage of
passing tests.

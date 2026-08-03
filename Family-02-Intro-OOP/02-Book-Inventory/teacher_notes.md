# Teacher Notes — Book Inventory

> Family 02 · Intro to OOP · Assessment 02 · Difficulty 1/5 · ~15 minutes

## Learning Objective

Students define their first class: an object bundles its own data as instance
variables, and a method uses that data instead of receiving it as arguments.

## Concepts Reinforced

- Defining a class
- Writing a constructor (`__init__`)
- Instance variables (state) with `self`
- Methods that read instance variables
- Objects are independent (each holds its own state)

## Common Student Mistakes

- Forgetting `self.` when creating or reading instance variables.
- Storing parameters in local variables instead of `self.title`, `self.price`,
  `self.copies`.
- Treating `stock_value` like a function that takes arguments, instead of using
  `self.price` and `self.copies`.
- Returning a value from `__init__`.
- Making two books share the same variable by mistake.

## Suggested Teaching Strategy

1. Contrast the procedural way first: a function `stock_value(title, price,
   copies)` that receives three loose arguments.
2. Show that a `Book` object keeps its own title, price, and copies together,
   so the data is not scattered.
3. Trace the example by hand: create a book, read each attribute, then call
   `stock_value`.
4. Emphasize that `stock_value` uses `self.price` and `self.copies`. The
   object already knows them.
5. Demonstrate that two book objects never mix their data (the independence
   tests).

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests: stored attributes, `stock_value`
(basic, boundary, typical), object independence, and hidden cases. Hidden tests
check only documented behavior and add no new requirements. A student's score is
the percentage of passing tests.

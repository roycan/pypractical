# Teacher Notes — Ticket Sales

> Family 02 · Intro to OOP · Assessment 03 · Difficulty 1/5 · ~15 minutes

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
- Storing parameters in local variables instead of `self.event`, `self.price`,
  `self.seats`.
- Treating `potential_revenue` like a function that takes arguments, instead of
  using `self.price` and `self.seats`.
- Returning a value from `__init__`.
- Making two tickets share the same variable by mistake.

## Suggested Teaching Strategy

1. Contrast the procedural way first: a function `potential_revenue(event,
   price, seats)` that receives three loose arguments.
2. Show that a `Ticket` object keeps its own event, price, and seats together,
   so the data is not scattered.
3. Trace the example by hand: create a ticket, read each attribute, then call
   `potential_revenue`.
4. Emphasize that `potential_revenue` uses `self.price` and `self.seats`. The
   object already knows them.
5. Demonstrate that two ticket objects never mix their data (the independence
   tests).

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests: stored attributes,
`potential_revenue` (basic, boundary, typical), object independence, and hidden
cases. Hidden tests check only documented behavior and add no new requirements.
A student's score is the percentage of passing tests.

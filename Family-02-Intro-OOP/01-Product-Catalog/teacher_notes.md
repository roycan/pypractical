# Teacher Notes — Product Catalog

> Family 02 · Intro to OOP · Assessment 01 · Difficulty 1/5 · ~15 minutes

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
- Storing parameters in local variables instead of `self.name`, `self.price`,
  `self.quantity`.
- Treating `total_value` like a function that takes arguments, instead of using
  `self.price` and `self.quantity`.
- Returning a value from `__init__`.
- Making two products share the same variable by mistake.

## Suggested Teaching Strategy

1. Contrast the procedural way first: a function `total_value(name, price,
   quantity)` that receives three loose arguments.
2. Show that a `Product` object keeps its own name, price, and quantity
   together, so the data is not scattered.
3. Trace the example by hand: create a product, read each attribute, then call
   `total_value`.
4. Emphasize that `total_value` uses `self.price` and `self.quantity`. The
   object already knows them.
5. Demonstrate that two product objects never mix their data (the independence
   tests).

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests: stored attributes, `total_value`
(basic, boundary, typical), object independence, and hidden cases. Hidden tests
check only documented behavior and add no new requirements. A student's score is
the percentage of passing tests.

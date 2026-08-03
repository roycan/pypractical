# Teacher Notes — Seed Order

> Family 02 · Intro to OOP · Assessment 04 · Difficulty 1/5 · ~15 minutes

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
- Storing parameters in local variables instead of `self.variety`, `self.price`,
  `self.packets`.
- Treating `order_total` like a function that takes arguments, instead of using
  `self.price` and `self.packets`.
- Returning a value from `__init__`.
- Making two seed packets share the same variable by mistake.

## Suggested Teaching Strategy

1. Contrast the procedural way first: a function `order_total(variety, price,
   packets)` that receives three loose arguments.
2. Show that a `SeedPacket` object keeps its own variety, price, and packets
   together, so the data is not scattered.
3. Trace the example by hand: create a seed packet, read each attribute, then
   call `order_total`.
4. Emphasize that `order_total` uses `self.price` and `self.packets`. The
   object already knows them.
5. Demonstrate that two seed packet objects never mix their data (the
   independence tests).

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests: stored attributes, `order_total`
(basic, boundary, typical), object independence, and hidden cases. Hidden tests
check only documented behavior and add no new requirements. A student's score is
the percentage of passing tests.

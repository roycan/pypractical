# Teacher Notes — Fee Report

> Family 07 · Polymorphism · Assessment 03 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students process a list of different object types through a shared method. The
report calls the same `fee` method on every payment, and each payment's class
decides what value comes back.

## Concepts Reinforced

- Polymorphism (same method name, different behavior per class)
- Duck typing (the report never checks a payment's class)
- Classes and objects
- Methods
- Loops over a collection
- Building and summing a list

## Common Student Mistakes

- Checking the payment's class with `isinstance` instead of just calling the
  method.
- Forgetting to loop over `self.payments`.
- Returning inside the loop (stops after the first payment).
- Mixing up `fees` (returns a list) and `total_fees` (returns an integer).
- Forgetting to start `payments` as an empty list.

## Suggested Teaching Strategy

1. Show the two provided classes side by side: both have `fee`, but
   `Cash.fee()` returns `0` while `Card.fee()` returns `amount // 10`.
2. Emphasize that the report does NOT care which class a payment is — it calls
   `fee()` on all of them.
3. Trace the example: add a cash and a card payment, then read `fees()` and
   `total_fees()`.
4. Highlight that this is polymorphism: one method name, different results.
5. Have students run the tests to confirm both the list and the total are right.

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests grouped into an empty-report
check, `fees()`, `total_fees()`, and hidden cases. Hidden tests check only
documented behavior and add no new requirements. A student's score is the
percentage of passing tests.

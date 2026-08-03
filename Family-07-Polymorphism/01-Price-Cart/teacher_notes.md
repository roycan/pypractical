# Teacher Notes — Price Cart

> Family 07 · Polymorphism · Assessment 01 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students process a list of different object types through a shared method. The
cart calls the same `amount` method on every item, and each item's class decides
what value comes back.

## Concepts Reinforced

- Polymorphism (same method name, different behavior per class)
- Duck typing (the cart never checks an item's class)
- Classes and objects
- Methods
- Loops over a collection
- Building and summing a list

## Common Student Mistakes

- Checking the item's class with `isinstance` instead of just calling the method.
- Forgetting to loop over `self.items`.
- Returning inside the loop (stops after the first item).
- Mixing up `amounts` (returns a list) and `total` (returns an integer).
- Forgetting to start `items` as an empty list.

## Suggested Teaching Strategy

1. Show the two provided classes side by side: both have `amount`, but
   `FullPrice.amount()` returns the full price while `HalfPrice.amount()` returns
   half.
2. Emphasize that the cart does NOT care which class an item is — it calls
   `amount()` on all of them.
3. Trace the example: add a full-price and a half-price item, then read
   `amounts()` and `total()`.
4. Highlight that this is polymorphism: one method name, different results.
5. Have students run the tests to confirm both the list and the total are right.

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests grouped into an empty-cart check,
`amounts()`, `total()`, and hidden cases. Hidden tests check only documented
behavior and add no new requirements. A student's score is the percentage of
passing tests.

# Teacher Notes — Weight Scale

> Family 07 · Polymorphism · Assessment 04 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students process a list of different object types through a shared method. The
scale calls the same `weight` method on every load, and each load's class decides
what value comes back.

## Concepts Reinforced

- Polymorphism (same method name, different behavior per class)
- Duck typing (the scale never checks a load's class)
- Classes and objects
- Methods
- Loops over a collection
- Building and summing a list

## Common Student Mistakes

- Checking the load's class with `isinstance` instead of just calling the method.
- Forgetting to loop over `self.loads`.
- Returning inside the loop (stops after the first load).
- Mixing up `weights` (returns a list) and `total_weight` (returns an integer).
- Forgetting to start `loads` as an empty list.

## Suggested Teaching Strategy

1. Show the two provided classes side by side: both have `weight`, but
   `Light.weight()` returns `count * 1` while `Heavy.weight()` returns
   `count * 5`.
2. Emphasize that the scale does NOT care which class a load is — it calls
   `weight()` on all of them.
3. Trace the example: add a light and a heavy load, then read `weights()` and
   `total_weight()`.
4. Highlight that this is polymorphism: one method name, different results.
5. Have students run the tests to confirm both the list and the total are right.

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests grouped into an empty-scale
check, `weights()`, `total_weight()`, and hidden cases. Hidden tests check only
documented behavior and add no new requirements. A student's score is the
percentage of passing tests.

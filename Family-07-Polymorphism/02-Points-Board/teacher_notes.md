# Teacher Notes — Points Board

> Family 07 · Polymorphism · Assessment 02 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students process a list of different object types through a shared method. The
board calls the same `points` method on every task, and each task's class decides
what value comes back.

## Concepts Reinforced

- Polymorphism (same method name, different behavior per class)
- Duck typing (the board never checks a task's class)
- Classes and objects
- Methods
- Loops over a collection
- Building and summing a list

## Common Student Mistakes

- Checking the task's class with `isinstance` instead of just calling the method.
- Forgetting to loop over `self.entries`.
- Returning inside the loop (stops after the first task).
- Mixing up `points_list` (returns a list) and `total_points` (returns an
  integer).
- Forgetting to start `entries` as an empty list.

## Suggested Teaching Strategy

1. Show the two provided classes side by side: both have `points`, but
   `Easy.points()` returns `level * 1` while `Hard.points()` returns `level * 3`.
2. Emphasize that the board does NOT care which class a task is — it calls
   `points()` on all of them.
3. Trace the example: add an easy and a hard task, then read `points_list()` and
   `total_points()`.
4. Highlight that this is polymorphism: one method name, different results.
5. Have students run the tests to confirm both the list and the total are right.

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests grouped into an empty-board
check, `points_list()`, `total_points()`, and hidden cases. Hidden tests check
only documented behavior and add no new requirements. A student's score is the
percentage of passing tests.

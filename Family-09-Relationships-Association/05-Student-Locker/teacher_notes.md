# Teacher Notes — Student Locker

> Family 09 · Relationships I (Association) · Assessment 05 · Difficulty 2/5 · ~15 minutes

## Learning Objective

Students model the simplest association: one object stores a reference to
another object, and the code handles both the "has it" and "doesn't have it"
cases.

## Concepts Reinforced

- Object relationships
- Association (a "has-a" relationship)
- Classes and objects
- A single object reference as instance state
- Handling `None` (the "no object yet" case)

## Common Student Mistakes

- Comparing `self.locker` to `None` with `==` instead of `is` (both work, but
  `is` is clearer; accept either).
- Forgetting to set `self.locker = None` in `__init__`.
- Returning the locker object instead of its number in `get_locker_number`.
- Forgetting the `"No locker"` string case.
- Not calling `get_number()` on the locker and instead returning the whole object.

## Suggested Teaching Strategy

1. Emphasize the "has-a" idea: a student has a locker.
2. Draw the object reference: `Student.locker` points to a `Locker` (or to
   nothing, `None`).
3. Trace the two cases in `get_locker_number`: with and without a locker.
4. Contrast this with the list-based problems: here the student holds at most
   one locker, not a list of many.

## Automatic Assessment

`tests.py` runs 8 equal-weight behavior tests: the no-locker default, assigning
a locker, reading the number, reading the combination, and hidden cases for
independence and different values. Hidden tests check only documented behavior
and add no new requirements. A student's score is the percentage of passing
tests.
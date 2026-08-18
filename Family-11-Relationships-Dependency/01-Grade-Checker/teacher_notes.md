# Teacher Notes — Grade Checker

> Family 11 · Relationships III (Dependency) · Assessment 01 · Difficulty 2/5 · ~15 minutes

## Learning Objective

Students write a class that uses another class only as a method parameter —
reading its data and returning a result — without ever storing it. This is the
"uses-a" (dependency) relationship.

## Concepts Reinforced

- Object relationships
- Dependency (a "uses-a" relationship)
- Classes and objects
- Methods that accept objects as parameters
- Calling getters on a parameter
- if / elif chains

## Common Student Mistakes

- Storing the `Answer` in `__init__` (that would be aggregation, not dependency).
- Returning the whole `Answer` object instead of a derived value.
- Using `>` instead of `>=` at a grade boundary (90, 80, 70, 60).
- Checking the grade cutoffs in ascending order instead of descending.
- Forgetting the `"Tie"` result in `compare`.

## Suggested Teaching Strategy

1. Contrast "has-a" (association) with "uses-a" (dependency): `GradeChecker`
   never keeps the `Answer`; it only touches it while the method runs.
2. Show a diagram: the `Answer` exists independently and is passed in as an
   argument, then used.
3. Emphasize that `GradeChecker` has no `__init__` because it stores nothing.
4. Trace the grade boundaries carefully: 90 → A, 89 → B, 80 → B, 79 → C, etc.

## Automatic Assessment

`tests.py` runs 18 equal-weight behavior tests: pass/fail, all five letter
grades, grade boundaries, comparison (higher/tie), and hidden cases. Hidden
tests check only documented behavior and add no new requirements. A student's
score is the percentage of passing tests.
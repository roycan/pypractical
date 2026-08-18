# Teacher Notes — Score Report

> Family 11 · SOLID - Single Responsibility · Assessment 02 · Difficulty 4/5 · ~25 minutes

## Learning Objective

Students apply the Single Responsibility Principle by splitting data handling
from presentation into two classes.

## Concepts Reinforced

- Single Responsibility Principle (SRP)
- SOLID design
- Separation of concerns
- Classes and objects
- Methods
- Passing one object to another (a dependency)

## Common Student Mistakes

- Storing points in the Report class.
- Formatting the summary string inside the Score class.
- Mismatched summary string (wrong spacing or punctuation).
- Computing the total inside the summary instead of calling `score.total()`.
- Using a comprehension instead of an explicit loop for the total.

## Suggested Teaching Strategy

1. Emphasize that one class equals one reason to change.
2. The Score has one job: store points and compute the count and sum.
3. The Report has one job: build a readable string from a Score.
4. The Report depends on the Score (it uses it); the Score knows nothing of
   formatting.
5. Trace the example: build a Score, add points, then hand it to a Report.

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests: Score count/total/empty/single,
Report summary variants, and a check that reports never store data. Hidden
tests check only documented behavior and add no new requirements. A student's
score is the percentage of passing tests.

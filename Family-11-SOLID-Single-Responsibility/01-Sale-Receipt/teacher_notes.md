# Teacher Notes — Sale Receipt

> Family 11 · SOLID - Single Responsibility · Assessment 01 · Difficulty 4/5 · ~25 minutes

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

- Storing amounts in the Receipt class.
- Formatting the summary string inside the Sale class.
- Mismatched summary string (wrong spacing or punctuation).
- Computing the total inside the summary instead of calling `sale.total()`.
- Using a comprehension instead of an explicit loop for the total.

## Suggested Teaching Strategy

1. Emphasize that one class equals one reason to change.
2. The Sale has one job: store amounts and compute the count and total.
3. The Receipt has one job: build a readable string from a Sale.
4. The Receipt depends on the Sale (it uses it); the Sale knows nothing of
   formatting.
5. Trace the example: build a Sale, add amounts, then hand it to a Receipt.

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests: Sale count/total/empty/single,
Receipt summary variants, and a check that receipts never store data. Hidden
tests check only documented behavior and add no new requirements. A student's
score is the percentage of passing tests.

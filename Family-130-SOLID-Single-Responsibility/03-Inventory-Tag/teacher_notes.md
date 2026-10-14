# Teacher Notes — Inventory Tag

> Family 13 · SOLID - Single Responsibility · Assessment 03 · Difficulty 4/5 · ~25 minutes

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

- Storing quantities in the Tag class.
- Formatting the summary string inside the Stock class.
- Mismatched summary string (wrong spacing or punctuation).
- Computing the total inside the summary instead of calling `stock.total()`.
- Using a comprehension instead of an explicit loop for the total.

## Suggested Teaching Strategy

1. Emphasize that one class equals one reason to change.
2. The Stock has one job: store quantities and compute the count and total.
3. The Tag has one job: build a readable string from a Stock.
4. The Tag depends on the Stock (it uses it); the Stock knows nothing of
   formatting.
5. Trace the example: build a Stock, add quantities, then hand it to a Tag.

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests: Stock count/total/empty/single,
Tag summary variants, and a check that tags never store data. Hidden tests check
only documented behavior and add no new requirements. A student's score is the
percentage of passing tests.

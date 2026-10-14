# Family 07 — Polymorphism

> SG 11 · Difficulty 3/5 · ~20 min

## Overview

Students call the same method on different object types and let each class decide
the result — the duck-typing pattern behind real carts, scoreboards, and fee
reports.

## Primary Learning Objective

The same method call produces different results across object types.

## Concepts Reinforced

- Polymorphism (same method name, different behavior per class)
- Duck typing (the caller never checks an item's class)
- Classes and objects
- Methods
- Loops over a collection
- Building and summing a list

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Price-Cart | Full and half price |
| 02 | 02-Points-Board | Easy and hard tasks |
| 03 | 03-Fee-Report | Cash and card |
| 04 | 04-Weight-Scale | Light and heavy loads |

All variants are isomorphic: same concept and difficulty, different stories, for
fairness across class sections.

## Learning Progression

- Previous: Family 06 — Method Overriding
- Current: Family 07 — Polymorphism
- Next: Family 08 — Abstraction

## Common Student Mistakes

- Checking the item's class with `isinstance` instead of just calling the method.
- Forgetting to loop over `self.items`.
- Returning inside the loop (stops after the first item).
- Mixing up `amounts` (returns a list) and `total` (returns an integer).
- Forgetting to start `items` as an empty list.

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Round 2 (2026-08).

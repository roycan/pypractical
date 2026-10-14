# Family 04 — Encapsulation

> SG 8 · Difficulty 2/5 · ~20 min

## Overview

Students protect an object's data behind a private attribute with validating
accessors and mutators, so the object enforces its own rules — like a bank
account that refuses an invalid withdrawal.

## Primary Learning Objective

Protect an object's data with a private attribute and validating
accessors/mutators.

## Concepts Reinforced

- Encapsulation
- Classes and objects
- Instance variables
- Methods
- Accessors (getters) and mutators

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Bank-Account | Account balance |
| 02 | 02-Fuel-Tank | Fuel in litres |
| 03 | 03-Piggy-Bank | Saved coins |
| 04 | 04-Water-Tank | Water in litres |

All variants are isomorphic: same concept and difficulty, different stories, for
fairness across class sections.

## Learning Progression

- Previous: Family 03 — Classes and Objects
- Current: Family 04 — Encapsulation
- Next: Family 05 — Inheritance

## Common Student Mistakes

- Exposing the balance without a leading underscore.
- Forgetting the `amount > 0` check in `deposit` or `withdraw`.
- Allowing an overdraft (withdrawing more than the balance).
- Returning a value from a void mutator (`deposit` or `withdraw`).

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Round 2 (2026-08).

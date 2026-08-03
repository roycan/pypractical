# Family 01 — Minimum Cost

> SG (Stage 1, functions) · Difficulty 1/5 · ~15 min

## Overview

Students meet decision-making in code: for each item, compare two pricing
options, pick the cheaper, and add it to a running total — the everyday logic
shops and services use to keep costs down.

## Primary Learning Objective

For each item, charge the cheaper of two pricing options and accumulate a running
total.

## Concepts Reinforced

- Variables and assignment
- Integer arithmetic
- `for` loops over a list
- `if` / `else` conditionals
- The accumulator pattern

## Prerequisites

basic Python (variables, loops, conditionals)

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Parking-Garage | Hourly vs flat parking fee |
| 02 | 02-Internet-Cafe | Hourly vs day-pass computer use |

All variants are isomorphic: same concept and difficulty, different stories, for
fairness across class sections.

## Learning Progression

- Previous: None (Stage 1 entry)
- Current: Family 01 — Minimum Cost
- Next: Family 02 — Intro to OOP

## Common Student Mistakes

- Forgetting to initialize `total = 0` before the loop.
- Charging the fixed fee for every customer instead of the cheaper option.
- Returning inside the loop, which stops after the first customer.
- Confusing the order of the arguments when calling the function.

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Round 2 (2026-08).

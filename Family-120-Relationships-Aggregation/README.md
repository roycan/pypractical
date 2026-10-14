# Family 12 — Relationships IV (Aggregation)

> SG 7 · Difficulty 3/5 · ~20 min

## Overview

Students learn aggregation: a whole object holds a list of part objects, but the
parts are created outside and passed in. The parts can exist independently of the
whole — unlike composition, the whole does not create its parts.

## Primary Learning Objective

Aggregation: a whole holds parts that are created outside and passed in.

## Concepts Reinforced

- Object relationships
- Aggregation (a "has-a" relationship where parts live independently)
- Whole-part relationship
- Classes and objects
- Lists as instance state
- Loops over a collection

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Computer-Peripherals | Keyboard, mouse, and other devices |

## Learning Progression

- Previous: Family 11 — Relationships III (Dependency)
- Current: Family 12 — Relationships IV (Aggregation)
- Next: Family 13 — SOLID: Single Responsibility

## Common Student Mistakes

- Creating the parts in `__init__` instead of receiving them (that's composition).
- Forgetting to initialize `self.peripherals = []` in `__init__`.
- Returning the count from `list_peripheral_names` (or vice versa).
- Not returning `False` from `remove_peripheral` when the name is not found.
- Comparing the whole object to the name instead of using `get_name()`.

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Storm exercises (2026-08).
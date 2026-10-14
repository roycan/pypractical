# Family 10 — Relationships II (Composition)

> SG 7 · Difficulty 4/5 · ~25 min

## Overview

Students learn composition: a whole object creates and owns its parts in
`__init__`, then aggregates their data — the whole/part pattern behind
flashlights, crates, and trains.

## Primary Learning Objective

Composition: a whole creates and owns its part objects, then aggregates their
data.

## Concepts Reinforced

- Composition (a whole creates and owns its parts)
- Object ownership (parts do not exist without the whole)
- Whole-part relationship
- Classes and objects
- Lists as instance state
- Loops in `__init__`

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Flashlight | Batteries inside |
| 02 | 02-Storage-Crate | Packed boxes |
| 03 | 03-Computer-Memory | Memory modules |
| 04 | 04-Passenger-Train | Train carriages |
| 05 | 05-House-Rooms | Built-in rooms |

All variants are isomorphic: same concept and difficulty, different stories, for
fairness across class sections.

## Learning Progression

- Previous: Family 09 — Relationships I (Association)
- Current: Family 10 — Relationships II (Composition)
- Next: Family 11 — Relationships III (Dependency)

## Common Student Mistakes

- Not creating the parts in `__init__` (leaving the list empty).
- Creating the list but never appending the part objects.
- Returning the count from the total method (or vice versa).
- An off-by-one error in the loop (for example `range(count + 1)`).
- Receiving parts from outside instead of building them (that's aggregation).

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Round 2 (2026-08).

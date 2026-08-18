# Family 11 — Relationships III (Dependency)

> SG 7 · Difficulty 2/5 · ~15 min

## Overview

Students learn dependency: one class uses another class only as a method
parameter, reads its data, and returns a result — without ever storing the
other class. This is the weakest relationship; the used object lives
independently.

## Primary Learning Objective

Dependency: one class uses another class as a parameter without storing it.

## Concepts Reinforced

- Object relationships
- Dependency (a "uses-a" relationship)
- Classes and objects
- Methods that accept objects as parameters
- Calling getters on a parameter
- Returning a value derived from the parameter

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Grade-Checker | Checking a student answer |

## Learning Progression

- Previous: Family 10 — Relationships II (Composition)
- Current: Family 11 — Relationships III (Dependency)
- Next: Family 12 — Relationships IV (Aggregation)

## Common Student Mistakes

- Storing the parameter in `__init__` (that would be aggregation/association,
  not dependency).
- Returning the whole `Answer` object instead of a derived value.
- Using `>` instead of `>=` at a grade boundary.
- Forgetting to return the tie result in `compare`.

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Storm exercises (2026-08).
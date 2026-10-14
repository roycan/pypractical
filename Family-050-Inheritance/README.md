# Family 05 — Inheritance

> SG 9 · Difficulty 2/5 · ~20 min

## Overview

Students write a subclass that inherits a parent's behavior and adds its own,
reusing code through `super().__init__()` — the "is-a" relationship behind real
staff, vehicle, and team hierarchies.

## Primary Learning Objective

A subclass inherits a parent's methods (`super().__init__`) and adds its own.

## Concepts Reinforced

- Inheritance
- Subclasses
- Classes and objects
- Methods
- Constructors
- `super().__init__(...)`

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Staff-Hierarchy | Employee and Manager |
| 02 | 02-Vehicle-Hierarchy | Vehicle and Motorcycle |
| 03 | 03-Team-Roster | Player and Captain |
| 04 | 04-Pet-Registry | Animal and Pet |
| 05 | 05-Animal-Bird | Animal and Bird |

All variants are isomorphic: same concept and difficulty, different stories, for
fairness across class sections.

## Learning Progression

- Previous: Family 04 — Encapsulation
- Current: Family 05 — Inheritance
- Next: Family 06 — Method Overriding

## Common Student Mistakes

- Forgetting `(Employee)` when declaring the child class.
- Forgetting to call `super().__init__(name, salary)`.
- Redefining `get_name` or `get_salary` in the child instead of inheriting them.
- Shadowing a parent attribute by hand instead of calling `super()`.

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Round 2 (2026-08).

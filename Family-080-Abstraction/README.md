# Family 08 — Abstraction

> SG 12 · Difficulty 3/5 · ~20 min

## Overview

Students learn abstraction: a base class declares an interface by raising
`NotImplementedError`, and each subclass implements its own version — the
contract pattern behind shapes, fabrics, and screen grids.

## Primary Learning Objective

A base class defines an interface (raises `NotImplementedError`); subclasses
implement it.

## Concepts Reinforced

- Abstraction (a base class declares an interface; subclasses implement it)
- Abstract methods (a method that raises `NotImplementedError`)
- Inheritance (subclasses extend the base)
- Subclasses
- Classes and objects
- `super().__init__`

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Shapes | Rectangle and Triangle |
| 02 | 02-Land-Area | Rectangular and triangular plots |
| 03 | 03-Fabric-Order | Full and half rolls |
| 04 | 04-Screen-Grid | Standard and compact grids |

All variants are isomorphic: same concept and difficulty, different stories, for
fairness across class sections.

## Learning Progression

- Previous: Family 07 — Polymorphism
- Current: Family 08 — Abstraction
- Next: Family 09 — Relationships I (Association)

## Common Student Mistakes

- Not implementing `area` in a subclass (so it inherits the `raise`).
- Forgetting `super().__init__(name)` (so `get_name` and `name` break).
- Using the wrong formula (for example, `base * height` for a rectangle).
- Integer-division mistakes in `Triangle` (using `/` instead of `//`).

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Round 2 (2026-08).

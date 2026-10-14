# Family 13 — SOLID: Single Responsibility

> SG 27 · Difficulty 4/5 · ~25 min

## Overview

Students apply the Single Responsibility Principle: one class owns the data, a
separate class owns the presentation — the separation of concerns behind clean
receipts, reports, and tags.

## Primary Learning Objective

Apply the Single Responsibility Principle: one class for data, a separate class
for presentation.

## Concepts Reinforced

- Single Responsibility Principle (SRP)
- SOLID design
- Separation of concerns
- Classes and objects
- Methods
- Passing one object to another (a dependency)

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Sale-Receipt | Sale and Receipt |
| 02 | 02-Score-Report | Score and Report |
| 03 | 03-Inventory-Tag | Stock and Tag |

All variants are isomorphic: same concept and difficulty, different stories, for
fairness across class sections.

## Learning Progression

- Previous: Family 10 — Relationships II (Composition)
- Current: Family 13 — SOLID: Single Responsibility
- Next: Round 3: Data Handling

## Common Student Mistakes

- Storing amounts in the presentation (Receipt) class.
- Formatting the summary string inside the data (Sale) class.
- Mismatched summary string (wrong spacing or punctuation).
- Computing the total inside the summary instead of calling `total()`.
- Using a comprehension instead of an explicit loop for the total.

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Round 2 (2026-08).

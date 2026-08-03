# Family 02 — Intro to OOP

> SG 3 · Difficulty 1/5 · ~15 min

## Overview

Students take their first step from procedural code to OOP: an object bundles its
own data, and a method reads that data instead of receiving it as arguments.

## Primary Learning Objective

Define a class; an object bundles its own data (the procedural-to-OOP bridge).

## Concepts Reinforced

- Defining a class
- Writing a constructor (`__init__`)
- Instance variables (state) with `self`
- Methods that read instance variables
- Objects are independent (each holds its own state)

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Product-Catalog | Shop products |
| 02 | 02-Book-Inventory | Bookstore stock |
| 03 | 03-Ticket-Sales | Event tickets |
| 04 | 04-Seed-Order | Garden seeds |

All variants are isomorphic: same concept and difficulty, different stories, for
fairness across class sections.

## Learning Progression

- Previous: Family 01 — Minimum Cost
- Current: Family 02 — Intro to OOP
- Next: Family 03 — Classes and Objects

## Common Student Mistakes

- Forgetting `self.` when creating or reading instance variables.
- Storing parameters in local variables instead of `self.name`, `self.price`.
- Treating a method like a function that takes arguments instead of using `self`.
- Returning a value from `__init__`.
- Making two objects accidentally share the same variable.

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Round 2 (2026-08).

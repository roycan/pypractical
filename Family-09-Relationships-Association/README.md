# Family 09 — Relationships I (Association)

> SG 6 · Difficulty 3/5 · ~20 min

## Overview

Students model a one-to-many association: a container object holds a list of items
and can count them or find one by a key — the structure behind libraries,
classrooms, and playlists.

## Primary Learning Objective

A one-to-many association: a container holds many items and can find one by key.

## Concepts Reinforced

- Object relationships
- Association (a "has-a" relationship)
- One-to-many multiplicity (one container, many items)
- Classes and objects
- Lists as instance state
- Methods that loop over a collection

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Library | Books on shelves |
| 02 | 02-Classroom | Enrolled students |
| 03 | 03-Playlist | Saved songs |
| 04 | 04-Team-Roster | Team players |

All variants are isomorphic: same concept and difficulty, different stories, for
fairness across class sections.

## Learning Progression

- Previous: Family 08 — Abstraction
- Current: Family 09 — Relationships I (Association)
- Next: Family 10 — Relationships II (Composition)

## Common Student Mistakes

- Returning the count instead of the item object from the find method.
- Forgetting to return `None` after the loop.
- Comparing the whole object to the key instead of using its getter.
- Returning too early inside the loop (returning on a non-match).
- Not initializing `self.items = []` in `__init__`, or sharing one list.

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Round 2 (2026-08).

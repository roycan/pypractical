# Family 09 — Relationships I (Association)

> SG 6 · Difficulty 3/5 · ~20 min

## Overview

Students model association at several multiplicities: a basic has-a link, a
one-to-one link, a one-to-many container, and a many-to-many link where both
sides hold lists — the structure behind lockers, ID cards, libraries, clubs, and
enrollments.

## Primary Learning Objective

Association: one object holds a reference to another, at varying multiplicities.

## Concepts Reinforced

- Object relationships
- Association (a "has-a" relationship)
- Basic has-a, one-to-one, one-to-many, and many-to-many multiplicities
- Classes and objects
- A single object reference or a list as instance state
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
| 05 | 05-Student-Locker | Student and locker |
| 06 | 06-Person-ID | Person and ID card |
| 07 | 07-Student-Club | Student and clubs |
| 08 | 08-Student-Subject | Student and subjects |

Problems 01–04 are isomorphic (one-to-many). Problems 05–08 cover basic has-a,
one-to-one, and many-to-many multiplicities for a complete association
progression.

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

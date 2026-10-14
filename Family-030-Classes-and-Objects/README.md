# Family 03 — Classes and Objects

> SG 4-5 · Difficulty 2/5 · ~20 min

## Overview

Students design classes with attributes and methods that cooperate, then connect
them through a provided helper — the way real objects in a booking or scheduling
system work together.

## Primary Learning Objective

Design classes with attributes and methods that collaborate through a provided
helper.

## Concepts Reinforced

- Defining a class
- Writing a constructor (`__init__`)
- Instance variables (state)
- Methods that read and update state
- Objects working together

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-TV-Recorder | TV programs and recorders |
| 02 | 02-Meeting-Room-Scheduler | Meetings and rooms |
| 03 | 03-Interview-Scheduler | Interviews and interviewers |
| 04 | 04-Studio-Booking | Sessions and studios |

All variants are isomorphic: same concept and difficulty, different stories, for
fairness across class sections.

## Learning Progression

- Previous: Family 02 — Intro to OOP
- Current: Family 03 — Classes and Objects
- Next: Family 04 — Encapsulation

## Common Student Mistakes

- Forgetting `self.` when creating or reading instance variables.
- Storing parameters in local variables instead of `self.start`, `self.end`.
- Not initializing `available_at` to `0` or `programs` to `[]`.
- Returning a value from `record` (it should only update state).
- Trying to modify the provided helper function.

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Round 2 (2026-08).

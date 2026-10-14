# Family 06 — Method Overriding

> SG 10 · Difficulty 3/5 · ~20 min

## Overview

Students override a parent method in a subclass so the same method name produces
different behavior — the real-world pattern where an express or premium service
charges by its own rule.

## Primary Learning Objective

A subclass overrides a parent method with its own behavior.

## Concepts Reinforced

- Method overriding
- Inheritance
- Subclasses
- Classes and objects
- Methods

## Prerequisites

the previous family

## Assessment Variants

| # | Problem | Story |
|---|---|---|
| 01 | 01-Shipping-Cost | Parcel and ExpressParcel |
| 02 | 02-Parking-Fee | Vehicle and Truck |
| 03 | 03-Ticket-Price | Ticket and FirstClass |
| 04 | 04-Rental-Cost | Tool and PowerTool |

All variants are isomorphic: same concept and difficulty, different stories, for
fairness across class sections.

## Learning Progression

- Previous: Family 05 — Inheritance
- Current: Family 06 — Method Overriding
- Next: Family 07 — Polymorphism

## Common Student Mistakes

- Forgetting `super().__init__(name, weight)`, so the child has no data.
- Giving the override a different method name, so it does not actually override.
- Calling the parent's method (`super().shipping()`) instead of replacing it.
- Forgetting `self` in the method definition.
- Trying to modify the provided parent class.

## Automatic Assessment

Each problem ships a `tests.py` (equal-weight, deterministic). Run any suite with
`python3 -m unittest tests` from inside the problem folder. A student's score is
the percentage of passing tests.

## Revision History

- v1.0 — Round 2 (2026-08).

# Round 2 — OOP Families Plan

> Scale the full OOP curriculum into auto-gradable assessment families, built in
> dependency order. Family numbers mirror the teaching/dependency order. Per
> [`06-WORKFLOW.md`](../06-WORKFLOW.md): *"whenever there is a conflict between speed
> and quality, we choose quality."*

## Purpose

Round 2 turns the two Round-1 reference problems into a complete OOP assessment
bank covering the dependency chain SG 3 -> 4 -> 5 -> 8 -> 9 -> 10 -> 11 -> 12 -> 6
-> 7 -> 27. Each problem ships the 6 standard deliverables; each family has ~3-4
isomorphic variants (same concept and difficulty, different stories) for fairness
across class sections.

## Renumbering (applied at the start of Round 2)

Family numbers now mirror the teaching/dependency order. The Round-1 TV Recorder
moved from `Family-02-Intro-OOP` to `Family-03-Classes-and-Objects`; the
`Family-02-Intro-OOP` folder was repurposed for SG 3 (Introduction to OOP), where
the name fits even better.

## Family to topic mapping (final)

| # | Folder | SG | Title | Primary concept | Difficulty | Problems |
|---|---|---|---|---|---|---|
| 1 | Family-01-Minimum-Cost | - | Minimum Cost (functions) | loop + conditional accumulator | 1/5 | 1 |
| 2 | Family-02-Intro-OOP | 3 | Introduction to OOP | define a class; objects bundle data | 1/5 | 4 |
| 3 | Family-03-Classes-and-Objects | 4-5 | Classes and Objects | class, __init__, attributes, methods, collaboration via a helper | 2/5 | 4 |
| 4 | Family-04-Encapsulation | 8 | Encapsulation | private attrs, accessors, validating mutators | 2/5 | 4 |
| 5 | Family-05-Inheritance | 9 | Inheritance | subclass extends a parent (super().__init__) | 2/5 | 4 |
| 6 | Family-06-Method-Overriding | 10 | Method Overriding | subclass overrides a parent method | 3/5 | 4 |
| 7 | Family-07-Polymorphism | 11 | Polymorphism | same method on a mixed list of object types | 3/5 | 4 |
| 8 | Family-08-Abstraction | 12 | Abstraction | abstract base (raises NotImplementedError); subclasses implement | 3/5 | 4 |
| 9 | Family-09-Relationships-Association | 6 | Relationships I | one-to-many association (container has many items) | 3/5 | 4 |
| 10 | Family-10-Relationships-Composition | 7 | Relationships II | composition (whole creates and owns its parts) | 4/5 | 4 |
| 13 | Family-13-SOLID-Single-Responsibility | 27 | SOLID: Single Responsibility | split data handling from presentation | 4/5 | 3 |

## Conventions locked this round

- `tests.py` ends with the `__main__` guard **commented out** (LMS compatibility).
- Verify with **`python3 -m unittest tests`** run from inside the problem folder.
- Every Round-1 hard rule carries over: SPEC-005 class structure; Google-style
  docstrings; no type hints; no `pass` (use the SPEC-005 placeholder table); one
  primary concept per problem; hidden tests add no new requirements; explicit
  loops (no list comprehensions); provided classes/helpers marked DO NOT MODIFY.
- Isomorphic siblings within a family reuse the same structure and difficulty,
  and (where arithmetic is multiplication or integer division) the same numeric
  test values with domain nouns swapped.

## Definition of Done (Round 2) - MET

1. All 11 families built in dependency order with ~3-4 isomorphic problems each.
2. Every problem ships 6 files: `problem.md`, `starter.py`, `solution.py`,
   `tests.py`, `teacher_notes.md`, `metadata.yml`.
3. `python3 -m unittest tests` is green for every problem (full-bank regression).
4. Every expected value independently verified (by execution + manual arithmetic).
5. The `examples/` legacy snippets are left untouched; canonical content lives in
   the `Family-NN/` folders.

## Outcome (COMPLETE - 2026-08-03)

- **40 problems** (1 function reference + 39 OOP), **240 files**, **473 tests**.
- Full-bank regression: **40/40 folders OK, 0 failures, 473 tests pass**.

| Family | Problems | Tests each |
|---|---|---|
| Family-01 | 1 | 12 |
| Family-02 (SG 3) | 4 | 12 |
| Family-03 (SG 4-5) | 4 | 14 |
| Family-04 (SG 8) | 4 | 13 |
| Family-05 (SG 9) | 4 | 11 |
| Family-06 (SG 10) | 4 | 11 |
| Family-07 (SG 11) | 4 | 12 |
| Family-08 (SG 12) | 4 | 12 |
| Family-09 (SG 6) | 4 | 11 |
| Family-10 (SG 7) | 4 | 11 |
| Family-13 (SG 27) | 3 | 11 |

## Notes for Round 3

Data handling (SG 18 text files -> 19 analysis -> 20 JSON) will need a file-I/O
fixture pattern and is out of scope for Round 2.

# Family 055 — Encapsulation and Inheritance (Integration)

> SG 8 + SG 9 · Difficulty 2/5 · ~15 minutes · Practical-exam integration family

## Overview

This family is the practical-exam integration family: one problem assesses two
previously taught ideas together. Students write a single child class that
reuses a provided parent through `super().__init__(...)` (inheritance) and
protects its own data with a validated, protected attribute (encapsulation).
The parent class is provided and complete; the exam is the child.

## Primary Learning Objective

Apply inheritance and encapsulation together in one class: reuse a parent with
`super().__init__(...)` and validate before storing in a protected attribute.

## Concepts Reinforced

- Inheritance and subclasses (`class Book(Publication):`)
- `super().__init__(...)`
- Encapsulation with a protected attribute (`_number_of_pages`)
- Input validation before storing (reject `<= 0`)
- Getters (accessors) via the `@property` decorator
- Setters via the `@<name>.setter` decorator

## Prerequisites

- Family 040 — Encapsulation
- Family 050 — Inheritance

## Estimated Classroom Time

- Reading the problem: 2–3 minutes
- Coding: 8–15 minutes
- Testing: 3–5 minutes

Total: approximately **10–25 minutes** (timed practical exam).

## Difficulty

Beginner+

## Assessment Type

Independent Practical (timed exam covering two topics in one problem).

## Assessment Philosophy

Class-time pressure often forces two topics into one exam. This family exists
so that combination is deliberate rather than accidental: the skeleton is
identical across variants, the scope is fixed (one child class, five tasks),
and the test suite is balanced 5 inheritance / 6 encapsulation / 1 integration
/ 1 hidden, so neither concept dominates the score. CURRICULUM.md notes that
some assessments "provide opportunities to integrate multiple ideas" — this is
that assessment, used after both single-concept families are taught.

## Assessment Variants

| # | Problem | Story | Validated field | Kind |
|---|---|---|---|---|
| 01 | 01-Library-Book | School library books | `number_of_pages` | Exam variant |
| 02 | 02-Video-Game-Edition | Game store deluxe editions | `bonus_levels` | Exam variant |
| 03 | 03-Streaming-Account | Streaming premium accounts | `max_screens` | Exam variant |
| 04 | 04-Sports-Captain | Sports club captains | `trophies_won` | Exam variant |
| 05 | 05-Race-Car | Race car top speeds | `top_speed` | Practice extension |

Variants 01–04 are isomorphic: identical skeleton and difficulty, different
stories, for fairness across exam sections. Variant **05-Race-Car** is a
deliberately **NON-isomorphic practice extension** — not an exam-equivalent
variant. Its validation rule references parent state
(`top_speed <= self.max_speed`), so inheritance and encapsulation interlock and
a solution pattern-matched from 01–04 will not fit. Its invalid-value fallback
is the parent's `max_speed`, not the `0` placeholder used by 01–04.

## Learning Progression

- Previous: Family 050 — Inheritance
- Current: Family 055 — Encapsulation and Inheritance (Integration)
- Next: Family 060 — Method Overriding

## Common Student Mistakes

- Forgetting `(Publication)` when declaring the child class.
- Forgetting to call `super().__init__(title, author)`.
- Storing a public attribute instead of the protected `_number_of_pages`.
- Writing `self.<name> = value` inside the setter, which calls the setter again
  and raises `RecursionError` (it must be `self._<name>`).
- Forgetting the `@<name>.setter` block, so `__init__`'s assignment raises
  `AttributeError: can't set attribute`.
- Checking only `< 0`, letting zero slip through (`<= 0` is required).
- Printing the warning but forgetting the `0` placeholder fallback.
- Redefining `display_info()` in the child — not required; the parent's method
  is inherited and reused unchanged.

## Teaching Notes

Emphasize the division of labor: the parent owns the shared fields and the
shared `display_info()`; the child only adds its own validated field. The
`0` fallback is a documented placeholder meaning "not recorded", never a valid
count — this resolves the "zero is invalid yet stored" trap deliberately. The
demo in `solution.py` is behind a main guard so it never interferes with the
auto-grading.

## Automatic Assessment

Each problem ships a `tests.py` with 13 equal-weight deterministic tests. A
student's score is the percentage of passing tests. The repo-level gate
`python3 tools/verify.py family <problem-dir>` additionally runs a
broken-solution matrix: five classic mistakes (no parent, no `super()`, no
`@property`, a non-validating setter, and a `< 0` check) are injected into a
temp copy of the solution, and each must fail the test that guards its concept —
proving the tests grade what they claim.

## Future Extensions

- Add a validating setter (`set_number_of_pages`) and test post-construction
  updates (extends toward the full Family 040 pattern).
- Add method overriding so `display_info()` includes the child's field
  (moves into Family 060 territory).
- Build a list of mixed publications and report totals (polymorphism preview).

## Revision History

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-14 | Initial release (4 variants, gate-verified) |
| 1.1 | 2026-10-20 | Added 05-Race-Car: a deliberate NON-isomorphic practice extension whose relational validation interlocks inheritance + encapsulation; `tools/verify.py` gains per-spec mutation selection and a `relational_boundary` mutation |
| 1.2 | 2026-10-21 | Variants 01–04 now expose the protected value through a `@property` getter and a `@<name>.setter`, with `__init__` routing through the setter (SG 8's own pattern). Adds one post-construction test per variant (12 → 13) and two matrix mutations (`no_property`, `setter_no_validate`). This reverses plan decision D2 ("no setters") to align the exam with SG 8's graded `@property` requirement; 05-Race-Car keeps its plain getter as the non-isomorphic extension |

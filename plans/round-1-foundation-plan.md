# Round 1 — Foundation Plan

> Spec-compliant, runnable references for the function path **and** the OOP path,
> plus the class-based spec the OOP course needs.

## Purpose

Round 1 produces **no assessment volume**. It locks the quality bar and the two
template patterns the entire curriculum will reuse. Per [`06-WORKFLOW.md`](../06-WORKFLOW.md),
*"whenever there is a conflict between speed and quality, we choose quality."*

## Scope (in)

- One **class-based spec addendum** (extends [`40-problem-markdown-spec.md`](../40-problem-markdown-spec.md)
  and [`41-python-template-spec.md`](../41-python-template-spec.md) to cover classes).
- One **function reference problem** — upgrade parking-garage to full compliance.
- One **OOP reference problem** — upgrade tv-recording to full compliance.
- **Empirical verification** of every expected value by executing the code.

## Scope (out — deferred)

- Family-level `README.md` ([`20-FAMILY_TEMPLATE.md`](../20-FAMILY_TEMPLATE.md)) — added
  when a family has multiple problems.
- Additional problems, isomorphic variants, and all other topics (Rounds 2–3).
- `metadata.yml` — see T5 (schema undefined; proposed simplification below).

## Proposed locations

| Artifact | Path |
|---|---|
| OOP spec addendum | `43-oop-class-spec.md` (SPEC-005, extends 40/41/42) |
| Function reference | `Family-01-Minimum-Cost/01-Parking-Garage/` |
| OOP reference | `Family-02-Intro-OOP/01-TV-Recorder/` |

Each problem folder holds: `problem.md`, `starter.py`, `solution.py`, `tests.py`,
`teacher_notes.md` (and `metadata.yml` only if T5 is kept).

## Scoring legend

- **Feasibility** — can it technically be done here (write files, run Python).
- **Confidence** — likelihood it is correct/approved with **no rework**.
- **Status** — Clear (both > 90) · Watch (one = 90) · Review (either ≤ 90).

## Task breakdown

| # | Task | Feasibility | Confidence | Status |
|---|---|---|---|---|
| T1 | Draft OOP class-based spec addendum (`43-oop-class-spec.md`) | 95% | 75% | Review |
| T2 | Function reference — upgrade parking-garage (problem/starter/solution/tests) | 97% | 93% | Clear |
| T3 | OOP reference — upgrade tv-recording (problem/starter/solution/tests) | 95% | 84% | Review |
| T4 | Verify expected values by executing solution + tests (both problems) | 99% | 96% | Clear |
| T5 | `metadata.yml` for both problems | 92% | 68% | Review |
| T6 | `teacher_notes.md` for both problems | 95% | 90% | Watch |
| T7 | Full regression run + combined spec-checklist sign-off | 97% | 90% | Watch |

## Tasks requiring review (≤ 90%)

### T1 — OOP class-based spec addendum (confidence 75%)

Genuine design decisions, not just writing: the class-based `problem.md` skeleton
(what replaces `## Function Specification / ### Parameters / ### Returns`?), and the
**placeholder rule** for OOP methods — [`41-python-template-spec.md`](../41-python-template-spec.md)
forbids `pass` and says use `return`, but void mutator methods (e.g. `record()`)
have no return value, and `__init__` must set attributes without leaking structure.

**Simplification:** keep it minimal and concrete — one proposed skeleton + an
explicit placeholder table (value method → `return None`/`0`/`[]`/`False`; void
method → bare `return`). Cover only what tv-recording and the near-term OOP
families need. Get sign-off **before** applying to T3. Raises confidence to ~92%.

### T3 — tv-recording upgrade (confidence 84%)

Risk is almost entirely the novel class-markdown mapping from T1. Four methods
need the correct placeholder strategy; tests must gain the missing import + guard.

**Simplification:** gate on T1 sign-off. Once the class spec is agreed, T3 becomes
mechanical and confidence rises to ~92%.

### T5 — metadata.yml (confidence 68%)

[`inceptions/context.md`](../inceptions/context.md) flags SPEC-003 as **missing**
(sequence jumps 002 → 004). There is no agreed `.yml` schema. We know the *fields*
from [`30-PROBLEM_TEMPLATE.md`](../30-PROBLEM_TEMPLATE.md) section 7, but not the
file format — so this is a judgment call that could need rework later.

**Simplification (recommended):** **defer** `metadata.yml`. Round 1 delivers five
files per problem. Define the schema in a later round once a few real problems
reveal which metadata is actually useful. This is the single biggest confidence win.

**Alternative:** derive a minimal schema now from section 7 and include it.

### Watch items (exactly 90)

- **T6** teacher_notes — use the fixed section list from
  [`30-PROBLEM_TEMPLATE.md`](../30-PROBLEM_TEMPLATE.md); low risk.
- **T7** regression + checklist — use the 14-item checklist from
  [`30-PROBLEM_TEMPLATE.md`](../30-PROBLEM_TEMPLATE.md) and the four-test contract
  from [`07-TESTING_GUIDE.md`](../07-TESTING_GUIDE.md); tick each line.

## Strengths that de-risk Round 1

- **We can execute code.** T4 satisfies the mandatory *"verify every expected
  value"* rule ([`07-TESTING_GUIDE.md`](../07-TESTING_GUIDE.md)) empirically rather
  than by mental math — the strongest available verification.
- Both example problems already have **correct, verified** expected values, so T2/T3
  are upgrades, not new derivations.

## Definition of Done (Round 1)

1. `43-oop-class-spec.md` exists and you have signed off on it.
2. Both reference problems live in their canonical `Family-NN/NN-Name/` folders.
3. `python3 tests.py` exits green for both, run against their `solution.py`.
4. Both pass the combined spec checklist (SPEC-001/002/004 + addendum + STD-001/002).
5. `teacher_notes.md` present for both (and `metadata.yml` if T5 is kept).

## Assumptions

- Python 3.10+ is available to execute tests (per [`inceptions/context.md`](../inceptions/context.md)).
- Specs are authoritative over the legacy `examples/` (we upgrade, not relax specs).
- Existing `examples/` files are left in place as legacy; compliant copies go to the
  `Family-NN/` structure.

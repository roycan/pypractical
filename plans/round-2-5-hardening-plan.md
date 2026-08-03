# Round 2.5 — Hardening Plan

> Lock the conventions, tooling, and documentation surfaced during Round 2; mark
> the classroom-tested problems stable; and retire the legacy `examples/` folder.
> Per [`06-WORKFLOW.md`](../06-WORKFLOW.md): *"whenever there is a conflict between
> speed and quality, we choose quality."*

## Scope (in)

- T1 — Reconcile SPEC-004 ([`42-unittest-spec.md`](../42-unittest-spec.md)) with the
  commented-out `__main__` guard and the `python3 -m unittest tests` verification
  command; sync [`07-TESTING_GUIDE.md`](../07-TESTING_GUIDE.md) and
  [`inceptions/context.md`](../inceptions/context.md) section 9.
- T2 — A best-effort worked-example linter: run `solution.py` and diff its stdout
  against the `## Example` Output block in `problem.md` (normalized; report-only).
- T3 — A one-command full-bank runner (`run_all_tests.sh`) plus a `.gitignore`
  for `__pycache__`.
- T4 — A concise per-family `README.md` for all 11 families, grounded in each
  family's existing `teacher_notes.md`, following [`20-FAMILY_TEMPLATE.md`](../20-FAMILY_TEMPLATE.md).
- T5 — Formalize the `metadata.yml` schema as SPEC-003 (codify the fields already
  used by all 40 problems, plus a `classroom_tested` field).
- T6 — Upgrade Internet-Cafe to a canonical
  `Family-01-Minimum-Cost/02-Internet-Cafe` problem (Round-1-style 6-file
  upgrade), then mark Parking-Garage and Internet-Cafe v1.0 stable.
- T7 — Remove the legacy `examples/` folder entirely (after T6).
- T8 — Record classroom-tested status via a `classroom_tested` metadata field.

## Decisions locked this session

- Internet-Cafe is upgraded to a canonical `Family-01` problem (same upgrade
  Parking-Garage received in Round 1). Both Parking-Garage and Internet-Cafe are
  then marked v1.0 stable, and `examples/` is removed entirely.
- `tests.py` guards stay commented out (LMS); canonical verification is
  `python3 -m unittest tests`.
- `metadata.yml` gains a `classroom_tested` field, documented in SPEC-003.

## Scoring legend

- **Feasibility** — can it be done here (write files, run Python).
- **Confidence** — likelihood it is correct/approved with no rework.
- **Status** — Clear (both > 90) - Watch (one = 90) - Review (either <= 90).

## Task scorecard (post-simplification)

| # | Task | Feas. % | Conf. % | Status |
|---|---|---|---|---|
| T1 | SPEC-004 + testing guide + context.md reconciliation | 99 | 96 | Clear |
| T2 | Worked-example linter (best-effort, normalized diff) | 90 | 92 | Clear |
| T3 | `run_all_tests.sh` + `.gitignore` | 98 | 96 | Clear |
| T4 | 11 family READMEs (concise, grounded in teacher_notes) | 95 | 92 | Clear |
| T5 | SPEC-003 metadata schema (codify existing + classroom_tested) | 95 | 93 | Clear |
| T6 | Upgrade Internet-Cafe + mark both stable | 95 | 90 | Watch |
| T7 | Remove `examples/` (after T6) | 99 | 95 | Clear |
| T8 | `classroom_tested` metadata field | 98 | 93 | Clear |

## Definition of Done

1. `examples/` removed; Internet-Cafe canonical and green.
2. SPEC-003 and SPEC-004 reflect current reality.
3. `run_all_tests.sh` passes (full bank green, including Internet-Cafe).
4. Worked-example linter runs (clean or report-only).
5. 11 family `README.md` files present.
6. Parking-Garage and Internet-Cafe flagged `classroom_tested` / stable.

## Outcome (COMPLETE — 2026-08-03)

All eight tasks delivered and verified.

| # | Task | Result |
|---|---|---|
| T1 | SPEC-004 + testing guide + context.md reconciliation | Done — commented-out guard + `python3 -m unittest tests` now canonical |
| T2 | Worked-example linter | Done — `tools/check_examples.py`; 41/41 PASS (0 mismatch) |
| T3 | Full-bank runner + `.gitignore` | Done — `run_all_tests.sh` (41 OK, 485 tests) + `.gitignore` |
| T4 | 11 family READMEs | Done — one concise README per family |
| T5 | SPEC-003 metadata schema | Done — `44-metadata-spec.md` |
| T6 | Upgrade Internet-Cafe + mark stable | Done — `Family-01/02-Internet-Cafe`; both Minimum-Cost problems `classroom_tested: true` |
| T7 | Remove `examples/` | Done — removed (superseded by Family-NN) |
| T8 | `classroom_tested` field | Done — all 41 `metadata.yml` carry it (2 true, 39 false) |

Bonus fix: corrected a pre-existing YAML parse error in
`Family-04-Encapsulation/04-Water-Tank/metadata.yml`; all 41 metadata now parse.

Final state: 41 problems, 485 tests, 0 failures; every worked example verified
honest by the linter; specs, runner, linter, family READMEs, and the metadata
schema are all in place.

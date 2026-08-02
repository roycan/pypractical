# Changelog

All notable changes to PyPractical are documented in this file.

PyPractical follows the principle that educational resources improve through continuous refinement.

Changes are recorded not only for technical updates, but also for improvements in pedagogy, assessment quality, classroom experience, and contributor feedback.

---

# Changelog Categories

Changes should be grouped using the following headings whenever appropriate.

## Added

New assessments, assessment families, documentation, templates, or features.

---

## Improved

Better explanations, clearer stories, stronger hints, improved teacher notes, or refinements that enhance the learning experience.

---

## Fixed

Corrections to problems, examples, teacher solutions, unit tests, expected outputs, or documentation.

---

## Verified

Items that have been independently reviewed or classroom-tested.

Examples include:

* verified expected outputs
* classroom validation
* reviewed assessment timing
* confirmed grading accuracy

Verification is considered an important milestone in the life of an assessment.

---

## Deprecated

Assessments or materials that should no longer be used.

Whenever practical, explain the preferred replacement.

---

## Removed

Material intentionally removed from the project.

Document the reason whenever possible.

---

# Versioning Philosophy

PyPractical values educational stability.

Minor improvements should not require teachers to redesign their courses.

Version numbers should reflect meaningful improvements rather than frequent cosmetic changes.

Suggested format:

Major.Minor.Patch

Example:

1.2.3

where:

Major

Significant curriculum or assessment changes.

Minor

New assessment families or important educational improvements.

Patch

Corrections, clarifications, typo fixes, and verified expected outputs.

---

# Release Template

## Version X.Y.Z

Release Date:

YYYY-MM-DD

### Added

*

### Improved

*

### Fixed

*

### Verified

*

### Deprecated

*

### Removed

*

---

# Actual Releases

## Version 0.1.0 — Round 1 Foundation

Release Date:

2026-08-02

### Added

* SPEC-005 class-based (OOP) problem specification (`43-oop-class-spec.md`), extending
  SPEC-001/SPEC-002 to cover classes, attributes, and methods.
* Canonical function reference problem — Parking Garage Daily Report
  (`Family-01-Minimum-Cost/01-Parking-Garage/`), 6 deliverables.
* Canonical OOP reference problem — TV Recorder Scheduler
  (`Family-02-Intro-OOP/01-TV-Recorder/`), 6 deliverables.
* `metadata.yml` schema established (title, family, difficulty, estimated_time,
  language, concepts, grading, version).
* Round 1 plan with per-task feasibility/confidence scorecard
  (`plans/round-1-foundation-plan.md`).

### Improved

* `41-python-template-spec.md` (SPEC-002): docstring standard set to Google style
  bank-wide.
* OOP placeholder rule documented in SPEC-005 (`__init__` and void methods use a bare
  `return`; value methods use `return False`/`0`/`[]`/`""`/`None`).

### Verified

* All 26 unit tests pass by execution (12 parking-garage + 14 tv-recorder).
* Every expected value independently verified by hand and by running the suites.

---

# Example Release

## Version 1.0.0

Initial public release.

### Added

* Project philosophy
* Design principles
* Curriculum framework
* Assessment templates
* First assessment family
* Automatic grading support

### Verified

* Teacher reference solutions
* Expected outputs
* Classroom timing estimates

---

## Version 1.1.0

### Added

* Internet Café assessment
* Theme Park assessment

### Improved

* Clearer hints for beginners
* Better teacher notes
* Improved workflow documentation

### Fixed

* Corrected expected output in Parking Garage assessment
* Improved wording in starter code documentation

### Verified

* Classroom tested in three Grade 9 sections
* Hidden tests reviewed

---

# Classroom Feedback

Some changes originate from classroom experience rather than code review.

Whenever practical, record observations such as:

* students consistently misunderstood an instruction
* completion time differed from expectations
* a story proved particularly engaging
* a hint revealed too much
* a common misconception suggested a better explanation

Teaching experience is one of the most valuable sources of improvement.

---

# Contributor Recognition

Educational improvement is a collaborative effort.

Whenever practical, acknowledge contributors whose ideas significantly improved an assessment, workflow, or document.

Recognition encourages a healthy and generous community.

---

# A Living History

A changelog is more than a list of edits.

It is the story of how PyPractical grows.

Every improvement reflects a lesson learned from a teacher, a student, or a contributor.

Every version represents another step toward creating assessments that teachers can trust and students can enjoy.

We preserve that history because future contributors deserve to understand not only what changed—but why it changed.

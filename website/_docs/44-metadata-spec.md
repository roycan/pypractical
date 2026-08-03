# Metadata Specification

**Document ID:** SPEC-003

**Status:** Draft

**Applies To:** Every `metadata.yml` file in PyPractical

---

# Purpose

This specification defines the required fields and format for every problem's
`metadata.yml`. Consistent metadata lets teachers and tools quickly read a
problem's objectives, difficulty, and grading model.

---

# Required Fields

Every `metadata.yml` must contain these fields, in this order:

- `title` (string): The problem's display title.
- `family` (string): The family title (e.g. "Minimum Cost", "Encapsulation").
- `difficulty` (string): Difficulty as `N/5` (e.g. "2/5").
- `estimated_time` (string): Classroom time estimate (e.g. "20 minutes").
- `language` (string): The programming language (always "Python" today).
- `concepts` (list of strings): Concepts the assessment teaches or reinforces.
- `grading` (string): Always "automatic unittest".
- `classroom_tested` (boolean): `true` if piloted in a real classroom, else `false`.
- `version` (string): Semantic version of this problem (e.g. "1.0").

---

# Format Rules

- Plain YAML, one field per line, a blank line between top-level fields.
- `concepts` is a list using a `- ` bullet per item.
- Booleans use lowercase `true` / `false`.

---

# Example

```yaml
title: Parking Garage Daily Report

family: Minimum Cost

difficulty: 1/5

estimated_time: 15 minutes

language: Python

concepts:
  - variables
  - arithmetic
  - if
  - loops
  - accumulators
  - functions

grading: automatic unittest

classroom_tested: true

version: 1.0
```

---

# Validation Checklist

- All required fields present and in order.
- difficulty is `N/5`.
- concepts is a non-empty list.
- grading is "automatic unittest".
- classroom_tested is a boolean.

---

# Compliance

A `metadata.yml` is SPEC-003 compliant only if it satisfies every requirement
above.

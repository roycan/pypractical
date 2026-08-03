# Unit Test Specification

**Document ID:** SPEC-004

**Status:** Draft

**Applies To:** All Python `unittest` files in PyPractical

---

# Purpose

This specification defines the required structure for all automated unit tests used by PyPractical assessments.

Unit tests exist to verify student solutions fairly, consistently, and automatically.

Every assessment published in PyPractical must include a unit test suite that complies with this specification.

---

# Guiding Principles

Every unit test should be:

* fair
* deterministic
* readable
* maintainable
* independent
* beginner-friendly

The goal is to evaluate **observable behavior**, not implementation details.

Students should be free to write different correct solutions.

---

# Testing Philosophy

PyPractical evaluates **what the student's program does**, not **how it is written**.

Correct solutions should pass regardless of whether they use:

* loops
* helper functions
* different variable names
* different control structures

Unless a lesson explicitly requires a specific programming construct, implementation choices should not affect grading.

---

# File Structure

Every unit test file should follow this structure.

```text
Imports

Student Solution Import

Test Class

Individual Test Methods

Main Guard
```

The order should remain consistent across every assessment.

---

# Required Imports

Every unit test should import:

```python
import unittest
```

and the student's solution.

Example

```python
try:
    from solution import calculate_daily_revenue
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass
```

The `try/except` guard lets the same suite run in two places: a serverless
runner injects the student's code into the test module's namespace (the names
are already defined and `solution.py` is absent), while local `unittest`
imports `solution.py` directly.

Avoid unnecessary imports.

---

# Test Class

Every assessment contains one primary test class.

Example

```python
class TestParkingGarage(unittest.TestCase):
```

The class name should clearly identify the assessment.

---

# Test Method Naming

Every test method begins with

```text
test_
```

Examples

```python
test_single_customer()

test_empty_list()

test_large_values()

test_mixed_case()
```

Method names should describe the behavior being verified.

---

# One Behavior Per Test

Each test should verify one observable behavior.

Good

```python
test_single_customer()
```

Poor

```python
test_everything()
```

Small tests are easier to understand and debug.

---

# Assertion Style

Preferred

```python
self.assertEqual(actual, expected)
```

Use the simplest appropriate assertion.

Examples

```python
self.assertTrue(...)

self.assertFalse(...)

self.assertIsNone(...)
```

Avoid unnecessarily complex assertions.

---

# Test Categories

Every assessment should include a balanced collection of tests.

---

## Basic Tests

Simple examples.

Purpose

Verify that students understand the core requirement.

---

## Boundary Tests

Minimum and maximum valid inputs.

Examples

* smallest list
* largest values
* one element
* many elements

---

## Typical Tests

Representative classroom scenarios.

These should resemble the examples students are likely to solve manually.

---

## Mixed Tests

Combine multiple situations in one input.

Mixed tests frequently reveal logical mistakes.

---

## Hidden Tests

Hidden tests verify that students solved the published problem rather than memorized sample inputs.

Hidden tests must never introduce new requirements.

If a hidden test depends on undocumented behavior, the assessment should be corrected.

---

# Equal Weight Philosophy

Every test contributes equally whenever practical.

Reasons

* simple grading
* transparent scoring
* encourages complete solutions
* avoids subjective weighting

Each passing test represents one demonstrated behavior.

---

# Independence

Tests must not depend on previous tests.

Avoid

```python
shared_list.append(...)
```

inside one test that affects another.

Each test should create its own input data.

---

# Expected Values

Every expected value must be verified independently.

Recommended methods

* manual calculation
* teacher reference solution
* independent implementation
* peer review

Never publish an expected value that has not been verified.

---

# Randomness

Do not use random inputs.

Tests must produce identical results every time they are executed.

If randomized testing is desired during development, it should not appear in the published assessment.

---

# Performance

Performance testing is optional.

Only include performance tests when algorithmic efficiency is a published learning objective.

Most Grade 9 assessments prioritize correctness over optimization.

---

# Error Messages

Assertion failures should help teachers identify the failing behavior.

Prefer

```python
self.assertEqual(actual, expected)
```

inside a clearly named test

rather than writing custom messages for every assertion.

Good method names already communicate intent.

---

# Hidden Teacher Tests

Additional hidden tests may be used during grading.

Hidden tests should

* follow this specification
* remain deterministic
* evaluate only documented behavior

Students should never fail because of undisclosed expectations.

---

# Common Testing Mistakes

Avoid

* duplicated tests
* incorrect expected values
* implementation-specific checks
* hidden requirements
* inconsistent naming
* overly large test methods

Simple tests are easier to trust and maintain.

---

# Main Guard

By convention the main guard is included but **commented out**, because some
learning-management systems run the suite their own way:

```python

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()
```

The canonical way to run a suite is, from inside the problem folder:

```bash
python3 -m unittest tests
```

---

# Validation Checklist

Before publishing, verify

* □ Imports are correct
* □ Student solution imports successfully
* □ One primary test class
* □ Test methods follow naming convention
* □ Tests are independent
* □ Expected values verified
* □ Basic tests included
* □ Boundary tests included
* □ Mixed tests included
* □ Hidden tests documented
* □ No random behavior
* □ Tests pass using the teacher solution

---

# Compliance

A unit test suite is **SPEC-004 compliant** only if it satisfies every structural and behavioral requirement defined in this specification.

Unit tests are part of the assessment.

They deserve the same level of review, documentation, and craftsmanship as the problem statement itself.

# Testing Guide

## Why Testing Matters

Every assessment in PyPractical is a promise.

When a teacher chooses to use one of our practicals, they trust that:

* the problem is correct
* the examples are correct
* the teacher solution is correct
* the unit tests are correct
* the expected answers are correct

That trust is earned through careful testing.

Testing is therefore one of the most important parts of the assessment development process.

---

# Our Testing Philosophy

Testing exists to verify the assessment—not the student.

Before an assessment can evaluate student work, the assessment itself must be verified.

Every published assessment should give teachers confidence that it behaves exactly as described.

---

# The Four Things We Test

Every assessment contains four artifacts that require verification.

## 1. Problem Statement

Verify that:

* every instruction is clear
* no requirements contradict one another
* examples match the specification
* constraints are complete

Students should never lose points because of ambiguous wording.

---

## 2. Teacher Solution

The reference solution should:

* solve every published requirement
* use beginner-friendly Python
* prioritize readability
* pass every unit test

The teacher solution serves as the reference implementation for the assessment.

---

## 3. Unit Tests

Unit tests verify observable behavior.

They should never require implementation details.

Students should be free to write different correct solutions.

Good tests evaluate what the program does—not how it does it.

---

## 4. Expected Outputs

Every expected output must be independently verified.

Never assume a calculated answer is correct simply because it "looks right."

Whenever practical:

* calculate by hand
* verify with an independent solution
* ask another contributor to confirm

Incorrect expected values damage trust more than missing tests.

---

# Recommended Test Categories

Every assessment should include a balanced set of tests.

## Basic Cases

Simple examples that demonstrate expected behavior.

---

## Boundary Cases

Inputs at the limits of the specification.

Examples:

* minimum values
* maximum values
* empty collections
* single-item collections

---

## Typical Cases

Representative classroom examples.

These should resemble the situations students are most likely to encounter.

---

## Mixed Cases

Inputs containing several different situations in a single test.

These often reveal logical errors that simple tests cannot detect.

---

## Hidden Cases

Hidden tests verify that students solved the general problem.

Hidden tests should never introduce new requirements.

If a hidden test requires behavior that is not described in the problem statement, the assessment should be revised—not the student.

---

# Equal Weight Testing

PyPractical recommends giving every unit test equal weight whenever practical.

Each passing test demonstrates one observable behavior.

This approach:

* rewards consistent understanding
* simplifies grading
* encourages complete solutions
* provides meaningful feedback

---

# Manual Verification

Automatic tests are essential.

Manual verification is still required.

Before publishing:

* solve sample cases by hand
* verify arithmetic independently
* review every expected answer
* read the problem from a student's perspective

Automation complements human review.

It does not replace it.

---

# Classroom Validation

Real classrooms reveal problems that automated testing cannot.

Observe:

* Which instructions cause confusion?
* Which tests fail most often?
* Which mistakes appear repeatedly?
* Do students finish within the expected time?

Update assessments based on classroom observations.

Real-world feedback is part of the testing process.

---

# Regression Testing

Whenever an assessment changes:

* rerun all unit tests
* verify sample outputs
* confirm that previous functionality still works

A small wording change can accidentally affect several test cases.

Regression testing helps preserve quality over time.

---

# Common Testing Mistakes

Avoid:

* incorrect expected outputs
* duplicated test cases
* hidden requirements
* ambiguous specifications
* testing implementation details
* rewarding one specific algorithm instead of correct behavior

The best unit tests are invisible to students.

Students should feel that the tests simply confirm whether their solution works.

---

# Before Every Release

Every published assessment should satisfy this checklist.

## Problem Statement

* □ Instructions reviewed
* □ Examples verified
* □ Constraints checked

## Teacher Solution

* □ Complete
* □ Readable
* □ Passes every test

## Unit Tests

* □ Basic cases
* □ Boundary cases
* □ Mixed cases
* □ Hidden cases

## Verification

* □ Expected outputs verified independently
* □ Sample solutions checked manually
* □ Classroom observations incorporated

Only after every checklist item is complete should an assessment be considered ready for classroom use.

---

# A Lesson We Carry Forward

Every project teaches us something.

One incorrect expected value is enough to reduce confidence in an otherwise excellent assessment.

For that reason, PyPractical treats verification as an essential part of assessment engineering.

Testing is not the final step.

It is woven throughout the entire development process.

The trust teachers place in PyPractical begins with the care we invest in every published assessment.

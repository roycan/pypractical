# Workflow

## Why a Workflow?

Good educational resources rarely appear fully formed.

They are designed, reviewed, tested, used in classrooms, refined, and improved over time.

PyPractical treats assessment development as an engineering process.

Every assessment should become better through careful iteration rather than being considered "finished" after its first draft.

This workflow helps contributors build assessments that teachers can confidently use in their classrooms.

---

# The PyPractical Development Cycle

Every assessment follows the same journey.

```text
Learning Objective
        ↓
Story Design
        ↓
Problem Statement
        ↓
Starter Code
        ↓
Teacher Solution
        ↓
Unit Tests
        ↓
Manual Verification
        ↓
Classroom Testing
        ↓
Revision
        ↓
Publication
```

Each stage improves the quality of the assessment.

Skipping stages often leads to weaker assessments.

---

# Step 1 — Identify the Learning Objective

Every assessment begins with a single question:

> **What should students learn from this assessment?**

Only one primary learning objective should be introduced.

Previously learned concepts may be reinforced, but they should not compete for the student's attention.

---

# Step 2 — Design an Authentic Story

Students should understand why the program exists.

Choose a scenario that feels believable.

Examples include:

* schools
* libraries
* hospitals
* businesses
* transportation
* entertainment

The story should motivate the programming problem.

It should never exist solely to force the use of a programming construct.

---

# Step 3 — Write the Problem Statement

The problem statement should answer every important question.

Students should know:

* what they are building
* what inputs they receive
* what output is expected
* any constraints
* how success will be measured

Good instructions remove uncertainty without removing challenge.

---

# Step 4 — Create the Starter Code

Starter code should reduce unnecessary setup.

It should provide:

* function signature
* docstrings
* TODO comments
* parameter descriptions
* return description

Starter code should encourage students to think rather than simply fill in blanks.

---

# Step 5 — Write the Teacher Solution

Before creating unit tests, implement a complete reference solution.

The teacher solution serves several purposes:

* verifies the assessment is solvable
* establishes expected behavior
* validates the unit tests
* documents the intended approach

The teacher solution should prioritize readability over cleverness.

---

# Step 6 — Create Unit Tests

Unit tests verify observable behavior.

Whenever practical, include:

* basic cases
* boundary cases
* mixed cases
* hidden cases

Unit tests should evaluate the published specification and nothing more.

---

# Step 7 — Verify Every Expected Value

This step is mandatory.

Every expected value must be independently verified.

Do not rely solely on AI-generated arithmetic.

Do not rely solely on mental calculations.

Incorrect expected values undermine trust in the assessment.

Verification is an essential quality assurance step.

---

# Step 8 — Classroom Testing

The classroom is the ultimate review environment.

Observe:

* completion time
* student questions
* common mistakes
* confusing wording
* unexpected solutions

Real classroom experience often reveals opportunities for improvement that are impossible to predict beforehand.

---

# Step 9 — Improve the Assessment

No assessment is perfect.

Revise:

* wording
* examples
* hints
* starter code
* unit tests
* teacher notes

Improvement is expected.

Version history helps preserve these refinements.

---

# Step 10 — Publish

Only publish an assessment when it is ready for classroom use.

Published assessments should include all required resources:

* problem statement
* starter code
* teacher solution
* unit tests
* teacher notes
* metadata

Teachers should be able to adopt a published assessment with confidence.

---

# Continuous Improvement

Publication is not the end of development.

Every classroom provides new insights.

PyPractical encourages contributors to revisit assessments as new ideas emerge.

Better stories.

Clearer instructions.

Stronger unit tests.

Improved teacher guidance.

Every revision benefits future classrooms.

---

# Our Quality Checklist

Before publishing, confirm that:

* □ The learning objective is clear.
* □ The story feels authentic.
* □ The instructions are complete.
* □ The starter code follows the style guide.
* □ The teacher solution is readable.
* □ The unit tests pass.
* □ Every expected value has been verified.
* □ The assessment has been reviewed.
* □ Teacher resources are complete.

If any item is incomplete, continue refining the assessment.

Quality is worth the extra effort.

---

# The Classroom Comes First

The purpose of this workflow is not to produce more assessments.

The purpose is to produce better assessments.

Whenever there is a conflict between speed and quality, we choose quality.

Every published assessment represents a promise to teachers.

That promise is worth protecting.

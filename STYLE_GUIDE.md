# Style Guide

## Why a Style Guide?

Consistency reduces cognitive load.

When every assessment follows the same structure, students spend less time learning how to read an assessment and more time solving the programming problem itself.

Likewise, teachers can quickly understand and adopt new assessments because they know where to find the information they need.

This guide exists to make every PyPractical assessment feel familiar, regardless of who wrote it.

---

# General Principles

When in doubt, choose:

* clarity over cleverness
* simplicity over complexity
* readability over brevity
* consistency over personal preference

The goal is not to showcase advanced Python techniques.

The goal is to help students learn.

---

# Writing Style

Write as if speaking to a student.

Use clear, direct language.

Prefer short sentences.

Avoid unnecessary technical vocabulary.

Whenever possible:

* explain before introducing new terms
* use familiar words
* avoid ambiguity

Students should spend their effort programming—not decoding instructions.

---

# Problem Titles

Titles should describe the scenario.

Examples:

* Parking Garage Daily Report
* Internet Café Daily Report
* Theme Park Revenue
* Library Book Tracker

Avoid generic titles such as:

* Problem 1
* Exercise
* Programming Task

Good titles help students immediately understand the context.

---

# Story Design

Stories should feel authentic.

Ask yourself:

> Could someone reasonably write software for this?

Good stories often involve:

* schools
* libraries
* hospitals
* restaurants
* transportation
* businesses
* games
* community organizations

Avoid stories that exist only to force a programming construct.

The programming concept should arise naturally from the story.

---

# Problem Structure

Every problem should use the same order.

1. Story
2. Task
3. Parameters
4. Returns
5. Example
6. Explanation
7. Hint
8. Constraints

This structure should remain consistent throughout the repository.

---

# Function Names

Function names should describe what the function accomplishes.

Prefer:

```python
calculate_daily_revenue()
find_available_room()
record_program()
```

Avoid:

```python
problem1()
task()
solution()
compute()
```

Meaningful names improve readability.

---

# Variable Names

Variable names should communicate intent.

Prefer:

```python
parking_hours
hourly_rate
students
books
reservations
```

Avoid:

```python
a
b
x
list1
temp
```

Students should learn that good software communicates through its names.

---

# Starter Code

Starter code should:

* include a docstring
* explain the parameters
* explain the return value
* include TODO comments
* avoid giving away the solution

Starter code should guide students without removing the opportunity to think.

---

# Hints

Hints should guide, not solve.

Good hints encourage students to think about the next step.

Example:

1. Loop through each customer.
2. Compute the hourly cost.
3. Compare it with the fixed fee.
4. Add the cheaper amount to the total.

Avoid writing hints that describe the complete algorithm in code-like detail.

---

# Unit Tests

Unit tests should verify behavior, not implementation.

A good test suite includes:

* simple cases
* boundary cases
* mixed cases
* hidden cases

Every expected value must be verified independently before publication.

Correctness is more important than quantity.

---

# Teacher Notes

Every assessment should include:

* learning objectives
* estimated completion time
* common mistakes
* difficulty
* pedagogical notes

Teacher notes exist to support instruction, not just grading.

---

# Formatting

Use consistent Markdown headings.

Keep line lengths reasonably short for readability.

Separate major sections with a blank line.

Use bullet lists for related items.

Use numbered lists when order matters.

Consistency helps both readers and future contributors.

---

# Python Style

Write Python that beginners can understand.

Prefer explicit code over clever shortcuts.

Avoid introducing advanced language features unless they are part of the learning objective.

Students should be able to read every reference solution after completing the lesson.

---

# Assessment Families

Problems within the same family should be isomorphic.

Equivalent problems should:

* assess the same concepts
* require similar effort
* have comparable difficulty
* use different stories
* use different variable names
* use different examples

Students in different class sections should experience assessments that are fair without being identical.

---

# A Living Guide

This style guide is not fixed.

As PyPractical grows, new lessons will emerge.

If a new convention makes assessments clearer for students or easier for teachers, we should adopt it.

Consistency serves learning—not the other way around.

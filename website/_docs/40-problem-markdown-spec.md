# Problem Markdown Specification

**Document ID:** SPEC-001

**Status:** Draft

**Applies To:** All student-facing problem statements in PyPractical

---

# Purpose

This specification defines the required Markdown structure for every student problem statement in PyPractical.

A consistent format allows:

* students to quickly recognize familiar layouts
* teachers to easily review assessments
* automated tools to generate assessments consistently
* AI assistants to create valid problems without guessing the structure

Every published assessment must follow this specification.

---

# Guiding Principles

Every problem statement should be:

* clear
* complete
* beginner-friendly
* self-contained
* consistent with every other PyPractical assessment

Students should never need to infer missing requirements.

---

# Required Section Order

Every problem must contain the following sections in this exact order.

```text
# Title

## Story

## Task

## Function Specification

### Parameters

### Returns

## Constraints

## Example

## Explanation

## Hint
```

No required section may be omitted.

Additional sections may be added only when they improve student understanding.

---

# Title

The title identifies the assessment.

Requirements:

* Short
* Descriptive
* Scenario-focused

Preferred:

```text
# Parking Garage Daily Report
```

Avoid:

```text
# Problem 3

# Exercise

# Python Quiz
```

---

# Story

Purpose:

Explain the real-world context.

Requirements:

* 1–3 short paragraphs
* Authentic
* Easy to visualize
* No unnecessary technical details

Students should understand *why* the software exists before reading the task.

---

# Task

Purpose:

Describe exactly what students must implement.

Requirements:

State:

* what the function should do
* what information it receives
* what value it returns

Do **not** describe an algorithm.

Describe behavior.

---

# Function Specification

Every assessment uses a single Python function.

Example:

```python
def calculate_daily_revenue(customers, hourly_rate, fixed_rate):
```

Function names should describe behavior.

---

# Parameters

Document every parameter individually.

Use the following format.

```markdown
### customers

Type:

`list[int]`

Description:

A list containing the parking duration for each customer.
```

Required fields:

* name
* type
* description

---

# Returns

Document the return value.

Example:

```markdown
Type:

`int`

Description:

The total revenue collected during the day.
```

---

# Constraints

Document assumptions.

Example:

* Customer hours are positive integers.
* Hourly rate is positive.
* Fixed rate is positive.
* The customer list may contain one or more entries.

Constraints clarify the problem without revealing the solution.

---

# Example

Every assessment must include at least one complete example.

Example:

Input

```python
customers = [2,5,8]
hourly_rate = 100
fixed_rate = 500
```

Output

```python
1100
```

Examples should represent typical classroom situations.

---

# Explanation

Explain the example step by step.

Students should understand why the output is correct.

Avoid merely repeating calculations.

---

# Hint

Hints should be progressive.

Preferred format:

1. Process one customer at a time.
2. Compute both possible costs.
3. Choose the cheaper one.
4. Add it to the running total.

Hints should support thinking.

They should not replace thinking.

---

# Language Guidelines

Write for Grade 9 students.

Prefer:

* everyday vocabulary
* active voice
* short sentences

Avoid:

* unnecessary jargon
* overly academic wording
* ambiguous pronouns

---

# Markdown Formatting Rules

Use:

* ATX headings (`#`)
* fenced code blocks
* blank line between sections
* bullet lists for constraints
* numbered lists for hints

Avoid:

* HTML
* tables unless necessary
* excessive nesting

Consistency is more valuable than stylistic variety.

---

# Code Blocks

Use fenced Markdown code blocks.

Specify the language.

Example:

````markdown
```python
customers = [2,4,6]
```
````

Language identifiers improve rendering.

---

# Line Length

Recommended:

100 characters or fewer.

Long paragraphs should be broken into shorter ones.

Readable Markdown is easier to review.

---

# Tone

Every problem should feel encouraging.

Students should finish reading with the feeling:

> "I understand what I need to build."

Not:

> "I hope I'm guessing correctly."

---

# Validation Checklist

Before publishing, verify that:

* □ All required sections exist.
* □ Sections appear in the correct order.
* □ Story is authentic.
* □ Task describes behavior.
* □ Every parameter is documented.
* □ Return value is documented.
* □ Constraints are complete.
* □ Example is correct.
* □ Explanation matches the example.
* □ Hint guides without solving.
* □ Markdown renders correctly.

---

# Compliance

An assessment is considered **SPEC-001 compliant** only if it satisfies every required section and formatting rule defined in this document.

Future revisions to this specification should preserve backward compatibility whenever practical.

Consistency across assessments is a core design objective of PyPractical.

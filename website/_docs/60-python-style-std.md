# Python Style Standard

**Document ID:** STD-001

**Status:** Draft

**Applies To:** All Python code in PyPractical

---

# Purpose

This standard defines the preferred Python coding style for PyPractical.

Its purpose is not to enforce every recommendation in PEP 8.

Instead, it establishes a consistent, beginner-friendly coding style that prioritizes readability, clarity, and learning.

Whenever a choice exists between writing code that is shorter and code that is easier for a Grade 9 student to understand, PyPractical chooses readability.

---

# Guiding Principles

Good educational code should be:

* readable
* predictable
* explicit
* consistent
* easy to debug

Students learn not only from solving problems, but also by reading the code we provide.

Every example should model good programming habits.

---

# The Readability Rule

If a beginner is likely to ask,

> "What does this line do?"

consider rewriting it.

Longer code is acceptable if it improves understanding.

Readable code is preferred over clever code.

---

# Follow PEP 8 (When Appropriate)

PyPractical generally follows PEP 8 for:

* indentation
* spacing
* naming
* blank lines
* line length

Educational clarity always takes priority over strict compliance.

---

# Indentation

Use four spaces.

Never use tabs.

Example

```python
for customer in customers:
    total += customer
```

---

# Line Length

Recommended maximum:

100 characters

Break long expressions across multiple lines.

Readable code is easier to review in the classroom.

---

# Blank Lines

Use blank lines to separate logical sections.

Example

```python
total = 0

for customer in customers:
    ...

return total
```

Avoid large blocks of uninterrupted code.

---

# Variable Names

Use descriptive names.

Preferred

```python
parking_hours
hourly_rate
total_cost
customer_count
```

Avoid

```python
a
b
x
temp
list1
```

Variable names should explain the purpose of the value.

---

# Function Names

Use verbs.

Examples

```python
calculate_total()

find_student()

record_program()

sort_scores()
```

Function names describe actions.

---

# Class Names

Use PascalCase.

Examples

```python
Recorder

Student

LibraryBook

ParkingTicket
```

Class names describe objects.

---

# Constants

Use UPPER_CASE.

Example

```python
MAX_CAPACITY = 50
```

Only introduce constants when they improve readability.

---

# Comments

Comments explain **why**, not **what**.

Good

```python
# The recorder is now available for another program.
```

Poor

```python
# Add 1 to i.
```

Avoid comments that simply repeat the code.

---

# Docstrings

Every public function should include a docstring.

Include:

* purpose
* parameters
* return value

Students should become familiar with reading documentation.

---

# Conditionals

Prefer explicit comparisons.

Preferred

```python
if total_cost < fixed_rate:
```

Avoid unnecessarily compact expressions.

Example

```python
minimum = total_cost if total_cost < fixed_rate else fixed_rate
```

unless the conditional expression is a learning objective.

---

# Loops

Prefer readable loops.

Preferred

```python
for customer in customers:
```

Avoid index-based loops unless the index is actually needed.

Example

```python
for i in range(len(customers)):
```

should only be used when `i` is required.

---

# Boolean Expressions

Write conditions naturally.

Preferred

```python
if recorder.is_available():
```

Avoid

```python
if recorder.is_available() == True:
```

---

# Collections

Use the simplest collection that satisfies the learning objective.

Recommended progression

1. Variables
2. Lists
3. Dictionaries
4. Objects

Do not introduce more complex structures unless they support the lesson.

---

# Functions

Functions should do one logical task.

Avoid excessively long functions.

Recommended guideline:

Approximately 30 lines or fewer for beginner assessments.

---

# Classes

Classes should represent real-world objects.

Examples

* Recorder
* Book
* Student
* Reservation

Avoid creating classes solely to demonstrate object-oriented programming.

Objects should have meaningful responsibilities.

---

# Advanced Python Features

Avoid introducing advanced features unless they are explicit learning objectives.

Examples include:

* decorators
* generators
* lambda expressions
* list comprehensions
* recursion
* context managers
* metaclasses

Students should first master fundamental programming concepts.

---

# Error Handling

Do not include exception handling unless it is part of the lesson.

Assume valid input unless stated otherwise.

---

# Imports

Only import modules required by the assessment.

Avoid unnecessary dependencies.

Simple programs are easier to understand.

---

# Magic Numbers

Avoid unexplained numeric literals.

Preferred

```python
MAX_STUDENTS = 40
```

instead of

```python
if students > 40:
```

when the number has conceptual meaning.

---

# Return Statements

Return values should clearly communicate the result.

Avoid returning from the middle of long functions unless doing so improves readability.

Prefer one clear return near the end for beginner assessments.

---

# Consistency

Consistency is more important than personal preference.

Students benefit from seeing familiar coding patterns across different assessments.

Every PyPractical solution should feel like it belongs in the same project.

---

# Validation Checklist

Before publishing, verify:

* □ Descriptive variable names
* □ Meaningful function names
* □ PascalCase class names
* □ Four-space indentation
* □ Clear comments
* □ Complete docstrings
* □ Readable loops
* □ Beginner-friendly conditionals
* □ No unnecessary advanced features
* □ Consistent formatting

---

# Compliance

Python code is **STD-001 compliant** when it follows the conventions defined in this document.

The objective of this standard is not stylistic perfection.

Its objective is to help students learn to write Python that is clear, correct, and maintainable.

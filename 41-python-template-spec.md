# Python Template Specification

**Document ID:** SPEC-002

**Status:** Draft

**Applies To:** All student starter code in PyPractical

---

# Purpose

This specification defines the required structure for all Python starter code distributed with PyPractical assessments.

Starter code exists to:

* reduce setup time
* provide a consistent programming interface
* focus students on solving the problem
* simplify automatic grading

Starter code should guide students without revealing the solution.

---

# Design Principles

Every starter program should be:

* beginner-friendly
* readable
* well documented
* consistent
* automatically gradable

The goal is not to demonstrate advanced Python.

The goal is to provide a clean starting point.

---

# File Structure

Every starter file should contain the following sections.

```text
Module Docstring

Function Definition

Function Docstring

TODO Section

Placeholder Return

(Optional)

Main Guard (for local testing only)
```

The order should remain consistent across every assessment.

---

# Module Docstring

Every file begins with a short description.

Example

```python
"""
PyPractical Starter Code

Family:
Minimum Cost Decisions

Assessment:
Parking Garage Daily Report
"""
```

The module docstring identifies the assessment.

---

# Function Definition

Every assessment exposes exactly one public function.

Example

```python
def calculate_daily_revenue(customers, hourly_rate, fixed_rate):
```

Requirements

* descriptive function name
* snake_case
* no abbreviations
* no default parameters unless required

---

# Function Docstring

Every function includes a complete docstring.

Preferred format

```python
def calculate_daily_revenue(customers, hourly_rate, fixed_rate):
    """
    Calculate the total parking revenue collected.

    Parameters
    ----------
    customers : list[int]
        Parking duration for each customer.

    hourly_rate : int
        Cost per hour.

    fixed_rate : int
        Flat parking fee.

    Returns
    -------
    int
        Total revenue collected.
    """
```

Every parameter must be documented.

---

# TODO Section

Starter code should clearly indicate where students write code.

Example

```python
    # TODO:
    # Write your solution here.
```

Do not provide algorithm hints inside the code.

Hints belong in the problem statement.

---

# Placeholder Return

Every function must execute successfully before students modify it.

Preferred

```python
    return 0
```

or

```python
    return []
```

or

```python
    return ""
```

depending on the expected return type.

Avoid

```python
    pass
```

because it causes unit tests to fail with confusing errors.

---

# Main Guard

Optional.

If included, use

```python
if __name__ == "__main__":
```

Main guards should contain only simple manual testing.

Never include assessment answers.

---

# Comments

Comments should explain purpose.

Avoid comments that explain the algorithm.

Preferred

```python
# TODO:
# Process every customer.
```

Avoid

```python
# Compare hourly cost and fixed fee,
# then add the cheaper one.
```

That belongs in the student hint.

---

# Imports

Starter code should avoid imports unless they are part of the learning objective.

Preferred

```python
# No imports
```

Acceptable

```python
import math
```

Only when required by the assessment.

---

# Input and Output

PyPractical assessments use function parameters.

Avoid

```python
input()

print()
```

unless the assessment explicitly teaches console programming.

Automatic grading relies on function calls.

---

# Global Variables

Do not use global variables.

Students should write self-contained functions.

---

# Error Handling

Do not require students to write exception handling unless that is part of the lesson.

Assume valid input unless the problem statement specifies otherwise.

---

# Type Hints

Current recommendation

No type hints.

Reason

Grade 9 students should focus on programming concepts before learning optional typing syntax.

Future curriculum levels may introduce them.

---

# Python Version

Starter code should be compatible with

Python 3.10+

Avoid version-specific features whenever practical.

---

# Naming Conventions

Use descriptive names.

Preferred

```python
parking_hours
total_revenue
hourly_rate
customer_count
```

Avoid

```python
a
b
temp
list1
```

Starter code models good programming habits.

---

# Formatting

Follow PEP 8 where appropriate.

Requirements

* four-space indentation
* blank line after docstring
* meaningful spacing
* consistent formatting

Readable code is easier to debug.

---

# Things Starter Code Must NOT Include

Do not include

* teacher solution
* partial solution
* hidden algorithms
* unnecessary helper functions
* advanced syntax
* optimization tricks
* hidden constants

Starter code should provide structure—not answers.

---

# Validation Checklist

Before publishing, verify

* □ Module docstring included
* □ One public function
* □ Descriptive function name
* □ Complete function docstring
* □ Parameters documented
* □ Return documented
* □ TODO section present
* □ Placeholder return value
* □ No solution included
* □ Compatible with automatic grading
* □ PEP 8 compliant

---

# Compliance

A starter program is **SPEC-002 compliant** only if it satisfies every structural requirement defined in this specification.

Consistency is more important than personal coding style.

Every PyPractical starter file should feel immediately familiar to both teachers and students.

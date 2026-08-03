# Family Template

Every assessment family in PyPractical should include a `README.md` based on this template.

A family groups together multiple equivalent practical assessments that teach the same primary learning objective through different authentic stories.

Families are the building blocks of the curriculum.

---

# Family Title

Example:

> Family 01 – Minimum Cost Decisions

---

# Overview

Provide a short description of the family.

Example:

This family introduces students to making decisions in Python by comparing two possible choices and selecting the better option. Students practice arithmetic, variables, loops, and conditional statements while solving authentic real-world problems.

---

# Primary Learning Objective

Describe the one new concept students should learn.

Example:

Students will use conditional statements to compare two values and select the better result.

---

# Concepts Reinforced

List previously learned concepts that naturally appear.

Example:

* Variables
* Input parameters
* Arithmetic operators
* Loops
* Functions
* Returning values

These concepts should support the learning objective rather than compete with it.

---

# Prerequisites

Students should already understand:

* Python variables
* Arithmetic expressions
* Function definitions
* `for` loops
* `if` / `else`
* Returning a value

---

# Estimated Classroom Time

Suggested completion time:

* Reading the problem: 3–5 minutes
* Planning: 3–5 minutes
* Coding: 10–15 minutes
* Testing and debugging: 5–10 minutes

Total: approximately **20–30 minutes**

Adjust this estimate based on the intended student level.

---

# Difficulty

Choose one.

* Beginner
* Beginner+
* Intermediate
* Advanced

Difficulty should reflect the intended audience rather than the algorithm itself.

---

# Assessment Type

Examples:

* Diagnostic
* Guided Practical
* Fill-in Practical
* Independent Practical
* Project

A family may support more than one assessment type.

---

# Assessment Philosophy

Briefly explain why this family exists.

Example:

This family emphasizes decision-making through authentic scenarios. Students repeatedly encounter the same computational idea in different contexts, helping them recognize underlying programming patterns rather than memorizing solutions.

---

# Assessment Variants

List every equivalent problem.

| Problem                | Story             | Status   |
| ---------------------- | ----------------- | -------- |
| Parking Garage         | Parking fees      | Complete |
| Internet Café          | Computer rental   | Complete |
| Theme Park             | Ride pass pricing | Planned  |
| School Printing Center | Printing costs    | Planned  |

Equivalent problems should assess the same learning objective while using different stories.

---

# Learning Progression

Describe where this family fits within the curriculum.

Example:

Previous Family

* Functions

Current Family

* Decision Making

Next Family

* Accumulating Values

Students should naturally feel that each family prepares them for the next.

---

# Common Student Mistakes

Document recurring observations from classroom use.

Examples:

* Comparing the wrong values
* Returning the hourly cost instead of the minimum
* Forgetting to accumulate the total
* Using the fixed fee for every customer
* Returning inside the loop

These notes should evolve through classroom experience.

---

# Teaching Notes

Suggestions for instructors.

Examples:

* Solve the first example together.
* Encourage students to trace one customer by hand.
* Remind students that loops process one item at a time.
* Ask students to explain why each decision is made.

Teaching notes should support classroom discussion rather than simply provide answers.

---

# Automatic Assessment

Document the grading strategy.

Example:

* All grading uses Python `unittest`.
* Each test has equal weight.
* Hidden tests evaluate additional valid inputs.
* Correct behavior is graded rather than implementation style.

---

# Future Extensions

Ideas for later curriculum stages.

Examples:

* Replace dictionaries with objects.
* Store transactions in files.
* Add graphical interfaces.
* Convert to a multi-class design.

Extensions help demonstrate how a simple assessment can grow with the curriculum.

---

# Revision History

Maintain a brief record of significant improvements.

| Version | Date       | Summary                                 |
| ------- | ---------- | --------------------------------------- |
| 1.0     | YYYY-MM-DD | Initial release                         |
| 1.1     | YYYY-MM-DD | Improved hints                          |
| 1.2     | YYYY-MM-DD | Corrected expected output in unit tests |

Revision history reminds future contributors that educational resources evolve through classroom experience.

# Problem Template

Every programming practical in PyPractical should be created using this template.

The template is designed to ensure that every assessment is complete, consistent, automatically gradable, and ready for classroom use.

Each section exists for a reason.

Please do not remove sections without careful consideration.

---

# 1. Problem Information

## Title

Provide a short, descriptive title.

Good examples:

* Parking Garage Daily Report
* Library Book Returns
* TV Recorder Scheduler

The title should describe the scenario rather than the programming concept.

---

## Family

State the assessment family.

Example:

> Family 01 – Minimum Cost Decisions

---

## Learning Objective

State one primary learning objective.

Example:

Students will use conditional statements to choose the lower of two calculated costs.

Avoid introducing multiple major concepts in the same assessment.

---

## Difficulty

Choose one.

* Beginner
* Beginner+
* Intermediate
* Advanced

---

## Estimated Time

Specify realistic classroom expectations.

Example:

15 minutes

25 minutes

30 minutes

Remember that estimates should come from classroom experience whenever possible.

---

# 2. Student Problem Statement

## Story

Provide an authentic scenario.

Students should understand why the software is being written.

Stories should feel realistic and relatable.

---

## Task

Describe exactly what students must accomplish.

Avoid unnecessary detail.

Students should know:

* what to calculate
* what inputs they receive
* what output they should produce

---

## Parameters

Describe every function parameter.

Example:

```text
customers

A list containing the parking duration for each customer.
```

Include:

* name
* type
* meaning

---

## Return Value

Describe the expected return value.

Example:

Return the total revenue collected for the day.

---

## Constraints

Document any assumptions.

Example:

* Parking hours are positive integers.
* Hourly rate is positive.
* Fixed rate is positive.

Constraints should help students understand the problem without revealing the algorithm.

---

## Example

Include one or more worked examples.

Examples should demonstrate the intended behavior without covering every possible case.

---

## Explanation

Explain why the example produces the given answer.

Students often learn more from the explanation than from the example itself.

---

## Hints

Hints should encourage thinking rather than provide complete solutions.

Prefer incremental hints.

Example:

1. Process one customer at a time.
2. Compute both possible costs.
3. Choose the smaller cost.
4. Add it to the running total.

---

# 3. Starter Code

Provide starter code that includes:

* function signature
* parameter documentation
* return documentation
* TODO comments

Starter code should reduce setup time while preserving the student's opportunity to solve the problem independently.

---

# 4. Teacher Solution

Include a complete reference solution.

The reference solution should:

* prioritize readability
* use beginner-friendly Python
* follow the style guide
* avoid unnecessary optimization

Students should be able to understand the solution after classroom discussion.

---

# 5. Unit Tests

Every assessment must include a comprehensive unittest suite.

Recommended categories:

* Basic cases
* Boundary cases
* Typical cases
* Mixed cases
* Hidden cases

Hidden tests should verify the published specification—not introduce new requirements.

Every expected value must be independently verified.

---

# 6. Teacher Notes

Teacher notes should include:

## Learning Objectives

What should students learn?

---

## Concepts Reinforced

Which previous concepts naturally appear?

---

## Common Mistakes

Document mistakes observed in real classrooms.

Examples:

* incorrect comparison
* forgetting accumulation
* returning too early
* modifying the input list

---

## Suggested Teaching Strategy

Examples:

* Solve one example together.
* Encourage students to trace variables.
* Discuss alternative correct solutions.
* Demonstrate debugging techniques.

Teacher notes should support instruction rather than simply provide answers.

---

# 7. Assessment Metadata

Include the following metadata.

| Item                | Example                     |
| ------------------- | --------------------------- |
| Family              | Minimum Cost Decisions      |
| Difficulty          | Beginner                    |
| Estimated Time      | 15 minutes                  |
| Assessment Type     | Diagnostic                  |
| Primary Concept     | Conditional Statements      |
| Concepts Reinforced | Variables, Loops, Functions |
| Python Topics       | if/else, for loop           |
| Automatic Grading   | Python unittest             |

Metadata helps teachers quickly determine whether an assessment fits their lesson.

---

# 8. Revision History

Maintain a brief history of important changes.

Example:

| Version | Summary                          |
| ------- | -------------------------------- |
| 1.0     | Initial classroom version        |
| 1.1     | Improved wording                 |
| 1.2     | Corrected unit test expectations |
| 1.3     | Added teacher hints              |

Educational resources improve through iteration.

Version history preserves that progress.

---

# Final Checklist

Before publishing, confirm that:

* □ One primary learning objective
* □ Authentic story
* □ Clear task description
* □ Complete parameter documentation
* □ Realistic examples
* □ Helpful explanations
* □ Progressive hints
* □ Complete starter code
* □ Readable teacher solution
* □ Passing unit tests
* □ Independently verified expected outputs
* □ Complete teacher notes
* □ Metadata included
* □ Revision history updated

If every box can be checked with confidence, the assessment is ready for classroom use.

---

# Remember

Students experience only one assessment.

Teachers may use dozens.

Contributors may create hundreds.

A consistent template helps every assessment feel familiar, allowing everyone to focus on what matters most: learning through programming.
1
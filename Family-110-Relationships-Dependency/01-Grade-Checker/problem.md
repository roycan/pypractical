# Grade Checker

## Story

A grade checker looks at an answer and decides whether it passes. The checker
uses the answer but does not own it — it receives it, reads it, and returns a
result. That is a dependency: one class uses another without storing it.

## Task

The `Answer` class is provided and complete. Do **not** modify it.

Complete the `GradeChecker` class. It does not store any data. Instead, its
methods receive an `Answer` object as a parameter, read that answer's data, and
return a result.

## Class Specification

### Answer (provided, do not modify)

An `Answer` object represents one student's answer.

It stores:

- the student's name (`name`)
- the score (`score`)

It provides `get_name` (returns the name) and `get_score` (returns the score).

### GradeChecker

A `GradeChecker` object has no stored data. It only checks answers.

## Required Methods

### GradeChecker.check_pass(answer, passing_score)

Return `True` if the answer's score is greater than or equal to `passing_score`.
Otherwise return `False`.

### GradeChecker.get_grade(answer)

Return a letter grade from the answer's score:

- `"A"` when the score is 90 or more
- `"B"` when the score is 80 or more
- `"C"` when the score is 70 or more
- `"D"` when the score is 60 or more
- `"F"` when the score is below 60

### GradeChecker.compare(answer1, answer2)

Return the name of the student with the higher score. If the scores are equal,
return the string `"Tie"`.

## Constraints

- name is a non-empty string
- score is an integer from 0 to 100
- passing_score is an integer from 0 to 100
- All inputs are valid

## Example

```python
checker = GradeChecker()
answer = Answer("Ada", 85)
print(checker.check_pass(answer, 60))
print(checker.get_grade(answer))
print(checker.compare(Answer("Ada", 85), Answer("Bo", 70)))
```

Output

```text
True
B
Ada
```

## Explanation

`check_pass` returns `True` because 85 is at least 60. `get_grade` returns
`"B"` because 85 is at least 80 but below 90. `compare` returns `"Ada"` because
85 is higher than 70. The `GradeChecker` never stores the `Answer` — it only
uses it as a parameter. That is dependency.

## Hint

In `get_grade`, check the score from the highest cutoff down to the lowest.
In `compare`, use `get_score` on both answers and compare.
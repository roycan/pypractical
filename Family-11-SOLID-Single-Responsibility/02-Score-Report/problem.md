# Score Report

## Story

A game records points and prints a report.

A junior programmer put storing points, computing the sum, AND formatting the
report all in one class. That class has too many jobs.

Your job is to apply the Single Responsibility Principle and split the work into
two classes.

## Task

Complete the **Score** and **Report** classes.

Give the **Score** class one job: store points and compute the count and sum.
Give the **Report** class a different job: format a summary string from a Score.

## Class Specification

### Score

A `Score` object records the points of a game.

Each score stores:

- a list of points

The Score class is responsible for the **data**. It stores points and computes
the count and the sum. It does **not** format any string.

### Report

A `Report` object builds a readable summary from a Score.

The Report class is responsible for the **presentation**. It does **not** store
any points. It reads them through the Score it is given.

## Required Methods

### Score.__init__()

- Create an empty list named `points`.

### Score.add_point(point)

Append the point to the `points` list.

### Score.count()

Return the number of recorded points.

### Score.total()

Loop over `points`, sum them, and return the total.

### Report.summary(score)

Return the summary string built from the score:

```text
"Points: " + str(score.count()) + ", Sum: " + str(score.total())
```

## Constraints

- Points are positive integers.
- The summary string format is exactly `Points: <count>, Sum: <total>`
  (note the space after each colon and the comma plus space).
- Use `str()` and string concatenation to build the summary. Do not use
  f-strings.
- Use an explicit loop to compute the total (not a comprehension).
- All inputs are valid.

## Example

```python
score = Score()
score.add_point(100)
score.add_point(200)
print(score.count())
print(score.total())

report = Report()
print(report.summary(score))
```

Output

```text
2
300
Points: 2, Sum: 300
```

## Explanation

The Score class has one responsibility: it stores points and computes `count`
and `total`. The Report class has a different responsibility: it formats a
readable summary from a Score. The Report does not store points — it reads them
through the Score it is given. Splitting the job this way is the Single
Responsibility Principle: each class has one reason to change.

## Hint

Keep the two responsibilities apart. Score only stores and calculates. Report
only builds the string:

`"Points: " + str(score.count()) + ", Sum: " + str(score.total())`

# Points Board

## Story

A game board records tasks that players complete. Some tasks are easy and some
are hard.

The task classes have already been written. The board simply collects tasks and
reports each one's points, calling the same `points` method on every task no
matter which class it is.

## Task

The `Easy` and `Hard` classes are provided and complete. Do **not** modify them.

Complete the `Board` class so it collects tasks and reports each one's points and
the total.

## Class Specification

### Easy (provided, do not modify)

An `Easy` object represents one easy task.

It stores:

- the task's name (`name`)
- the task's level (`level`)

Its `points` method returns `level * 1`.

### Hard (provided, do not modify)

A `Hard` object represents one hard task.

It stores:

- the task's name (`name`)
- the task's level (`level`)

Its `points` method returns `level * 3`.

### Board

A `Board` object collects tasks and reports their points.

A board should remember:

- every task added to it

## Required Methods

### Board.__init__()

- Create an empty list named `entries`.

### Board.add(entry)

Add the given task to the board's list.

### Board.points_list()

Loop over the board's entries, call `points()` on each, and return the list of
results.

### Board.total_points()

Loop over the board's entries, add each `points()` to a running total, and return
the total (an integer).

## Constraints

- name is a non-empty string
- level is a positive integer
- `Easy` gives `level * 1` points
- `Hard` gives `level * 3` points

All inputs are valid.

## Example

```python
board = Board()
board.add(Easy("A", 10))
board.add(Hard("B", 10))
print(board.points_list())
print(board.total_points())
```

Output

```text
[10, 30]
40
```

## Explanation

`points_list()` calls `.points()` on each task. An `Easy` task returns
`10 * 1 = 10`; a `Hard` task returns `10 * 3 = 30`. The SAME method name gives
different results depending on the task's class — that is polymorphism.
`total_points()` adds them together: `10 + 30 = 40`.

## Hint

In `points_list` and `total_points`, loop over `self.entries` and call
`entry.points()` on each. The board does not need to know which class each task
is — it just calls the shared method.

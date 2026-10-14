# Student Locker

## Story

Every student is assigned one locker. A locker has a number and a combination.
The student stores their locker — the simplest form of association: one object
holds a reference to another object.

## Task

The `Locker` class is provided and complete. Do **not** modify it.

Complete the `Student` class so a student can be assigned a locker, report the
locker's number, and tell whether they have a locker.

## Class Specification

### Locker (provided, do not modify)

A `Locker` object represents one school locker.

It stores:

- the locker number (`number`)
- the combination (`combination`)

It provides `get_number` (returns the number) and `get_combination` (returns
the combination).

### Student

A `Student` object represents one student.

It stores:

- the student's name (`name`)
- a locker (`locker`)

Initially the student has no locker (`None`).

## Required Methods

### Student.__init__(name)

Store the student's name and set `locker` to `None`.

### Student.assign_locker(locker)

Store the given `Locker` object.

### Student.get_locker_number()

If the student has a locker, return its number. Otherwise return the string
`"No locker"`.

### Student.has_locker()

Return `True` if the student has a locker, otherwise `False`.

## Constraints

- name is a non-empty string
- locker number is a positive integer
- combination is a non-empty string
- All inputs are valid

## Example

```python
student = Student("Ada")
print(student.has_locker())
print(student.get_locker_number())

student.assign_locker(Locker(123, "12-24-36"))
print(student.has_locker())
print(student.get_locker_number())
```

Output

```text
False
No locker
True
123
```

## Explanation

A new `Student` starts with no locker, so `has_locker` returns `False` and
`get_locker_number` returns `"No locker"`. After `assign_locker`, the student
holds a reference to a `Locker`, so `has_locker` returns `True` and
`get_locker_number` returns `123`. One student, one locker: that is a basic
association.

## Hint

In `get_locker_number`, check whether `self.locker` is `None`. If it is, return
the string `"No locker"`. Otherwise return `self.locker.get_number()`.
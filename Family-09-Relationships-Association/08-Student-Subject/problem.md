# Student Subject

## Story

A student can enroll in several subjects. A subject can have several students
enrolled. That is a many-to-many relationship — both sides hold lists of the
other. When a student enrolls, both sides must be updated.

## Task

The `Subject` class is provided and complete. Do **not** modify it.

Complete the `Student` class so that enrolling and dropping keep both the
student's list and the subject's list in sync.

## Class Specification

### Subject (provided, do not modify)

A `Subject` object represents one school subject.

It stores:

- the subject code (`code`)
- the subject title (`title`)
- a list of enrolled student names (`students`)

It provides:

- `get_code` (returns the code)
- `get_title` (returns the title)
- `add_student(name)` (adds a name to the enrollment list)
- `remove_student(name)` (removes a name from the enrollment list)
- `count_students()` (returns the number of enrolled students)
- `has_student(name)` (returns True if the name is enrolled)

### Student

A `Student` object represents one student.

It stores:

- the student's name (`name`)
- a list of subjects (`subjects`)

Initially the list is empty.

## Required Methods

### Student.__init__(name)

Store the student's name and create an empty list named `subjects`.

### Student.enroll(subject)

Append the subject to the student's list, then call
`subject.add_student(self.name)` so the subject also records the student.

### Student.drop(subject_code)

Loop over `subjects`. If a subject with the given code is found, remove it from
the list, call `subject.remove_student(self.name)`, and return `True`. If no
subject matches, return `False`.

### Student.is_enrolled(subject_code)

Return `True` if the student is enrolled in a subject with the given code.
Otherwise return `False`.

### Student.list_subjects()

Return a list containing the title of every enrolled subject.

## Constraints

- name is a non-empty string
- code and title are non-empty strings
- Subject codes are unique
- All inputs are valid

## Example

```python
math = Subject("MATH101", "Mathematics")
sci = Subject("SCI101", "Science")
student = Student("Ada")
student.enroll(math)
student.enroll(sci)
print(student.list_subjects())
print(math.count_students())
print(math.has_student("Ada"))
print(student.drop("MATH101"))
print(math.count_students())
```

Output

```text
['Mathematics', 'Science']
1
True
True
0
```

## Explanation

The student enrolls in Mathematics and Science, so `list_subjects` returns both
titles. When enrolling in Mathematics, the student's list is updated AND
`math.add_student("Ada")` is called, so `math.count_students` returns 1 and
`math.has_student("Ada")` returns `True`. After dropping Mathematics, both sides
are updated again, so `math.count_students` returns 0. Both sides change
together — that is many-to-many.

## Hint

In `enroll`, append the subject, then call `subject.add_student(self.name)`. In
`drop`, loop over `self.subjects`, compare `subject.get_code()` with the given
code, then call `subject.remove_student(self.name)` after removing it from your
list.
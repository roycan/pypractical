# Classroom

## Story

A classroom holds many students — that is a one-to-many relationship: one
classroom, many students.

The `Student` class is already written. Complete the `Classroom` class so it
stores students, counts them, and finds a student by name.

## Task

The `Student` class is provided and complete. Do **not** modify it.

Complete the `Classroom` class. A classroom stores a list of `Student` objects,
can add a student, count how many students it holds, and find the first student
with a given name.

## Class Specification

### Student (provided, do not modify)

A `Student` object represents one student in a classroom.

It stores:

- the name (`name`)
- the grade (`grade`)

It provides `get_name` (returns the name) and `get_grade` (returns the grade).

### Classroom

A `Classroom` object represents one classroom.

It stores:

- a list of students (`students`)

Initially the list is empty.

## Required Methods

### Classroom.__init__()

Create an empty list named `students`.

### Classroom.add_student(student)

Append the given student to the end of `students`.

### Classroom.count_students()

Return the number of students stored in the classroom.

### Classroom.find_by_name(name)

Loop over `students`. Return the first student whose name matches the given
name. If no student matches, return `None`.

## Constraints

- Names and grades are non-empty strings
- Names may repeat; `find_by_name` returns the first match
- All inputs are valid

## Example

```python
classroom = Classroom()
classroom.add_student(Student("Ada", "9A"))
classroom.add_student(Student("Bo", "9B"))
print(classroom.count_students())

found = classroom.find_by_name("Ada")
print(found.get_grade())

missing = classroom.find_by_name("Cy")
print(missing)
```

Output

```text
2
9A
None
```

## Explanation

The classroom holds a list of students. `count_students` returns how many (2).
`find_by_name` loops over the students and returns the first student whose name
matches — `"Ada"` is in grade `"9A"`. When no student matches (`"Cy"`), it
returns `None`. One classroom, many students: that is a one-to-many association.

## Hint

In `find_by_name`, loop over `self.students`, compare `student.get_name()` with
the given name, and return the student on the first match. After the loop,
return `None`.

# Teacher Notes — Classroom

> Family 09 · Relationships - Association · Assessment 02 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students model a one-to-many association: a container object (a `Classroom`)
holds a list of another object type (`Student`). The `Student` class is provided
complete; students write the `Classroom` class to store, count, and find
students.

## Concepts Reinforced

- Object relationships
- Association (a "has-a" relationship)
- One-to-many multiplicity (one classroom, many students)
- Classes and objects
- Lists as instance state
- Methods that loop over a collection

## Common Student Mistakes

- Returning the count instead of the student object from `find_by_name`.
- Forgetting to return `None` after the loop.
- Comparing the whole student object to the name instead of using
  `student.get_name()`.
- Returning too early inside the loop (for example, returning inside the `if`
  even on a non-match).
- Not initializing `self.students = []` in `__init__`, or sharing one list
  between instances.

## Suggested Teaching Strategy

1. Draw one `Classroom` box connected to many `Student` boxes — that is the
   one-to-many association.
2. Show that the `Classroom` does not copy the students' data; it only holds
   references to `Student` objects in a list.
3. Trace `find_by_name` by hand: walk the list, compare `student.get_name()`,
   return the first match, and return `None` only after the loop ends.
4. Emphasize the difference between `count_students` (returns a number) and
   `find_by_name` (returns an object or `None`).

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests grouped into count, find_by_name,
and hidden cases. Hidden tests check only documented behavior and add no new
requirements. A student's score is the percentage of passing tests.

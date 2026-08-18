# Teacher Notes — Student Subject

> Family 09 · Relationships I (Association) · Assessment 08 · Difficulty 4/5 · ~25 minutes

## Learning Objective

Students model the full many-to-many relationship: both sides maintain lists,
and every enroll/drop must update both lists to stay in sync.

## Concepts Reinforced

- Object relationships
- Association (a "has-a" relationship)
- Many-to-many multiplicity (both sides modeled)
- Classes and objects
- Lists as instance state
- Keeping two lists consistent

## Common Student Mistakes

- Updating only the student's list and forgetting `subject.add_student(self.name)`.
- Updating only the subject's list and forgetting to append to the student's list.
- Forgetting `subject.remove_student(self.name)` in `drop`.
- Returning `False` from `drop` even when the subject was found.
- Comparing the whole subject to the code instead of using `get_code()`.
- Removing from the subject's list but leaving the subject in the student's list.

## Suggested Teaching Strategy

1. Draw the two lists side by side: `Student.subjects` and `Subject.students`.
2. Trace `enroll` step by step: append to one list, then add the name to the
   other list.
3. Trace `drop` step by step: find by code, remove from one list, then remove the
   name from the other list.
4. Emphasize the invariant: after any enroll or drop, both sides must agree.

## Automatic Assessment

`tests.py` runs 13 equal-weight behavior tests: enroll updating both sides,
multiple subjects, multiple students sharing a subject, membership checks, drop
updating both sides, and hidden cases for three subjects, a middle drop, many
students, and getters. Hidden tests check only documented behavior and add no
new requirements. A student's score is the percentage of passing tests.
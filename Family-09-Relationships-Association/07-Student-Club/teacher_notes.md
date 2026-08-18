# Teacher Notes — Student Club

> Family 09 · Relationships I (Association) · Assessment 07 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students model a many-to-many relationship from a single side: one student holds
a list of clubs, and the code joins, leaves, checks, and lists memberships. The
club does not track members.

## Concepts Reinforced

- Object relationships
- Association (a "has-a" relationship)
- Many-to-many multiplicity (one side modeled)
- Classes and objects
- Lists as instance state
- Avoiding duplicates
- Removing from a list by value

## Common Student Mistakes

- Appending a duplicate club in `join_club`.
- Forgetting to initialize `self.clubs = []` in `__init__`.
- Returning the count from `list_clubs` (or vice versa).
- Not returning `False` from `leave_club` when the name is not found.
- Comparing the whole club to the name instead of using `get_name()`.

## Suggested Teaching Strategy

1. Emphasize that many students can join the same club — that's what makes it
   many-to-many — but here we only track the student's side.
2. Trace `join_club` twice with the same club and show the duplicate is ignored.
3. Contrast `is_member` (a boolean check) with `list_clubs` (a list of names).
4. Preview the next problem: the "both sides" version where the club also tracks
   its members.

## Automatic Assessment

`tests.py` runs 13 equal-weight behavior tests: empty state, joining, duplicate
handling, membership checks, leaving (found/not found), and hidden cases for
independence and getters. Hidden tests check only documented behavior and add no
new requirements. A student's score is the percentage of passing tests.
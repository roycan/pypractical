# Student Club

## Story

A student can join several clubs — the chess club, the art club, the robotics
club. The student keeps track of which clubs they belong to. Many students can
join the same club, but the club itself does not track its members. That is a
many-to-many relationship from one side: the student manages their own list.

## Task

The `Club` class is provided and complete. Do **not** modify it.

Complete the `Student` class so a student can join clubs, leave clubs, check
membership, and list the clubs they belong to.

## Class Specification

### Club (provided, do not modify)

A `Club` object represents one school club.

It stores:

- the club's name (`name`)
- the club's description (`description`)

It provides `get_name` (returns the name) and `get_description` (returns the
description).

### Student

A `Student` object represents one student.

It stores:

- the student's name (`name`)
- a list of clubs (`clubs`)

Initially the list is empty.

## Required Methods

### Student.__init__(name)

Store the student's name and create an empty list named `clubs`.

### Student.join_club(club)

Append the club to the list. If the student is already a member, do nothing.

### Student.leave_club(club_name)

Loop over `clubs`. If a club with the given name is found, remove it and return
`True`. If no club matches, return `False`.

### Student.is_member(club_name)

Return `True` if the student belongs to a club with the given name. Otherwise
return `False`.

### Student.list_clubs()

Return a list containing the name of every club the student belongs to.

## Constraints

- name and description are non-empty strings
- Club names are unique
- All inputs are valid

## Example

```python
student = Student("Ada")
student.join_club(Club("Chess", "Play chess"))
student.join_club(Club("Art", "Paint and draw"))
student.join_club(Club("Chess", "Play chess"))
print(student.list_clubs())
print(student.is_member("Art"))
print(student.leave_club("Chess"))
print(student.list_clubs())
```

Output

```text
['Chess', 'Art']
True
True
['Art']
```

## Explanation

The student joins the Chess and Art clubs. Joining Chess a second time does
nothing, so `list_clubs` returns `["Chess", "Art"]`. `is_member("Art")` returns
`True`. After leaving Chess, `list_clubs` returns `["Art"]`. One student can
belong to many clubs — that is many-to-many from the student's side.

## Hint

In `join_club`, check `is_member` first to avoid duplicates. In `leave_club`,
loop over `self.clubs`, compare `club.get_name()` with the given name, and use
`self.clubs.remove(club)` on the first match.
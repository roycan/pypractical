# Sports Captain

## Story

A sports club keeps track of its members. Every member has a name and a club. A
captain also has a number of trophies won, and the club must never record a
captain with zero or negative trophies — that would be garbage data.

## Task

The `Member` class is provided and complete. Do **not** modify it.

Complete the `Captain` class so a captain inherits the member's name and club
and protects its own trophy count.

## Class Specification

### Member (provided, do not modify)

A `Member` object represents one club member.

Each member stores:

- the member's name (`name`)
- the member's club (`club`)

### Captain

A `Captain` object represents one team captain. A captain IS-A member.

Each captain should remember:

- the inherited member's name and club
- a protected trophy count (`_trophies_won`)

## Required Methods

### Captain.\_\_init\_\_(name, club, trophies_won)

Call `super().__init__(name, club)` so the captain inherits the name and club.
Then validate the trophy count:

- if `trophies_won` is zero or negative, print
  `"The number of trophies must be positive"` and store `0` as the placeholder
  meaning "not recorded"
- otherwise store the value in the protected attribute `_trophies_won`

### Captain.get_trophies_won()

Return the protected `_trophies_won`.

## Constraints

- name is a non-empty string
- club is a non-empty string
- trophies_won is an integer (it may be zero or negative — the constructor must
  handle that case)

## Example

```python
member = Member("Ana", "Chess")
print(member.display_info())

captain = Captain("Ben", "Football", 3)
print(captain.display_info())
print(captain.get_trophies_won())

bad_captain = Captain("Cal", "Basketball", -1)
print(bad_captain.get_trophies_won())
```

Output

```text
Name: Ana, Club: Chess
Name: Ben, Club: Football
3
The number of trophies must be positive
0
```

## Explanation

`member` is a plain `Member`. The `captain` is a `Captain`, so it is also a
member: its `name` and `club` come from the parent through
`super().__init__(name, club)`, and its `display_info()` is the parent's method,
reused unchanged. `bad_captain` is given a negative trophy count, so the
constructor prints a warning and stores the placeholder `0` — its data is
rejected, not silently kept.

## Hint

Write `class Captain(Member):` so the captain inherits from the parent. In
`__init__`, call `super().__init__(name, club)` first. Then check the trophy
count with `<= 0` before storing it in `self._trophies_won` — zero trophies is
garbage data too.

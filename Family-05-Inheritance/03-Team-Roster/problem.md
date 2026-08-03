# Team Roster

## Story

Every captain is also a player. The `Player` class has already been written and
stores a player's name and number.

A captain inherits the player's name and number, and adds a team.

## Task

The `Player` class is provided and complete. Do **not** modify it.

Complete the `Captain` class so a captain inherits `get_name` and `get_number`
from `Player` and also stores a `team`.

## Class Specification

### Player (provided, do not modify)

A `Player` object represents one team player.

Each player stores:

- the player's name (`name`)
- the player's number (`number`)

### Captain

A `Captain` object represents one player who leads a team.

Each captain should remember:

- the inherited player's name and number
- a team (`team`)

## Required Methods

### Captain.__init__(name, number, team)

Call `super().__init__(name, number)` to reuse the parent, then store the
captain's `team`.

### Captain.get_team()

Return the captain's `team`.

## Constraints

- name is a non-empty string
- number is a positive integer
- team is a non-empty string

All inputs are valid.

## Example

```python
player = Player("Ada", 9)
print(player.get_name())
print(player.get_number())

captain = Captain("Bo", 10, "Tigers")
print(captain.get_name())
print(captain.get_number())
print(captain.get_team())
```

Output

```text
Ada
9
Bo
10
Tigers
```

## Explanation

A `Captain` inherits `get_name` and `get_number` from `Player`, so
`captain.get_name()` returns `"Bo"` and `captain.get_number()` returns `10`
even though `Captain` does not define those methods. `Captain` adds its own
`team`, returned by `get_team`. That is inheritance: the child reuses the
parent and adds something new.

## Hint

In the child `__init__`, call `super().__init__(name, number)` to reuse the
parent, then set the new attribute with `self.team = team`.

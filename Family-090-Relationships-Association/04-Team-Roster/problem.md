# Team Roster

## Story

A team holds many players — that is a one-to-many relationship: one team, many
players.

The `Player` class is already written. Complete the `Team` class so it stores
players, counts them, and finds a player by name.

## Task

The `Player` class is provided and complete. Do **not** modify it.

Complete the `Team` class. A team stores a list of `Player` objects, can add a
player, count how many players it holds, and find the first player with a given
name.

## Class Specification

### Player (provided, do not modify)

A `Player` object represents one player on a team.

It stores:

- the name (`name`)
- the position (`position`)

It provides `get_name` (returns the name) and `get_position` (returns the
position).

### Team

A `Team` object represents one team.

It stores:

- a list of players (`players`)

Initially the list is empty.

## Required Methods

### Team.__init__()

Create an empty list named `players`.

### Team.add_player(player)

Append the given player to the end of `players`.

### Team.count_players()

Return the number of players stored on the team.

### Team.find_by_name(name)

Loop over `players`. Return the first player whose name matches the given name.
If no player matches, return `None`.

## Constraints

- Names and positions are non-empty strings
- Names may repeat; `find_by_name` returns the first match
- All inputs are valid

## Example

```python
team = Team()
team.add_player(Player("Ada", "Guard"))
team.add_player(Player("Bo", "Forward"))
print(team.count_players())

found = team.find_by_name("Ada")
print(found.get_position())

missing = team.find_by_name("Cy")
print(missing)
```

Output

```text
2
Guard
None
```

## Explanation

The team holds a list of players. `count_players` returns how many (2).
`find_by_name` loops over the players and returns the first player whose name
matches — `"Ada"` plays `"Guard"`. When no player matches (`"Cy"`), it returns
`None`. One team, many players: that is a one-to-many association.

## Hint

In `find_by_name`, loop over `self.players`, compare `player.get_name()` with the
given name, and return the player on the first match. After the loop, return
`None`.

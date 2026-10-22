# Video Game Edition

## Story

A game store keeps track of its games. Every game has a title and a genre. A
deluxe edition also has bonus levels, and the store must never record an edition
with zero or negative bonus levels — that would be garbage data.

## Task

The `Game` class is provided and complete. Do **not** modify it.

Complete the `DeluxeEdition` class so a deluxe edition inherits the game's title
and genre and protects its own bonus level count.

## Class Specification

### Game (provided, do not modify)

A `Game` object represents one game in the store.

Each game stores:

- the game's title (`title`)
- the game's genre (`genre`)

### DeluxeEdition

A `DeluxeEdition` object represents one deluxe edition of a game. A deluxe
edition IS-A game.

Each deluxe edition should remember:

- the inherited game's title and genre
- a protected bonus level count (`_bonus_levels`)

## Required Methods

### DeluxeEdition.\_\_init\_\_(title, genre, bonus_levels)

Call `super().__init__(title, genre)` so the deluxe edition inherits the title
and genre. Then assign the bonus level count to `self.bonus_levels` so the
setter below validates and stores it.

### DeluxeEdition.bonus_levels (property)

Use the `@property` decorator so callers read the count as
`deluxe.bonus_levels` — no parentheses. Return the protected `_bonus_levels`.

### DeluxeEdition.bonus_levels (setter)

Use the `@bonus_levels.setter` decorator. Validate the bonus level count:

- if the value is zero or negative, print
  `"The number of bonus levels must be positive"` and store `0` as the
  placeholder meaning "not recorded"
- otherwise store the value in the protected attribute `_bonus_levels`

## Constraints

- title is a non-empty string
- genre is a non-empty string
- bonus_levels is an integer (it may be zero or negative — the constructor must
  handle that case)

## Example

```python
game = Game("Chess", "Board")
print(game.display_info())

deluxe = DeluxeEdition("Elden Ring", "RPG", 40)
print(deluxe.display_info())
print(deluxe.bonus_levels)

bad_deluxe = DeluxeEdition("Mystery Quest", "Puzzle", -2)
print(bad_deluxe.bonus_levels)
```

Output

```text
Title: Chess, Genre: Board
Title: Elden Ring, Genre: RPG
40
The number of bonus levels must be positive
0
```

## Explanation

`game` is a plain `Game`. The `deluxe` is a `DeluxeEdition`, so it is also a
game: its `title` and `genre` come from the parent through
`super().__init__(title, genre)`, and its `display_info()` is the parent's
method, reused unchanged. The bonus level count is protected:
`deluxe.bonus_levels` reads it through the `@property` getter, and the
`@bonus_levels.setter` validates every value before it is stored. `bad_deluxe`
is given a negative bonus level count, so the setter prints a warning and stores
the placeholder `0` — its data is rejected, not silently kept.

## Hint

Write `class DeluxeEdition(Game):` so the edition inherits from the parent. In
`__init__`, call `super().__init__(title, genre)` first, then assign
`self.bonus_levels = bonus_levels` so the setter runs. Decorate the getter with
`@property` and the setter with `@bonus_levels.setter`. In the setter, check the
value with `<= 0` before storing it in `self._bonus_levels` — zero bonus levels
is garbage data too.

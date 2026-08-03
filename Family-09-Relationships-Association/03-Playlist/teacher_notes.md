# Teacher Notes — Playlist

> Family 09 · Relationships - Association · Assessment 03 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students model a one-to-many association: a container object (a `Playlist`)
holds a list of another object type (`Song`). The `Song` class is provided
complete; students write the `Playlist` class to store, count, and find songs.

## Concepts Reinforced

- Object relationships
- Association (a "has-a" relationship)
- One-to-many multiplicity (one playlist, many songs)
- Classes and objects
- Lists as instance state
- Methods that loop over a collection

## Common Student Mistakes

- Returning the count instead of the song object from `find_by_title`.
- Forgetting to return `None` after the loop.
- Comparing the whole song object to the title instead of using
  `song.get_title()`.
- Returning too early inside the loop (for example, returning inside the `if`
  even on a non-match).
- Not initializing `self.songs = []` in `__init__`, or sharing one list between
  instances.

## Suggested Teaching Strategy

1. Draw one `Playlist` box connected to many `Song` boxes — that is the
   one-to-many association.
2. Show that the `Playlist` does not copy the songs' data; it only holds
   references to `Song` objects in a list.
3. Trace `find_by_title` by hand: walk the list, compare `song.get_title()`,
   return the first match, and return `None` only after the loop ends.
4. Emphasize the difference between `count_songs` (returns a number) and
   `find_by_title` (returns an object or `None`).

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests grouped into count, find_by_title,
and hidden cases. Hidden tests check only documented behavior and add no new
requirements. A student's score is the percentage of passing tests.

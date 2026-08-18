# Teacher Notes — House Rooms

> Family 10 · Relationships II (Composition) · Assessment 05 · Difficulty 4/5 · ~25 minutes

## Learning Objective

Students model composition: a whole object creates its part objects in
`__init__` from a list of specifications, then aggregates their data.

## Concepts Reinforced

- Composition (a whole creates and owns its parts)
- Object ownership (parts do not exist without the whole)
- Whole-part relationship
- Classes and objects
- Lists as instance state
- Loops in `__init__`
- Tuples and tuple unpacking
- Finding a maximum

## Common Student Mistakes

- Not creating the parts in `__init__` (leaving the list empty).
- Creating the list but never appending the `Room` objects.
- Forgetting to unpack the tuple: writing `for room in room_specs:` and treating
  `room` as a `Room` when it is actually a tuple.
- Returning the count from `total_area` (or vice versa).
- Starting the largest-room comparison with a room that doesn't exist when the
  list is empty.
- Using `>=` in the largest-room comparison (which would break the tie rule).

## Suggested Teaching Strategy

1. Contrast composition with aggregation: in composition, the `House` creates the
   `Room` objects inside `__init__`; in aggregation, the parts are passed in.
2. Trace `for room_name, area in room_specs:` — tuple unpacking creates the two
   values from each tuple.
3. Walk through `get_largest_room`: start with the first room, then replace it
   only when a strictly larger room is found (so ties keep the first).
4. Have students verify `total_area` by hand: `12 + 20 + 6 = 38`.

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests: empty and non-empty counts, total
area, largest room (with and without ties), listing names, and hidden cases for
four rooms and getters. Hidden tests check only documented behavior and add no
new requirements. A student's score is the percentage of passing tests.
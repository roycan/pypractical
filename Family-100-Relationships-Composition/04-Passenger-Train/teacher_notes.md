# Teacher Notes — Passenger Train

> Family 10 · Relationships - Composition · Assessment 04 · Difficulty 4/5 · ~25 minutes

## Learning Objective

Students model composition: a whole object (a `Train`) creates and owns its
parts (`Carriage` objects) in `__init__`. The `Carriage` class is provided
complete; students write the `Train` class that builds its own carriages, counts
them, and reports their total seats.

## Concepts Reinforced

- Composition (a whole creates and owns its parts)
- Object ownership (parts do not exist independently of the whole)
- Whole-part relationship
- Classes and objects
- Lists as instance state
- Loops in `__init__`

## Common Student Mistakes

- Not creating the parts in `__init__` (leaving the list empty).
- Creating the list but never appending the `Carriage` objects.
- Returning the count from `total_seats` (or vice versa).
- An off-by-one error in the loop (for example `range(carriage_count + 1)`).
- Receiving carriages from outside instead of building them — that is aggregation
  (Family 09), not composition.

## Suggested Teaching Strategy

1. Contrast this with aggregation (Family 09): there, items arrive from outside
   via an `add_*` method. Here the whole builds its own parts in `__init__`.
2. Draw one `Train` box that contains many `Carriage` boxes created by it — the
   carriages cannot exist without the train.
3. Trace `__init__` by hand: start with an empty list, then loop
   `for i in range(carriage_count):` appending a new `Carriage(seats)` each time.
4. Show that `count_carriages` returns a length and `total_seats` loops to add
   each carriage's seats.

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests grouped into count, total_seats,
parts created, and hidden cases. Hidden tests check only documented behavior and
add no new requirements. A student's score is the percentage of passing tests.

# Teacher Notes — Flashlight

> Family 10 · Relationships - Composition · Assessment 01 · Difficulty 4/5 · ~25 minutes

## Learning Objective

Students model composition: a whole object (a `Flashlight`) creates and owns its
parts (`Battery` objects) in `__init__`. The `Battery` class is provided
complete; students write the `Flashlight` class that builds its own batteries,
counts them, and reports their total capacity.

## Concepts Reinforced

- Composition (a whole creates and owns its parts)
- Object ownership (parts do not exist independently of the whole)
- Whole-part relationship
- Classes and objects
- Lists as instance state
- Loops in `__init__`

## Common Student Mistakes

- Not creating the parts in `__init__` (leaving the list empty).
- Creating the list but never appending the `Battery` objects.
- Returning the count from `total_capacity` (or vice versa).
- An off-by-one error in the loop (for example `range(battery_count + 1)`).
- Receiving batteries from outside instead of building them — that is
  aggregation (Family 09), not composition.

## Suggested Teaching Strategy

1. Contrast this with aggregation (Family 09): there, items arrive from outside
   via an `add_*` method. Here the whole builds its own parts in `__init__`.
2. Draw one `Flashlight` box that contains many `Battery` boxes created by it —
   the batteries cannot exist without the flashlight.
3. Trace `__init__` by hand: start with an empty list, then loop
   `for i in range(battery_count):` appending a new `Battery(capacity)` each
   time.
4. Show that `count_batteries` returns a length and `total_capacity` loops to
   add each capacity.

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests grouped into count,
total_capacity, parts created, and hidden cases. Hidden tests check only
documented behavior and add no new requirements. A student's score is the
percentage of passing tests.

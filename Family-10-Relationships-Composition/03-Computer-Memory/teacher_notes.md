# Teacher Notes — Computer Memory

> Family 10 · Relationships - Composition · Assessment 03 · Difficulty 4/5 · ~25 minutes

## Learning Objective

Students model composition: a whole object (a `Computer`) creates and owns its
parts (`Module` objects) in `__init__`. The `Module` class is provided complete;
students write the `Computer` class that builds its own memory modules, counts
them, and reports their total memory.

## Concepts Reinforced

- Composition (a whole creates and owns its parts)
- Object ownership (parts do not exist independently of the whole)
- Whole-part relationship
- Classes and objects
- Lists as instance state
- Loops in `__init__`

## Common Student Mistakes

- Not creating the parts in `__init__` (leaving the list empty).
- Creating the list but never appending the `Module` objects.
- Returning the count from `total_memory` (or vice versa).
- An off-by-one error in the loop (for example `range(module_count + 1)`).
- Receiving modules from outside instead of building them — that is aggregation
  (Family 09), not composition.

## Suggested Teaching Strategy

1. Contrast this with aggregation (Family 09): there, items arrive from outside
   via an `add_*` method. Here the whole builds its own parts in `__init__`.
2. Draw one `Computer` box that contains many `Module` boxes created by it — the
   modules cannot exist without the computer.
3. Trace `__init__` by hand: start with an empty list, then loop
   `for i in range(module_count):` appending a new `Module(size)` each time.
4. Show that `count_modules` returns a length and `total_memory` loops to add
   each size.

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests grouped into count, total_memory,
parts created, and hidden cases. Hidden tests check only documented behavior and
add no new requirements. A student's score is the percentage of passing tests.

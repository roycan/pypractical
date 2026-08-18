# Teacher Notes — Computer Peripherals

> Family 12 · Relationships IV (Aggregation) · Assessment 01 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students model aggregation: a whole object holds a list of part objects that are
created outside and passed in. The parts can exist independently.

## Concepts Reinforced

- Object relationships
- Aggregation (a "has-a" relationship where parts live independently)
- Whole-part relationship
- Classes and objects
- Lists as instance state
- Loops over a collection
- Removing from a list by value

## Common Student Mistakes

- Creating the parts in `__init__` instead of receiving them (that's composition).
- Forgetting to initialize `self.peripherals = []` in `__init__`.
- Returning the count from `list_peripheral_names` (or vice versa).
- Not returning `False` from `remove_peripheral` when the name is not found.
- Comparing the whole object to the name instead of using `get_name()`.
- Using `list.remove()` on an element that may not exist without checking first.

## Suggested Teaching Strategy

1. Contrast aggregation with composition: in aggregation, the parts are created
   outside and passed in via `add_peripheral`. In composition, the whole creates
   the parts in `__init__`.
2. Draw the object diagram: `Computer.peripherals` is a list of `Peripheral`
   objects that were created independently.
3. Trace `remove_peripheral`: loop, find by name, remove, return True. After the
   loop, return False.
4. Emphasize that `Peripheral` objects can exist without a `Computer` — they are
   created first, then added.

## Automatic Assessment

`tests.py` runs 15 equal-weight behavior tests: empty state, adding, listing
names, checking types, removing (found/not found/middle), and hidden cases for
independence and getters. Hidden tests check only documented behavior and add no
new requirements. A student's score is the percentage of passing tests.
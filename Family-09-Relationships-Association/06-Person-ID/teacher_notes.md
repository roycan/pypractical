# Teacher Notes — Person ID

> Family 09 · Relationships I (Association) · Assessment 06 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students model a one-to-one association: one object holds exactly one reference
to another, and that reference can be replaced.

## Concepts Reinforced

- Object relationships
- Association (a "has-a" relationship)
- One-to-one multiplicity
- Classes and objects
- A single object reference as instance state
- Returning an object (not just a value)

## Common Student Mistakes

- Forgetting to set `self.id_card = None` in `__init__`.
- Returning the whole `IDCard` from `get_id_number` instead of calling
  `get_number()` on it.
- Not returning `None` from `get_id_card` when no card is set.
- Forgetting the `"No ID"` string case.
- Setting the card but not allowing a second card to replace the first.

## Suggested Teaching Strategy

1. Emphasize "one person, one card" — the relationship is one-to-one.
2. Draw the object reference: `Person.id_card` points to one `IDCard` or to
   `None`.
3. Trace `set_id_card` twice: the second card replaces the first.
4. Contrast `get_id_card` (returns the object) with `get_id_number` (returns a
   value derived from the object).

## Automatic Assessment

`tests.py` runs 8 equal-weight behavior tests: the no-card default, setting a
card, reading the number, replacing a card, and hidden cases for independence
and different values. Hidden tests check only documented behavior and add no
new requirements. A student's score is the percentage of passing tests.
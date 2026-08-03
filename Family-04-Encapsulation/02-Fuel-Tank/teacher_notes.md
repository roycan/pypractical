# Teacher Notes — Fuel Tank

> Family 04 · Encapsulation · Assessment 02 · Difficulty 2/5 · ~20 minutes

## Learning Objective

Students protect an object's data with a private-by-convention attribute and
validating getters/mutators.

## Concepts Reinforced

- Encapsulation
- Classes and objects
- Instance variables
- Methods
- Accessors (getters) and mutators

## Common Student Mistakes

- Exposing the litres without a leading underscore.
- Forgetting the `litres > 0` check in `add_fuel` or `draw_fuel`.
- Allowing the tank to go below zero (drawing more than available).
- Returning a value from a void mutator (`add_fuel` or `draw_fuel`).

## Suggested Teaching Strategy

1. Emphasize that the object guards its own rules.
2. Show that `_litres` is protected by convention and read only through
   `get_litres`.
3. Trace the example: every change goes through a validating mutator.
4. Discuss why invalid amounts must be ignored rather than crash the program.
5. Have students run the unittest suite to confirm their guards work.

## Automatic Assessment

`tests.py` runs 13 equal-weight behavior tests: initial state, basic changes,
input validation, a typical sequence, and hidden edge cases. Hidden tests check
only documented behavior and add no new requirements. A student's score is the
percentage of passing tests.

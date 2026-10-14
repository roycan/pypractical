# Teacher Notes — Bank Account

> Family 04 · Encapsulation · Assessment 01 · Difficulty 2/5 · ~20 minutes

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

- Exposing the balance without a leading underscore.
- Forgetting the `amount > 0` check in `deposit` or `withdraw`.
- Allowing an overdraft (withdrawing more than the balance).
- Returning a value from a void mutator (`deposit` or `withdraw`).

## Suggested Teaching Strategy

1. Emphasize that the object guards its own rules.
2. Show that `_balance` is protected by convention and read only through
   `get_balance`.
3. Trace the example: every change goes through a validating mutator.
4. Discuss why invalid amounts must be ignored rather than crash the program.
5. Have students run the unittest suite to confirm their guards work.

## Automatic Assessment

`tests.py` runs 13 equal-weight behavior tests: initial state, basic changes,
input validation, a typical sequence, and hidden edge cases. Hidden tests check
only documented behavior and add no new requirements. A student's score is the
percentage of passing tests.

# Teacher Notes — TV Recorder Scheduler

> Family 03 · Classes and Objects · Assessment 01 · Difficulty 2/5 · ~20 minutes

## Learning Objective

Students design a class with instance variables (state) and methods (behavior),
and connect two classes through a provided client function.

## Concepts Reinforced

- Defining a class
- Writing a constructor (`__init__`)
- Instance variables (state)
- Methods that read and update state
- Objects working together

## Common Student Mistakes

- Forgetting `self.` when creating or reading instance variables.
- Storing parameters in local variables instead of `self.start`, `self.end`, etc.
- Not initializing `available_at` to `0` or `programs` to `[]`.
- Returning a value from `record` (it should only update state).
- Trying to modify `minimum_recorders` (students must not change it).

## Suggested Teaching Strategy

1. Start with objects as nouns: a Program has a start, an end, and a channel.
2. Show that a Recorder remembers when it is free (`available_at`) and what it
   recorded (`programs`).
3. Trace the example by hand: create a program, create a recorder, check
   `can_record`, then call `record`.
4. Emphasize that `minimum_recorders` already works — correct classes make the
   whole system work.
5. Have students run the integration tests to see their classes used by the
   scheduler.

## Automatic Assessment

`tests.py` runs 14 equal-weight behavior tests: Program attributes, Recorder
initial state, `can_record`, `record`, and integration tests through the provided
scheduler. Hidden tests check only documented behavior and add no new
requirements. A student's score is the percentage of passing tests.

# Teacher Notes — Interview Scheduler

> Family 03 · Classes and Objects · Assessment 03 · Difficulty 2/5 · ~20 minutes

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
- Not initializing `available_at` to `0` or `interviews` to `[]`.
- Returning a value from `conduct` (it should only update state).
- Trying to modify `minimum_interviewers` (students must not change it).

## Suggested Teaching Strategy

1. Start with objects as nouns: an Interview has a start, an end, and a panel
   size.
2. Show that an Interviewer remembers when they are free (`available_at`) and
   what they conduct (`interviews`).
3. Trace the example by hand: create an interview, create an interviewer,
   check `can_take`, then call `conduct`.
4. Emphasize that `minimum_interviewers` already works — correct classes make
   the whole system work.
5. Have students run the integration tests to see their classes used by the
   scheduler.

## Automatic Assessment

`tests.py` runs 14 equal-weight behavior tests: Interview attributes,
Interviewer initial state, `can_take`, `conduct`, and integration tests through
the provided scheduler. Hidden tests check only documented behavior and add no
new requirements. A student's score is the percentage of passing tests.

# Teacher Notes — Video Game Edition

> Family 055 · Encapsulation and Inheritance · Assessment 02 · Difficulty 2/5 · ~15 minutes

## Learning Objective

Students combine two ideas in one class: a subclass reuses a provided parent
through `super().__init__(...)`, and the object protects its own data by
validating before it stores.

## Concepts Reinforced

- Inheritance and subclasses (`class DeluxeEdition(Game):`)
- `super().__init__(...)`
- Encapsulation with a protected attribute (`_bonus_levels`)
- Input validation before storing
- Getters (accessors)

## Common Student Mistakes

- Forgetting `(Game)` when declaring the child class.
- Forgetting to call `super().__init__(title, genre)`.
- Storing a public `bonus_levels` instead of the protected `_bonus_levels`.
- Checking only `< 0`, letting zero bonus levels slip through (`<= 0` is required).
- Printing the warning but forgetting the `0` placeholder fallback.
- Returning instead of printing the warning (or the reverse).

## Suggested Teaching Strategy

1. Point out the is-a relationship: a `DeluxeEdition` IS-A `Game`, so it reuses
   the parent's `display_info()` unchanged — no overriding here.
2. Trace `super().__init__(title, genre)`: the parent stores title and genre;
   the child only adds its own field.
3. Discuss why the object checks its own data "at the door" instead of trusting
   the caller. What would a bonus level count of `0` mean?
4. The zero-fallback rule is deliberate: `0` is a documented placeholder
   meaning "not recorded", never a valid count.
5. Have students predict what the broken-solution tests catch: removing the
   parent, removing `super()`, going public, or using `< 0`.

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests: the subclass relationship,
inherited title/genre, the inherited `display_info()`, the protected attribute
and getter, zero/negative warnings, the zero fallback, valid-construction
silence, independence of two editions, and one hidden parent case. Hidden tests
check only documented behavior and add no new requirements. A student's score
is the percentage of passing tests.

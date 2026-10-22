# Teacher Notes — Streaming Account

> Family 055 · Encapsulation and Inheritance · Assessment 03 · Difficulty 2/5 · ~15 minutes

## Learning Objective

Students combine two ideas in one class: a subclass reuses a provided parent
through `super().__init__(...)`, and the object protects its own data by
validating before it stores.

## Concepts Reinforced

- Inheritance and subclasses (`class PremiumAccount(Account):`)
- `super().__init__(...)`
- Encapsulation with a protected attribute (`_max_screens`)
- Input validation before storing
- Getters (accessors) via the `@property` decorator
- Setters via the `@max_screens.setter` decorator

## Common Student Mistakes

- Forgetting `(Account)` when declaring the child class.
- Forgetting to call `super().__init__(email, owner)`.
- Storing a public `max_screens` instead of the protected `_max_screens`.
- Writing `self.max_screens = value` inside the setter, which calls the setter
  again and raises `RecursionError` (it must be `self._max_screens`).
- Forgetting the `@max_screens.setter` block, so `__init__`'s assignment raises
  `AttributeError: can't set attribute`.
- Checking only `< 0`, letting zero screens slip through (`<= 0` is required).
- Printing the warning but forgetting the `0` placeholder fallback.
- Returning instead of printing the warning (or the reverse).

## Suggested Teaching Strategy

1. Point out the is-a relationship: a `PremiumAccount` IS-A `Account`, so it
   reuses the parent's `display_info()` unchanged — no overriding here.
2. Trace `super().__init__(email, owner)`: the parent stores email and owner;
   the child only adds its own field.
3. Show that `__init__` assigns `self.max_screens = ...`, so the setter is the
   single place that validates — the constructor reuses it rather than
   duplicating the check.
4. Discuss why the object checks its own data "at the door" instead of trusting
   the caller. What would a screen limit of `0` mean?
5. The zero-fallback rule is deliberate: `0` is a documented placeholder
   meaning "not recorded", never a valid count.
6. Have students predict what the broken-solution tests catch: removing the
   parent, removing `super()`, dropping `@property`, disabling the setter's
   guard, or using `< 0`.

## Automatic Assessment

`tests.py` runs 13 equal-weight behavior tests: the subclass relationship,
inherited email/owner, the inherited `display_info()`, the protected attribute
and property getter, zero/negative warnings, the zero fallback,
valid-construction silence, a post-construction update that must be validated,
independence of two premium accounts, and one hidden parent case. Hidden tests
check only documented behavior and add no new requirements. A student's score is
the percentage of passing tests.

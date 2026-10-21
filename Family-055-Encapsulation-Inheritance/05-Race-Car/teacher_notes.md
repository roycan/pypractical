# Teacher Notes — Race Car

> Family 055 · Encapsulation and Inheritance · Assessment 05 · Difficulty 2/5 · ~15 minutes

## Learning Objective

Students combine two ideas in one class: a subclass reuses a provided parent
through `super().__init__(...)`, and the object protects its own data by
validating it **against the parent's state** before it stores.

## Concepts Reinforced

- Inheritance and subclasses (`class Racer(Vehicle):`)
- `super().__init__(...)`
- Encapsulation with a protected attribute (`_top_speed`)
- Relational validation: the new value is checked against an inherited value
- Getters (accessors)

## How This Problem Differs From Variants 01–04

Variants 01–04 are isomorphic: the validated value is checked against a fixed
literal (`<= 0`) and an invalid value falls back to the placeholder `0`. This
problem is a deliberately **non-isomorphic practice extension**:

- The validation rule references **parent state**: `top_speed <= self.max_speed`.
  The bound is a relational one between the child's proposed value and a value
  the child only has because it called `super().__init__(...)`. Inheritance and
  encapsulation interlock, so a solution pattern-matched from 01–04 will not fit.
- The invalid fallback is the parent's `max_speed`, **not** `0`. There is no
  "not recorded" placeholder here; an impossible top speed is clamped to the
  largest speed the car can actually reach.
- Equal-to-maximum is **valid** (`<=`, not `<`): a top speed equal to the
  vehicle's maximum is legal, so the boundary test is meaningful.

Because it is not exam-equivalent, it is not labelled an Assessment Variant for
fair section comparison; it is a practice extension that interlocks the two
skills.

## Common Student Mistakes

- Forgetting `(Vehicle)` when declaring the child class.
- Forgetting to call `super().__init__(name, max_speed)` — then `self.max_speed`
  does not exist and the comparison raises `AttributeError`.
- Comparing against the argument `max_speed` instead of `self.max_speed` — it
  happens to work here, but it hides the fact that the bound is inherited state.
- Storing a public `top_speed` instead of the protected `_top_speed`.
- Using `<` instead of `<=`, wrongly rejecting a top speed equal to the maximum.
- Falling back to `0` (the 01–04 placeholder) instead of `self.max_speed`.
- Printing the warning but forgetting the clamp fallback.

## Suggested Teaching Strategy

1. Point out the is-a relationship: a `Racer` IS-A `Vehicle`, so it reuses the
   parent's `display_info()` unchanged — no overriding here.
2. Trace `super().__init__(name, max_speed)`: the parent stores name and
   max_speed; the child only adds its own field — but that field's rule depends
   on what the parent stored.
3. Make the interlock explicit: the child cannot validate `top_speed` until it
   has called `super()`, because `self.max_speed` does not exist before that.
   Ask students to predict what happens if `super()` is removed.
4. Discuss the boundary: why is a top speed equal to the maximum allowed? Why is
   the fallback the maximum rather than `0`?
5. Have students predict what the broken-solution tests catch: removing the
   parent, removing `super()`, going public, or using `<` instead of `<=`.

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests: the subclass relationship,
inherited name/max_speed, the inherited `display_info()`, the protected attribute
and getter, the equal-to-max valid case, the exceeding-max warning, the
clamp-to-max fallback, valid-construction silence, independence of two racers,
and one hidden parent case. Hidden tests check only documented behavior and add
no new requirements. A student's score is the percentage of passing tests.

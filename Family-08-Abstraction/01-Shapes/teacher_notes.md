# Teacher Notes — Shapes

> Family 08 · Abstraction · Assessment 01 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students implement an abstract method declared by a base class. The `Shape`
class defines the `area` method but does not implement it; each subclass fills in
its own formula.

## Concepts Reinforced

- Abstraction (a base class declares an interface; subclasses implement it)
- Abstract methods (a method that raises `NotImplementedError`)
- Inheritance (`Rectangle` and `Triangle` extend `Shape`)
- Subclasses
- Classes and objects
- `super().__init__`

## Common Student Mistakes

- Not implementing `area` in a subclass (so it inherits the `raise` from
  `Shape`).
- Forgetting `super().__init__(name)` (so `get_name` and `name` break).
- Using the wrong formula (for example, `Rectangle` returning `base * height`).
- Integer-division mistakes in `Triangle` (using `/` instead of `//`, or
  dividing before multiplying).

## Suggested Teaching Strategy

1. Explain that `Shape.area` raises an error on purpose — the base defines the
   contract (every shape has an area) without saying how to compute it.
2. Show that each subclass overrides `area` with its own formula.
3. Trace the example: a `Rectangle("R1", 4, 5)` returns `4 * 5 = 20`; a
   `Triangle("T1", 6, 4)` returns `6 * 4 // 2 = 12`.
4. Emphasize `super().__init__(name)` so the subclass reuses the base setup and
   inherits `get_name`.
5. Have students run the tests to confirm both subclasses compute `area`
   correctly and inherit from `Shape`.

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests grouped into `Rectangle`,
`Triangle`, inheritance, and hidden cases. Hidden tests check only documented
behavior and add no new requirements. A student's score is the percentage of
passing tests.

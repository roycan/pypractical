# Teacher Notes — Fabric Order

> Family 08 · Abstraction · Assessment 03 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students implement an abstract method declared by a base class. The `Cloth`
class defines the `units` method but does not implement it; each subclass fills
in its own formula.

## Concepts Reinforced

- Abstraction (a base class declares an interface; subclasses implement it)
- Abstract methods (a method that raises `NotImplementedError`)
- Inheritance (`FullRoll` and `HalfRoll` extend `Cloth`)
- Subclasses
- Classes and objects
- `super().__init__`

## Common Student Mistakes

- Not implementing `units` in a subclass (so it inherits the `raise` from
  `Cloth`).
- Forgetting `super().__init__(name)` (so `get_name` and `name` break).
- Using the wrong formula (for example, `HalfRoll` returning `length * width`
  without the `// 2`).
- Integer-division mistakes in `HalfRoll` (using `/` instead of `//`, or
  dividing before multiplying).

## Suggested Teaching Strategy

1. Explain that `Cloth.units` raises an error on purpose — the base defines the
   contract (every order has a unit count) without saying how to compute it.
2. Show that each subclass overrides `units` with its own formula.
3. Trace the example: a `FullRoll("C1", 4, 5)` returns `4 * 5 = 20`; a
   `HalfRoll("C2", 6, 4)` returns `6 * 4 // 2 = 12`.
4. Emphasize `super().__init__(name)` so the subclass reuses the base setup and
   inherits `get_name`.
5. Have students run the tests to confirm both subclasses compute `units`
   correctly and inherit from `Cloth`.

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests grouped into `FullRoll`,
`HalfRoll`, inheritance, and hidden cases. Hidden tests check only documented
behavior and add no new requirements. A student's score is the percentage of
passing tests.

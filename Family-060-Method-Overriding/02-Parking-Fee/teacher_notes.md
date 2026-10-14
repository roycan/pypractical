# Teacher Notes — Parking Fee

> Family 06 · Method Overriding · Assessment 02 · Difficulty 3/5 · ~20 minutes

## Learning Objective

Students write a subclass that calls `super().__init__` and overrides a parent
method with a different calculation.

## Concepts Reinforced

- Method overriding
- Inheritance
- Subclasses
- Classes and objects
- Methods

## Common Student Mistakes

- Forgetting `super().__init__(name, hours)`, so the child has no data.
- Giving the override a different method name, so it does not actually override.
- Calling the parent's method (`super().fee()`) instead of replacing it.
- Forgetting `self` in the method definition.
- Trying to modify the provided `Vehicle` class.

## Suggested Teaching Strategy

1. Show the same method name (`fee`) returning different values for the parent
   and the child.
2. Trace `vehicle.fee()` -> `4 * 5 = 20` and `truck.fee()` -> `4 * 8 = 32`.
3. Stress that overriding means the child uses the SAME method name with its OWN
   body.
4. Remind students to reuse the parent's data via `super().__init__`.

## Automatic Assessment

`tests.py` runs 11 behavior tests grouped into base method, override, inherited
methods, and hidden tests. Hidden tests check only documented behavior and add
no new requirements. A student's score is the percentage of passing tests.

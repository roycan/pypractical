# Teacher Notes — Vehicle Hierarchy

> Family 05 · Inheritance · Assessment 02 · Difficulty 2/5 · ~20 minutes

## Learning Objective

Students write a subclass that inherits a provided parent's methods and adds a
new attribute and getter.

## Concepts Reinforced

- Inheritance
- Subclasses
- Classes and objects
- Methods
- Constructors
- `super().__init__(...)`

## Common Student Mistakes

- Forgetting `(Vehicle)` when declaring the child class.
- Forgetting to call `super().__init__(brand, year)`.
- Redefining `get_brand` or `get_year` in the child instead of inheriting them.
- Shadowing a parent attribute by hand instead of calling `super()`.

## Suggested Teaching Strategy

1. Emphasize that a `Motorcycle` "is a" `Vehicle` (an is-a relationship).
2. Show that a `Motorcycle` automatically receives `get_brand` and `get_year`
   through inheritance.
3. Trace `super().__init__(brand, year)`: the parent sets `brand` and `year`,
   and the child adds `engine_type`.
4. Have students confirm that the inherited-method tests would fail if
   inheritance were removed.

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests: inherited methods, the child's
own method, the parent still working, the is-a relationship, independence of
two objects, and hidden cases. Hidden tests check only documented behavior and
add no new requirements. A student's score is the percentage of passing tests.

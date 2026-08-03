# Teacher Notes — Team Roster

> Family 05 · Inheritance · Assessment 03 · Difficulty 2/5 · ~20 minutes

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

- Forgetting `(Player)` when declaring the child class.
- Forgetting to call `super().__init__(name, number)`.
- Redefining `get_name` or `get_number` in the child instead of inheriting them.
- Shadowing a parent attribute by hand instead of calling `super()`.

## Suggested Teaching Strategy

1. Emphasize that a `Captain` "is a" `Player` (an is-a relationship).
2. Show that a `Captain` automatically receives `get_name` and `get_number`
   through inheritance.
3. Trace `super().__init__(name, number)`: the parent sets `name` and `number`,
   and the child adds `team`.
4. Have students confirm that the inherited-method tests would fail if
   inheritance were removed.

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests: inherited methods, the child's
own method, the parent still working, the is-a relationship, independence of
two objects, and hidden cases. Hidden tests check only documented behavior and
add no new requirements. A student's score is the percentage of passing tests.

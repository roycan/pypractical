# Teacher Notes — Staff Hierarchy

> Family 05 · Inheritance · Assessment 01 · Difficulty 2/5 · ~20 minutes

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

- Forgetting `(Employee)` when declaring the child class.
- Forgetting to call `super().__init__(name, salary)`.
- Redefining `get_name` or `get_salary` in the child instead of inheriting them.
- Shadowing a parent attribute by hand instead of calling `super()`.

## Suggested Teaching Strategy

1. Emphasize that a `Manager` "is an" `Employee` (an is-a relationship).
2. Show that a `Manager` automatically receives `get_name` and `get_salary`
   through inheritance.
3. Trace `super().__init__(name, salary)`: the parent sets `name` and `salary`,
   and the child adds `department`.
4. Have students confirm that the inherited-method tests would fail if
   inheritance were removed.

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests: inherited methods, the child's
own method, the parent still working, the is-a relationship, independence of
two objects, and hidden cases. Hidden tests check only documented behavior and
add no new requirements. A student's score is the percentage of passing tests.

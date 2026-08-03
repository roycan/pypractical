# Teacher Notes — Pet Registry

> Family 05 · Inheritance · Assessment 04 · Difficulty 2/5 · ~20 minutes

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

- Forgetting `(Animal)` when declaring the child class.
- Forgetting to call `super().__init__(species, age)`.
- Redefining `get_species` or `get_age` in the child instead of inheriting them.
- Shadowing a parent attribute by hand instead of calling `super()`.

## Suggested Teaching Strategy

1. Emphasize that a `Pet` "is an" `Animal` (an is-a relationship).
2. Show that a `Pet` automatically receives `get_species` and `get_age`
   through inheritance.
3. Trace `super().__init__(species, age)`: the parent sets `species` and `age`,
   and the child adds `owner`.
4. Have students confirm that the inherited-method tests would fail if
   inheritance were removed.

## Automatic Assessment

`tests.py` runs 11 equal-weight behavior tests: inherited methods, the child's
own method, the parent still working, the is-a relationship, independence of
two objects, and hidden cases. Hidden tests check only documented behavior and
add no new requirements. A student's score is the percentage of passing tests.

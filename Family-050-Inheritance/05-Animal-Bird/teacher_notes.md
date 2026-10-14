# Teacher Notes — Animal Bird

> Family 05 · Inheritance · Assessment 05 · Difficulty 2/5 · ~15 minutes

## Learning Objective

Students write a subclass that inherits a provided parent's methods and adds a
new attribute, getter, and a describe method that uses all three values.

## Concepts Reinforced

- Inheritance
- Subclasses
- Classes and objects
- Methods
- Constructors
- `super().__init__(...)`
- String formatting (f-strings)

## Common Student Mistakes

- Forgetting `(Animal)` when declaring the child class.
- Forgetting to call `super().__init__(name, species)`.
- Redefining `get_name` or `get_species` in the child instead of inheriting them.
- Using `self.name` and `self.species` in `describe` without calling `super()`
  first — those attributes won't exist.
- Forgetting the space before "cm" in the describe string.

## Suggested Teaching Strategy

1. Emphasize that a `Bird` "is an" `Animal` (an is-a relationship).
2. Show that a `Bird` automatically receives `get_name` and `get_species`
   through inheritance.
3. Trace `super().__init__(name, species)`: the parent sets `name` and `species`,
   and the child adds `wingspan`.
4. Have students confirm that the inherited-method tests would fail if
   inheritance were removed.
5. For `describe`, remind students about f-strings: `f"{self.name} is a ..."`.

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests: inherited methods, the child's
own methods, the parent still working, the is-a relationship, independence of
two objects, and hidden cases. Hidden tests check only documented behavior and
add no new requirements. A student's score is the percentage of passing tests.
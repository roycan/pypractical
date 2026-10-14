# Shapes

## Story

Every shape has an area, but each kind of shape computes it differently.

The `Shape` class defines the `area` method but leaves it unimplemented —
calling it raises an error. That is the contract: the base class says every
shape **has** an area, while each subclass says **how** to compute it.

Complete the `Rectangle` and `Triangle` classes so each implements `area` its
own way.

## Task

The `Shape` class is provided and complete. Do **not** modify it.

Complete the `Rectangle` and `Triangle` classes. Each must call
`super().__init__(name)` and implement the `area` method with its own formula.

## Class Specification

### Shape (provided, do not modify)

A `Shape` object represents an abstract shape.

It stores:

- the shape's name (`name`)

It provides a `get_name` method that returns the name. Its `area` method is
**not** implemented — calling it raises an error. Subclasses must implement
`area` themselves.

### Rectangle

A `Rectangle` object represents a rectangle shape.

A rectangle stores:

- the shape's name (`name`, inherited from `Shape`)
- the width (`width`)
- the height (`height`)

Its `area` method returns `width * height`.

### Triangle

A `Triangle` object represents a triangle shape.

A triangle stores:

- the shape's name (`name`, inherited from `Shape`)
- the base (`base`)
- the height (`height`)

Its `area` method returns `base * height // 2`.

## Required Methods

### Rectangle.__init__(name, width, height)

Call `super().__init__(name)`, then store `width` and `height` as instance
variables.

### Rectangle.area()

Return the area of this rectangle as `width * height`.

### Triangle.__init__(name, base, height)

Call `super().__init__(name)`, then store `base` and `height` as instance
variables.

### Triangle.area()

Return the area of this triangle as `base * height // 2` (integer division,
rounded down).

## Constraints

- `name` is a non-empty string
- `width`, `height`, and `base` are positive integers
- Triangle area uses integer division (rounded down)
- All inputs are valid

## Example

```python
rectangle = Rectangle("R1", 4, 5)
print(rectangle.get_name())
print(rectangle.area())

triangle = Triangle("T1", 6, 4)
print(triangle.get_name())
print(triangle.area())
```

Output

```text
R1
20
T1
12
```

## Explanation

The base `Shape` defines `area` but does **not** implement it (calling it raises
an error) — that is abstraction: the base says every shape **has** an area, while
each subclass says **how** to compute it.

`Rectangle` uses `width * height = 4 * 5 = 20`.

`Triangle` uses `base * height // 2 = 6 * 4 // 2 = 12`.

## Hint

Each subclass calls `super().__init__(name)` to reuse the base, stores its own
measurements, then implements `area` with its own formula.

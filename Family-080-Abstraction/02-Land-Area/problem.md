# Land Area

## Story

A land registry records plots of land. Every plot has an area, but a rectangular
plot and a triangular plot compute it differently.

The `Plot` class defines the `area` method but leaves it unimplemented — calling
it raises an error. That is the contract: the base class says every plot **has**
an area, while each subclass says **how** to compute it.

Complete the `Rectangular` and `Triangular` classes so each implements `area`
its own way.

## Task

The `Plot` class is provided and complete. Do **not** modify it.

Complete the `Rectangular` and `Triangular` classes. Each must call
`super().__init__(name)` and implement the `area` method with its own formula.

## Class Specification

### Plot (provided, do not modify)

A `Plot` object represents an abstract plot of land.

It stores:

- the plot's name (`name`)

It provides a `get_name` method that returns the name. Its `area` method is
**not** implemented — calling it raises an error. Subclasses must implement
`area` themselves.

### Rectangular

A `Rectangular` object represents a rectangular plot.

A rectangular plot stores:

- the plot's name (`name`, inherited from `Plot`)
- the length (`length`)
- the width (`width`)

Its `area` method returns `length * width`.

### Triangular

A `Triangular` object represents a triangular plot.

A triangular plot stores:

- the plot's name (`name`, inherited from `Plot`)
- the base (`base`)
- the height (`height`)

Its `area` method returns `base * height // 2`.

## Required Methods

### Rectangular.__init__(name, length, width)

Call `super().__init__(name)`, then store `length` and `width` as instance
variables.

### Rectangular.area()

Return the area of this plot as `length * width`.

### Triangular.__init__(name, base, height)

Call `super().__init__(name)`, then store `base` and `height` as instance
variables.

### Triangular.area()

Return the area of this plot as `base * height // 2` (integer division, rounded
down).

## Constraints

- `name` is a non-empty string
- `length`, `width`, `base`, and `height` are positive integers
- Triangular area uses integer division (rounded down)
- All inputs are valid

## Example

```python
rectangular = Rectangular("P1", 4, 5)
print(rectangular.get_name())
print(rectangular.area())

triangular = Triangular("P2", 6, 4)
print(triangular.get_name())
print(triangular.area())
```

Output

```text
P1
20
P2
12
```

## Explanation

The base `Plot` defines `area` but does **not** implement it (calling it raises
an error) — that is abstraction: the base says every plot **has** an area, while
each subclass says **how** to compute it.

`Rectangular` uses `length * width = 4 * 5 = 20`.

`Triangular` uses `base * height // 2 = 6 * 4 // 2 = 12`.

## Hint

Each subclass calls `super().__init__(name)` to reuse the base, stores its own
measurements, then implements `area` with its own formula.

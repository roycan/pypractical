# Screen Grid

## Story

A device maker tests screens for its products. Every screen has a pixel count,
but a standard screen and a compact screen compute it differently.

The `Screen` class defines the `pixels` method but leaves it unimplemented —
calling it raises an error. That is the contract: the base class says every
screen **has** a pixel count, while each subclass says **how** to compute it.

Complete the `Standard` and `Compact` classes so each implements `pixels` its
own way.

## Task

The `Screen` class is provided and complete. Do **not** modify it.

Complete the `Standard` and `Compact` classes. Each must call
`super().__init__(name)` and implement the `pixels` method with its own formula.

## Class Specification

### Screen (provided, do not modify)

A `Screen` object represents an abstract screen.

It stores:

- the screen's name (`name`)

It provides a `get_name` method that returns the name. Its `pixels` method is
**not** implemented — calling it raises an error. Subclasses must implement
`pixels` themselves.

### Standard

A `Standard` object represents a standard screen.

A standard screen stores:

- the screen's name (`name`, inherited from `Screen`)
- the number of rows (`rows`)
- the number of columns (`cols`)

Its `pixels` method returns `rows * cols`.

### Compact

A `Compact` object represents a compact screen.

A compact screen stores:

- the screen's name (`name`, inherited from `Screen`)
- the number of rows (`rows`)
- the number of columns (`cols`)

Its `pixels` method returns `rows * cols // 2`.

## Required Methods

### Standard.__init__(name, rows, cols)

Call `super().__init__(name)`, then store `rows` and `cols` as instance
variables.

### Standard.pixels()

Return the pixel count of this screen as `rows * cols`.

### Compact.__init__(name, rows, cols)

Call `super().__init__(name)`, then store `rows` and `cols` as instance
variables.

### Compact.pixels()

Return the pixel count of this screen as `rows * cols // 2` (integer division,
rounded down).

## Constraints

- `name` is a non-empty string
- `rows` and `cols` are positive integers
- Compact pixel count uses integer division (rounded down)
- All inputs are valid

## Example

```python
standard = Standard("S1", 4, 5)
print(standard.get_name())
print(standard.pixels())

compact = Compact("S2", 6, 4)
print(compact.get_name())
print(compact.pixels())
```

Output

```text
S1
20
S2
12
```

## Explanation

The base `Screen` defines `pixels` but does **not** implement it (calling it
raises an error) — that is abstraction: the base says every screen **has** a
pixel count, while each subclass says **how** to compute it.

`Standard` uses `rows * cols = 4 * 5 = 20`.

`Compact` uses `rows * cols // 2 = 6 * 4 // 2 = 12`.

## Hint

Each subclass calls `super().__init__(name)` to reuse the base, stores its own
dimensions, then implements `pixels` with its own formula.

# Fabric Order

## Story

A tailor orders cloth for garments. Every order has a number of units, but a
full roll and a half roll compute it differently.

The `Cloth` class defines the `units` method but leaves it unimplemented —
calling it raises an error. That is the contract: the base class says every
order **has** a unit count, while each subclass says **how** to compute it.

Complete the `FullRoll` and `HalfRoll` classes so each implements `units` its
own way.

## Task

The `Cloth` class is provided and complete. Do **not** modify it.

Complete the `FullRoll` and `HalfRoll` classes. Each must call
`super().__init__(name)` and implement the `units` method with its own formula.

## Class Specification

### Cloth (provided, do not modify)

A `Cloth` object represents an abstract cloth order.

It stores:

- the order's name (`name`)

It provides a `get_name` method that returns the name. Its `units` method is
**not** implemented — calling it raises an error. Subclasses must implement
`units` themselves.

### FullRoll

A `FullRoll` object represents a full roll of cloth.

A full roll stores:

- the order's name (`name`, inherited from `Cloth`)
- the length (`length`)
- the width (`width`)

Its `units` method returns `length * width`.

### HalfRoll

A `HalfRoll` object represents a half roll of cloth.

A half roll stores:

- the order's name (`name`, inherited from `Cloth`)
- the length (`length`)
- the width (`width`)

Its `units` method returns `length * width // 2`.

## Required Methods

### FullRoll.__init__(name, length, width)

Call `super().__init__(name)`, then store `length` and `width` as instance
variables.

### FullRoll.units()

Return the units of this roll as `length * width`.

### HalfRoll.__init__(name, length, width)

Call `super().__init__(name)`, then store `length` and `width` as instance
variables.

### HalfRoll.units()

Return the units of this roll as `length * width // 2` (integer division,
rounded down).

## Constraints

- `name` is a non-empty string
- `length` and `width` are positive integers
- HalfRoll units uses integer division (rounded down)
- All inputs are valid

## Example

```python
full = FullRoll("C1", 4, 5)
print(full.get_name())
print(full.units())

half = HalfRoll("C2", 6, 4)
print(half.get_name())
print(half.units())
```

Output

```text
C1
20
C2
12
```

## Explanation

The base `Cloth` defines `units` but does **not** implement it (calling it raises
an error) — that is abstraction: the base says every order **has** a unit count,
while each subclass says **how** to compute it.

`FullRoll` uses `length * width = 4 * 5 = 20`.

`HalfRoll` uses `length * width // 2 = 6 * 4 // 2 = 12`.

## Hint

Each subclass calls `super().__init__(name)` to reuse the base, stores its own
measurements, then implements `units` with its own formula.

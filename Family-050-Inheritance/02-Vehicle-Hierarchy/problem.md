# Vehicle Hierarchy

## Story

Every motorcycle is also a vehicle. The `Vehicle` class has already been written
and stores a vehicle's brand and year.

A motorcycle inherits the vehicle's brand and year, and adds an engine type.

## Task

The `Vehicle` class is provided and complete. Do **not** modify it.

Complete the `Motorcycle` class so a motorcycle inherits `get_brand` and
`get_year` from `Vehicle` and also stores an `engine_type`.

## Class Specification

### Vehicle (provided, do not modify)

A `Vehicle` object represents one basic vehicle.

Each vehicle stores:

- the vehicle's brand (`brand`)
- the vehicle's year (`year`)

### Motorcycle

A `Motorcycle` object represents one vehicle with a specific engine type.

Each motorcycle should remember:

- the inherited vehicle's brand and year
- an engine type (`engine_type`)

## Required Methods

### Motorcycle.__init__(brand, year, engine_type)

Call `super().__init__(brand, year)` to reuse the parent, then store the
motorcycle's `engine_type`.

### Motorcycle.get_engine_type()

Return the motorcycle's `engine_type`.

## Constraints

- brand is a non-empty string
- year is a positive integer
- engine_type is a non-empty string

All inputs are valid.

## Example

```python
vehicle = Vehicle("Honda", 2020)
print(vehicle.get_brand())
print(vehicle.get_year())

motorcycle = Motorcycle("Yamaha", 2022, "V-Twin")
print(motorcycle.get_brand())
print(motorcycle.get_year())
print(motorcycle.get_engine_type())
```

Output

```text
Honda
2020
Yamaha
2022
V-Twin
```

## Explanation

A `Motorcycle` inherits `get_brand` and `get_year` from `Vehicle`, so
`motorcycle.get_brand()` returns `"Yamaha"` and `motorcycle.get_year()` returns
`2022` even though `Motorcycle` does not define those methods. `Motorcycle`
adds its own `engine_type`, returned by `get_engine_type`. That is inheritance:
the child reuses the parent and adds something new.

## Hint

In the child `__init__`, call `super().__init__(brand, year)` to reuse the
parent, then set the new attribute with `self.engine_type = engine_type`.

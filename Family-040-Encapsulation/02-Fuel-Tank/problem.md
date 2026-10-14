# Fuel Tank

## Story

A fuel tank must never go below zero and must ignore invalid refuels or draws.

The litres are protected inside the object. They are read with `get_litres` and
changed only through `add_fuel` and `draw_fuel`.

## Task

Complete the `FuelTank` class so a tank protects its own litres.

## Class Specification

### FuelTank

A `FuelTank` object represents one fuel tank.

Each tank stores:

- the tank's name (`name`)
- protected litres (`_litres`)

## Required Methods

### FuelTank.__init__(name, starting_litres)

Store the tank's name as `name`. Store the starting litres as a protected
attribute `_litres`.

### FuelTank.get_litres()

Return the protected `_litres`.

### FuelTank.add_fuel(litres)

If `litres` is greater than `0`, add `litres` to `_litres`. Otherwise do
nothing.

### FuelTank.draw_fuel(litres)

If `litres` is greater than `0` and less than or equal to `_litres`, subtract
`litres` from `_litres`. Otherwise do nothing.

## Constraints

- name is a non-empty string
- starting_litres is a non-negative integer
- add_fuel and draw_fuel amounts are integers
- a draw that exceeds the litres is ignored
- amounts of zero or less are ignored

All inputs are valid integers.

## Example

```python
tank = FuelTank("Tank A", 1000)

print(tank.name)
print(tank.get_litres())

tank.add_fuel(500)
print(tank.get_litres())

tank.draw_fuel(300)
print(tank.get_litres())
```

Output

```text
Tank A
1000
1500
1200
```

## Explanation

The tank starts with `1000` litres. After refuelling with `500`, the litres
are `1500`. After drawing `300`, the litres are `1200`. The litres are
protected: they only change through `add_fuel` and `draw_fuel`, so they can
never become negative.

## Hint

Protect the litres with a leading underscore (`_litres`). Read it with
`get_litres`, and change it only inside `add_fuel` and `draw_fuel`.

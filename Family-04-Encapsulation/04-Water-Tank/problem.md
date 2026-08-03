# Water Tank

## Story

A water tank must never go below zero and must ignore invalid fills or drains.

The litres are protected inside the object. They are read with `get_litres` and
changed only through `fill` and `drain`.

## Task

Complete the `WaterTank` class so a tank protects its own litres.

## Class Specification

### WaterTank

A `WaterTank` object represents one water tank.

Each tank stores:

- the tank's name (`name`)
- protected litres (`_litres`)

## Required Methods

### WaterTank.__init__(name, starting_litres)

Store the tank's name as `name`. Store the starting litres as a protected
attribute `_litres`.

### WaterTank.get_litres()

Return the protected `_litres`.

### WaterTank.fill(litres)

If `litres` is greater than `0`, add `litres` to `_litres`. Otherwise do
nothing.

### WaterTank.drain(litres)

If `litres` is greater than `0` and less than or equal to `_litres`, subtract
`litres` from `_litres`. Otherwise do nothing.

## Constraints

- name is a non-empty string
- starting_litres is a non-negative integer
- fill and drain amounts are integers
- a drain that exceeds the litres is ignored
- amounts of zero or less are ignored

All inputs are valid integers.

## Example

```python
tank = WaterTank("Reservoir A", 1000)

print(tank.name)
print(tank.get_litres())

tank.fill(500)
print(tank.get_litres())

tank.drain(300)
print(tank.get_litres())
```

Output

```text
Reservoir A
1000
1500
1200
```

## Explanation

The tank starts with `1000` litres. After filling with `500`, the litres are
`1500`. After draining `300`, the litres are `1200`. The litres are
protected: they only change through `fill` and `drain`, so they can never
become negative.

## Hint

Protect the litres with a leading underscore (`_litres`). Read it with
`get_litres`, and change it only inside `fill` and `drain`.

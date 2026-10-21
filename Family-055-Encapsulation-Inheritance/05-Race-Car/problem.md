# Race Car

## Story

A racing team keeps track of its vehicles. Every vehicle has a name and a maximum
speed. A racer also has a top speed, but the team must never record a top speed
above the vehicle's maximum — that would be impossible for the car to reach.

## Task

The `Vehicle` class is provided and complete. Do **not** modify it.

Complete the `Racer` class so a racer inherits the vehicle's name and maximum
speed and caps its own top speed against them.

## Class Specification

### Vehicle (provided, do not modify)

A `Vehicle` object represents one vehicle.

Each vehicle stores:

- the vehicle's name (`name`)
- the vehicle's maximum speed (`max_speed`)

### Racer

A `Racer` object represents one race car. A racer IS-A vehicle.

Each racer should remember:

- the inherited vehicle's name and maximum speed
- a protected top speed (`_top_speed`)

## Required Methods

### Racer.\_\_init\_\_(name, max_speed, top_speed)

Call `super().__init__(name, max_speed)` so the racer inherits the name and
maximum speed. Then validate the top speed **against the parent's maximum**:

- if `top_speed` is less than or equal to `self.max_speed`, store the value in
  the protected attribute `_top_speed`
- otherwise print `"The top speed cannot exceed the maximum speed"` and store
  `self.max_speed` as the fallback

### Racer.get_top_speed()

Return the protected `_top_speed`.

## Constraints

- name is a non-empty string
- max_speed is a positive integer
- top_speed is an integer (it may exceed max_speed — the constructor must handle
  that case)

## Example

```python
vehicle = Vehicle("Sedan", 180)
print(vehicle.display_info())

racer = Racer("Bolt", 200, 190)
print(racer.display_info())
print(racer.get_top_speed())

bad_racer = Racer("Dash", 150, 170)
print(bad_racer.get_top_speed())
```

Output

```text
Vehicle: Sedan, Max speed: 180
Vehicle: Bolt, Max speed: 200
190
The top speed cannot exceed the maximum speed
150
```

## Explanation

`vehicle` is a plain `Vehicle`. The `racer` is a `Racer`, so it is also a
vehicle: its `name` and `max_speed` come from the parent through
`super().__init__(name, max_speed)`, and its `display_info()` is the parent's
method, reused unchanged. The `racer` proposes `190`, which does not exceed its
maximum `200`, so `190` is stored. `bad_racer` proposes `170` against a maximum
of `150`, so the constructor prints a warning and stores the parent's
`max_speed` (`150`) — the impossible value is capped against the parent's data,
not silently kept.

## Hint

Write `class Racer(Vehicle):` so the racer inherits from the parent. In
`__init__`, call `super().__init__(name, max_speed)` first. Then compare
`top_speed` with `self.max_speed` using `<=` before storing it in
`self._top_speed` — a top speed equal to the maximum is allowed, but anything
above it is not.

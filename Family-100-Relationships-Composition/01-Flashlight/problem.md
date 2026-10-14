# Flashlight

## Story

A flashlight is built with its own batteries — the flashlight creates the
batteries that belong to it. They do not exist on their own.

That is composition: a whole object creates and owns its parts. The `Battery`
class is already written. Complete the `Flashlight` class so it creates its
batteries, reports how many it has, and reports the total capacity.

## Task

The `Battery` class is provided and complete. Do **not** modify it.

Complete the `Flashlight` class. A flashlight creates its own batteries in
`__init__`, stores them in a list, reports how many batteries it holds, and
reports their total capacity.

## Class Specification

### Battery (provided, do not modify)

A `Battery` object represents one battery inside a flashlight.

It stores:

- the capacity (`capacity`)

It provides `get_capacity` (returns the capacity).

### Flashlight

A `Flashlight` object represents one flashlight that owns its batteries.

It stores:

- a list of batteries (`batteries`)

Initially the list is empty; the flashlight fills it itself in `__init__`.

## Required Methods

### Flashlight.__init__(battery_count, capacity)

- Create an empty list named `batteries`.
- Loop `battery_count` times. Each time, create a new `Battery(capacity)` and
  append it to `batteries`.

### Flashlight.count_batteries()

Return the number of batteries the flashlight holds.

### Flashlight.total_capacity()

Loop over `batteries`. Add each battery's capacity to a running total, then
return the total.

## Constraints

- `battery_count` is zero or a positive integer
- `capacity` is a positive integer
- All inputs are valid

## Example

```python
flashlight = Flashlight(3, 100)
print(flashlight.count_batteries())
print(flashlight.total_capacity())
```

Output

```text
3
300
```

## Explanation

In `__init__`, the flashlight creates 3 `Battery` objects, each of capacity 100,
and stores them in its own list. `count_batteries` returns 3. `total_capacity`
adds every battery's capacity: `100 + 100 + 100 = 300`. Because the flashlight
creates the batteries itself, the batteries are part of the flashlight — that is
composition.

## Hint

In `__init__`, create an empty list `self.batteries`, then use
`for i in range(battery_count):` to append a new `Battery(capacity)` each time.

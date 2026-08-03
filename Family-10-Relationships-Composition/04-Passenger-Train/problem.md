# Passenger Train

## Story

A train is built with its own carriages — the train creates the carriages that
belong to it. They do not exist on their own.

That is composition: a whole object creates and owns its parts. The `Carriage`
class is already written. Complete the `Train` class so it creates its carriages,
reports how many it has, and reports the total seats.

## Task

The `Carriage` class is provided and complete. Do **not** modify it.

Complete the `Train` class. A train creates its own carriages in `__init__`,
stores them in a list, reports how many carriages it holds, and reports their
total seats.

## Class Specification

### Carriage (provided, do not modify)

A `Carriage` object represents one passenger carriage inside a train.

It stores:

- the number of seats (`seats`)

It provides `get_seats` (returns the number of seats).

### Train

A `Train` object represents one train that owns its carriages.

It stores:

- a list of carriages (`carriages`)

Initially the list is empty; the train fills it itself in `__init__`.

## Required Methods

### Train.__init__(carriage_count, seats)

- Create an empty list named `carriages`.
- Loop `carriage_count` times. Each time, create a new `Carriage(seats)` and
  append it to `carriages`.

### Train.count_carriages()

Return the number of carriages the train holds.

### Train.total_seats()

Loop over `carriages`. Add each carriage's seats to a running total, then return
the total.

## Constraints

- `carriage_count` is zero or a positive integer
- `seats` is a positive integer
- All inputs are valid

## Example

```python
train = Train(3, 100)
print(train.count_carriages())
print(train.total_seats())
```

Output

```text
3
300
```

## Explanation

In `__init__`, the train creates 3 `Carriage` objects, each with 100 seats, and
stores them in its own list. `count_carriages` returns 3. `total_seats` adds
every carriage's seats: `100 + 100 + 100 = 300`. Because the train creates the
carriages itself, the carriages are part of the train — that is composition.

## Hint

In `__init__`, create an empty list `self.carriages`, then use
`for i in range(carriage_count):` to append a new `Carriage(seats)` each time.

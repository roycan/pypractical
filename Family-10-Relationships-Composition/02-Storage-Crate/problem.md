# Storage Crate

## Story

A crate is packed with its own boxes — the crate creates the boxes that belong
to it. They do not exist on their own.

That is composition: a whole object creates and owns its parts. The `Box` class
is already written. Complete the `Crate` class so it creates its boxes, reports
how many it has, and reports the total size.

## Task

The `Box` class is provided and complete. Do **not** modify it.

Complete the `Crate` class. A crate creates its own boxes in `__init__`, stores
them in a list, reports how many boxes it holds, and reports their total size.

## Class Specification

### Box (provided, do not modify)

A `Box` object represents one box inside a crate.

It stores:

- the size (`size`)

It provides `get_size` (returns the size).

### Crate

A `Crate` object represents one crate that owns its boxes.

It stores:

- a list of boxes (`boxes`)

Initially the list is empty; the crate fills it itself in `__init__`.

## Required Methods

### Crate.__init__(box_count, size)

- Create an empty list named `boxes`.
- Loop `box_count` times. Each time, create a new `Box(size)` and append it to
  `boxes`.

### Crate.count_boxes()

Return the number of boxes the crate holds.

### Crate.total_size()

Loop over `boxes`. Add each box's size to a running total, then return the
total.

## Constraints

- `box_count` is zero or a positive integer
- `size` is a positive integer
- All inputs are valid

## Example

```python
crate = Crate(3, 100)
print(crate.count_boxes())
print(crate.total_size())
```

Output

```text
3
300
```

## Explanation

In `__init__`, the crate creates 3 `Box` objects, each of size 100, and stores
them in its own list. `count_boxes` returns 3. `total_size` adds every box's
size: `100 + 100 + 100 = 300`. Because the crate creates the boxes itself, the
boxes are part of the crate — that is composition.

## Hint

In `__init__`, create an empty list `self.boxes`, then use
`for i in range(box_count):` to append a new `Box(size)` each time.

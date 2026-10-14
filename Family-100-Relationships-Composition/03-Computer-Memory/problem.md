# Computer Memory

## Story

A computer is assembled with its own memory modules — the computer creates the
modules that belong to it. They do not exist on their own.

That is composition: a whole object creates and owns its parts. The `Module`
class is already written. Complete the `Computer` class so it creates its
modules, reports how many it has, and reports the total memory.

## Task

The `Module` class is provided and complete. Do **not** modify it.

Complete the `Computer` class. A computer creates its own memory modules in
`__init__`, stores them in a list, reports how many modules it holds, and reports
their total memory.

## Class Specification

### Module (provided, do not modify)

A `Module` object represents one memory module inside a computer.

It stores:

- the size (`size`)

It provides `get_size` (returns the size).

### Computer

A `Computer` object represents one computer that owns its memory modules.

It stores:

- a list of modules (`modules`)

Initially the list is empty; the computer fills it itself in `__init__`.

## Required Methods

### Computer.__init__(module_count, size)

- Create an empty list named `modules`.
- Loop `module_count` times. Each time, create a new `Module(size)` and append it
  to `modules`.

### Computer.count_modules()

Return the number of modules the computer holds.

### Computer.total_memory()

Loop over `modules`. Add each module's size to a running total, then return the
total.

## Constraints

- `module_count` is zero or a positive integer
- `size` is a positive integer
- All inputs are valid

## Example

```python
computer = Computer(3, 100)
print(computer.count_modules())
print(computer.total_memory())
```

Output

```text
3
300
```

## Explanation

In `__init__`, the computer creates 3 `Module` objects, each of size 100, and
stores them in its own list. `count_modules` returns 3. `total_memory` adds every
module's size: `100 + 100 + 100 = 300`. Because the computer creates the modules
itself, the modules are part of the computer — that is composition.

## Hint

In `__init__`, create an empty list `self.modules`, then use
`for i in range(module_count):` to append a new `Module(size)` each time.

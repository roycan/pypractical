# Computer Peripherals

## Story

A computer has peripherals — a keyboard, a mouse, a monitor. The peripherals are
manufactured separately and can exist without the computer. The computer stores
them but does not create them. That is aggregation: the whole holds the parts,
but the parts can live on their own.

## Task

The `Peripheral` class is provided and complete. Do **not** modify it.

Complete the `Computer` class so a computer can add peripherals, remove them by
name, count them, list their names, and check whether it has a peripheral of a
given type.

## Class Specification

### Peripheral (provided, do not modify)

A `Peripheral` object represents one device connected to a computer.

It stores:

- the peripheral's name (`name`)
- the device type (`device_type`)

It provides `get_name` (returns the name) and `get_type` (returns the type).

### Computer

A `Computer` object represents one computer.

It stores:

- the computer's name (`name`)
- a list of peripherals (`peripherals`)

Initially the list is empty.

## Required Methods

### Computer.__init__(name)

Store the computer's name and create an empty list named `peripherals`.

### Computer.add_peripheral(peripheral)

Append the given peripheral to the end of `peripherals`.

### Computer.remove_peripheral(name)

Loop over `peripherals`. If a peripheral with the given name is found, remove it
and return `True`. If no peripheral matches, return `False`.

### Computer.count_peripherals()

Return the number of peripherals stored.

### Computer.list_peripheral_names()

Return a list containing the name of every peripheral.

### Computer.has_type(device_type)

Return `True` if at least one peripheral has the given type. Otherwise return
`False`.

## Constraints

- name and device_type are non-empty strings
- Peripheral names are unique
- All inputs are valid

## Example

```python
computer = Computer("MyPC")
computer.add_peripheral(Peripheral("Logitech K120", "keyboard"))
computer.add_peripheral(Peripheral("Razer DeathAdder", "mouse"))
print(computer.count_peripherals())
print(computer.list_peripheral_names())
print(computer.has_type("mouse"))
print(computer.has_type("monitor"))
print(computer.remove_peripheral("Logitech K120"))
print(computer.count_peripherals())
```

Output

```text
2
['Logitech K120', 'Razer DeathAdder']
True
False
True
1
```

## Explanation

The computer starts empty. Two peripherals are added — a keyboard and a mouse —
so `count_peripherals` returns 2 and `list_peripheral_names` returns both names.
`has_type("mouse")` returns `True` because the mouse is present, but
`has_type("monitor")` returns `False`. After removing the keyboard,
`count_peripherals` returns 1. The peripherals were created outside the computer
and passed in — that is aggregation.

## Hint

In `remove_peripheral`, loop over `self.peripherals`, compare
`peripheral.get_name()` with the given name, and use
`self.peripherals.remove(peripheral)` on the first match. In `has_type`, loop
and compare `peripheral.get_type()` with the given type.
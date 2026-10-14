# House Rooms

## Story

A house is built with its own rooms. The rooms do not exist before the house is
built and they do not exist after the house is demolished. The house creates the
rooms itself. That is composition: the whole creates and owns its parts.

## Task

The `Room` class is provided and complete. Do **not** modify it.

Complete the `House` class so it creates its rooms from a list of
specifications, and can count them, total their area, find the largest, and list
their names.

## Class Specification

### Room (provided, do not modify)

A `Room` object represents one room in a house.

It stores:

- the room's name (`name`)
- the room's area in square meters (`area`)

It provides `get_name` (returns the name) and `get_area` (returns the area).

### House

A `House` object represents one house.

It stores:

- the house's name (`name`)
- a list of rooms (`rooms`)

The house creates its rooms itself in `__init__`.

## Required Methods

### House.__init__(name, room_specs)

Create an empty list named `rooms`. Then loop over `room_specs`, which is a list
of `(room_name, area)` tuples. For each tuple, create a `Room(room_name, area)`
and append it to `rooms`.

### House.count_rooms()

Return the number of rooms.

### House.total_area()

Loop over `rooms`. Add each room's area to a running total, then return the
total.

### House.get_largest_room()

Return the name of the room with the largest area. If there is a tie, return the
first one.

### House.list_room_names()

Return a list containing the name of every room.

## Constraints

- room_specs has at least one room
- room name is a non-empty string
- area is a positive integer
- All inputs are valid

## Example

```python
house = House("Villa", [("Kitchen", 12), ("Bedroom", 20), ("Bath", 6)])
print(house.count_rooms())
print(house.total_area())
print(house.get_largest_room())
print(house.list_room_names())
```

Output

```text
3
38
Bedroom
['Kitchen', 'Bedroom', 'Bath']
```

## Explanation

The house creates three rooms from the given tuples. `count_rooms` returns 3.
`total_area` adds every room's area: `12 + 20 + 6 = 38`. The largest room is
`Bedroom` with area 20. `list_room_names` returns all three names. Because the
house creates the rooms itself, the rooms are part of the house — that is
composition.

## Hint

In `__init__`, create an empty list `self.rooms`, then loop over `room_specs`
with `for room_name, area in room_specs:` and append a new `Room(room_name,
area)` each time. For `get_largest_room`, track the largest room and compare
`room.get_area()`.
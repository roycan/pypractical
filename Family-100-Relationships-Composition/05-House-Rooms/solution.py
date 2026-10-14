"""House Rooms -- Family 10, Assessment 05 (teacher solution)."""


# Provided class. Do NOT modify it.
class Room:
    """Represents one room in a house."""

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def get_name(self):
        """Return the room's name."""
        return self.name

    def get_area(self):
        """Return the room's area in square meters."""
        return self.area


class House:
    """Represents a house that creates its own rooms."""

    def __init__(self, name, room_specs):
        """Initialize a house and create its rooms."""
        self.name = name
        self.rooms = []
        for room_name, area in room_specs:
            self.rooms.append(Room(room_name, area))

    def count_rooms(self):
        """Return the number of rooms."""
        return len(self.rooms)

    def total_area(self):
        """Return the total area of all rooms."""
        total = 0
        for room in self.rooms:
            total = total + room.get_area()
        return total

    def get_largest_room(self):
        """Return the name of the room with the largest area."""
        largest = self.rooms[0]
        for room in self.rooms:
            if room.get_area() > largest.get_area():
                largest = room
        return largest.get_name()

    def list_room_names(self):
        """Return a list of all room names."""
        names = []
        for room in self.rooms:
            names.append(room.get_name())
        return names


if __name__ == "__main__":
    house = House("Villa", [("Kitchen", 12), ("Bedroom", 20), ("Bath", 6)])
    print(house.count_rooms())
    print(house.total_area())
    print(house.get_largest_room())
    print(house.list_room_names())
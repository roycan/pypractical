"""House Rooms -- Family 10, Assessment 05 (starter).

The Room class is provided and complete. Complete the House class.
"""


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
        """Initialize a house and create its rooms.

        Args:
            name (str): The house's name.
            room_specs (list): A list of (room_name, area) tuples.
        """

        # TODO: Write your solution here.

        return

    def count_rooms(self):
        """Return the number of rooms.

        Returns:
            int: The number of rooms.
        """

        # TODO: Write your solution here.

        return 0

    def total_area(self):
        """Return the total area of all rooms.

        Returns:
            int: The sum of all room areas.
        """

        # TODO: Write your solution here.

        return 0

    def get_largest_room(self):
        """Return the name of the room with the largest area.

        Returns:
            str: The name of the largest room, or the first on a tie.
        """

        # TODO: Write your solution here.

        return ""

    def list_room_names(self):
        """Return a list of all room names.

        Returns:
            list: A list of room name strings.
        """

        # TODO: Write your solution here.

        return []
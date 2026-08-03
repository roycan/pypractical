"""Parking Fee -- Family 06, Assessment 02 (starter).

The Vehicle class is provided and complete. Complete the Truck class.
"""


# Provided class. Do NOT modify it.
class Vehicle:
    """Represents a standard vehicle."""

    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def get_name(self):
        """Return the vehicle's name."""
        return self.name

    def get_hours(self):
        """Return the vehicle's hours."""
        return self.hours

    def fee(self):
        """Return the parking fee (5 per hour)."""
        return self.hours * 5


class Truck(Vehicle):
    """Represents a truck that pays a higher parking fee."""

    def __init__(self, name, hours):
        """Initialize a truck.

        Args:
            name (str): The truck's name.
            hours (int): The truck's hours.
        """

        # TODO: Write your solution here.

        return

    def fee(self):
        """Return the truck parking fee (8 per hour).

        Returns:
            int: The truck parking fee.
        """

        # TODO: Write your solution here.

        return 0

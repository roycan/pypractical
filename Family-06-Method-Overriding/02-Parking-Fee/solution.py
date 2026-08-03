"""Parking Fee -- Family 06, Assessment 02 (teacher solution)."""


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
        super().__init__(name, hours)

    def fee(self):
        """Return the truck parking fee (8 per hour).

        Returns:
            int: The truck parking fee.
        """
        return self.hours * 8


if __name__ == "__main__":
    vehicle = Vehicle("Sedan", 4)
    print(vehicle.get_name())
    print(vehicle.fee())

    truck = Truck("Lorry", 4)
    print(truck.get_name())
    print(truck.fee())

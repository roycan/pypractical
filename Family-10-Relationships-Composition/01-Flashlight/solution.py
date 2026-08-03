"""Flashlight -- Family 10, Assessment 01 (teacher solution)."""


# Provided class. Do NOT modify it.
class Battery:
    """Represents one battery."""

    def __init__(self, capacity):
        self.capacity = capacity

    def get_capacity(self):
        """Return the battery's capacity."""
        return self.capacity


class Flashlight:
    """Represents a flashlight that creates and owns its batteries."""

    def __init__(self, battery_count, capacity):
        """Create the batteries that belong to this flashlight.

        Args:
            battery_count (int): How many batteries to create.
            capacity (int): The capacity of each battery.
        """
        self.batteries = []
        for i in range(battery_count):
            self.batteries.append(Battery(capacity))

    def count_batteries(self):
        """Return the number of batteries in the flashlight."""
        return len(self.batteries)

    def total_capacity(self):
        """Return the total capacity of all batteries combined."""
        total = 0
        for battery in self.batteries:
            total = total + battery.get_capacity()
        return total


if __name__ == "__main__":
    flashlight = Flashlight(3, 100)
    print(flashlight.count_batteries())
    print(flashlight.total_capacity())

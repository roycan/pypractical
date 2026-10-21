"""Race Car -- Family 055, Assessment 05 (teacher solution)."""


# Provided class. Do NOT modify it.
class Vehicle:
    """Represents a basic vehicle."""

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display_info(self):
        """Return a one-line description of the vehicle.

        Returns:
            str: The vehicle's name and maximum speed.
        """
        return f"Vehicle: {self.name}, Max speed: {self.max_speed}"


class Racer(Vehicle):
    """Represents a racer whose top speed is capped by the vehicle's maximum."""

    def __init__(self, name, max_speed, top_speed):
        """Initialize a racer.

        Args:
            name (str): The vehicle's name.
            max_speed (int): The vehicle's maximum speed.
            top_speed (int): The racer's proposed top speed.
        """
        super().__init__(name, max_speed)
        if top_speed <= self.max_speed:
            self._top_speed = top_speed
        else:
            print("The top speed cannot exceed the maximum speed")
            self._top_speed = self.max_speed

    def get_top_speed(self):
        """Return the protected top speed.

        Returns:
            int: The racer's top speed.
        """
        return self._top_speed


if __name__ == "__main__":
    vehicle = Vehicle("Sedan", 180)
    print(vehicle.display_info())

    racer = Racer("Bolt", 200, 190)
    print(racer.display_info())
    print(racer.get_top_speed())

    bad_racer = Racer("Dash", 150, 170)
    print(bad_racer.get_top_speed())

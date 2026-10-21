"""Race Car -- Family 055, Assessment 05 (starter).

The Vehicle class is provided and complete. Complete the Racer class.
"""


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


class Racer():                                 # TODO 1: make Racer inherit from Vehicle
    """Represents a racer whose top speed is capped by the vehicle's maximum."""

    def __init__(self, name, max_speed, top_speed):
        """Initialize a racer.

        Args:
            name (str): The vehicle's name.
            max_speed (int): The vehicle's maximum speed.
            top_speed (int): The racer's proposed top speed.
        """

        # TODO 2: Call super().__init__(name, max_speed).
        # TODO 3: Validate the top speed against the parent's maximum speed.
        #         If top_speed <= self.max_speed, store it in the PROTECTED
        #         attribute _top_speed; otherwise print
        #         "The top speed cannot exceed the maximum speed" and fall back
        #         to self.max_speed.

        return

    def get_top_speed(self):
        """Return the protected top speed.

        Returns:
            int: The racer's top speed.
        """

        # TODO 4: Return the protected _top_speed.

        return 0

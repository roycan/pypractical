"""Vehicle Hierarchy -- Family 05, Assessment 02 (starter).

The Vehicle class is provided and complete. Complete the Motorcycle class.
"""


# Provided class. Do NOT modify it.
class Vehicle:
    """Represents a basic vehicle."""

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_brand(self):
        """Return the vehicle's brand."""
        return self.brand

    def get_year(self):
        """Return the vehicle's year."""
        return self.year


class Motorcycle(Vehicle):
    """Represents a vehicle with a specific engine type."""

    def __init__(self, brand, year, engine_type):
        """Initialize a motorcycle.

        Args:
            brand (str): The motorcycle's brand.
            year (int): The motorcycle's year.
            engine_type (str): The motorcycle's engine type.
        """

        # TODO: Write your solution here.

        return

    def get_engine_type(self):
        """Return the motorcycle's engine type.

        Returns:
            str: The motorcycle's engine type.
        """

        # TODO: Write your solution here.

        return ""

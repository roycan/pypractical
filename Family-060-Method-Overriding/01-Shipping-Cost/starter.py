"""Shipping Cost -- Family 06, Assessment 01 (starter).

The Parcel class is provided and complete. Complete the ExpressParcel class.
"""


# Provided class. Do NOT modify it.
class Parcel:
    """Represents a standard parcel."""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_name(self):
        """Return the parcel's name."""
        return self.name

    def get_weight(self):
        """Return the parcel's weight."""
        return self.weight

    def shipping(self):
        """Return the shipping cost (5 per unit of weight)."""
        return self.weight * 5


class ExpressParcel(Parcel):
    """Represents an express parcel shipped at a higher rate."""

    def __init__(self, name, weight):
        """Initialize an express parcel.

        Args:
            name (str): The parcel's name.
            weight (int): The parcel's weight.
        """

        # TODO: Write your solution here.

        return

    def shipping(self):
        """Return the express shipping cost (10 per unit of weight).

        Returns:
            int: The express shipping cost.
        """

        # TODO: Write your solution here.

        return 0

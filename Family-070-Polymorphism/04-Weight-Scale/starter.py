"""Weight Scale -- Family 07, Assessment 04 (starter).

The Light and Heavy classes are provided and complete. Complete the Scale class.
"""


# Provided class. Do NOT modify it.
class Light:
    """A light load that weighs count * 1."""

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def weight(self):
        """Return the weight of this load (count * 1)."""
        return self.count * 1


# Provided class. Do NOT modify it.
class Heavy:
    """A heavy load that weighs count * 5."""

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def weight(self):
        """Return the weight of this load (count * 5)."""
        return self.count * 5


class Scale:
    """A scale that collects loads and reports their weights."""

    def __init__(self):
        """Initialize an empty scale.

        The scale starts with no loads.
        """

        # TODO: Write your solution here.

        return

    def add(self, load):
        """Add a load to the scale.

        Args:
            load: A load that has a weight() method.
        """

        # TODO: Write your solution here.

        return

    def weights(self):
        """Return the weight of each load on the scale.

        Returns:
            list: The weight of each load.
        """

        # TODO: Write your solution here.

        return []

    def total_weight(self):
        """Return the total weight of all loads on the scale.

        Returns:
            int: The total weight of all loads.
        """

        # TODO: Write your solution here.

        return 0

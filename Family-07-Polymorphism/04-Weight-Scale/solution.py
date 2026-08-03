"""Weight Scale -- Family 07, Assessment 04 (teacher solution)."""


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
        self.loads = []

    def add(self, load):
        """Add a load to the scale.

        Args:
            load: A load that has a weight() method.
        """
        self.loads.append(load)

    def weights(self):
        """Return the weight of each load on the scale.

        Returns:
            list: The weight of each load.
        """
        result = []
        for load in self.loads:
            result.append(load.weight())
        return result

    def total_weight(self):
        """Return the total weight of all loads on the scale.

        Returns:
            int: The total weight of all loads.
        """
        result = 0
        for load in self.loads:
            result = result + load.weight()
        return result


if __name__ == "__main__":
    scale = Scale()
    scale.add(Light("A", 4))
    scale.add(Heavy("B", 4))
    print(scale.weights())
    print(scale.total_weight())

"""Land Area -- Family 08, Assessment 02 (teacher solution)."""


# Provided class. Do NOT modify it.
class Plot:
    """An abstract plot. Subclasses must implement area()."""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Return the plot's name."""
        return self.name

    def area(self):
        """Return the area of the plot.

        Every kind of plot computes area differently, so the base Plot
        does not implement this method. Subclasses must provide their own.
        """
        raise NotImplementedError("Subclasses must implement area().")


class Rectangular(Plot):
    """A rectangular plot. Its area is length * width."""

    def __init__(self, name, length, width):
        """Initialize a rectangular plot with a name, length, and width."""
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        """Return the area of this plot (length * width)."""
        return self.length * self.width


class Triangular(Plot):
    """A triangular plot. Its area is base * height // 2."""

    def __init__(self, name, base, height):
        """Initialize a triangular plot with a name, base, and height."""
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        """Return the area of this plot (base * height // 2)."""
        return self.base * self.height // 2


if __name__ == "__main__":
    rectangular = Rectangular("P1", 4, 5)
    print(rectangular.get_name())
    print(rectangular.area())

    triangular = Triangular("P2", 6, 4)
    print(triangular.get_name())
    print(triangular.area())

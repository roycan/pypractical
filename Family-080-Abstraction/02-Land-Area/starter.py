"""Land Area -- Family 08, Assessment 02 (starter).

The Plot class is provided and complete. Complete the Rectangular and Triangular
classes.
"""


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

        # TODO: Write your solution here.

        return

    def area(self):
        """Return the area of this plot (length * width)."""

        # TODO: Write your solution here.

        return 0


class Triangular(Plot):
    """A triangular plot. Its area is base * height // 2."""

    def __init__(self, name, base, height):
        """Initialize a triangular plot with a name, base, and height."""

        # TODO: Write your solution here.

        return

    def area(self):
        """Return the area of this plot (base * height // 2)."""

        # TODO: Write your solution here.

        return 0

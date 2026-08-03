"""Shapes -- Family 08, Assessment 01 (starter).

The Shape class is provided and complete. Complete the Rectangle and Triangle
classes.
"""


# Provided class. Do NOT modify it.
class Shape:
    """An abstract shape. Subclasses must implement area()."""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Return the shape's name."""
        return self.name

    def area(self):
        """Return the area of the shape.

        Every kind of shape computes area differently, so the base Shape
        does not implement this method. Subclasses must provide their own.
        """
        raise NotImplementedError("Subclasses must implement area().")


class Rectangle(Shape):
    """A rectangle shape. Its area is width * height."""

    def __init__(self, name, width, height):
        """Initialize a rectangle with a name, width, and height."""

        # TODO: Write your solution here.

        return

    def area(self):
        """Return the area of this rectangle (width * height)."""

        # TODO: Write your solution here.

        return 0


class Triangle(Shape):
    """A triangle shape. Its area is base * height // 2."""

    def __init__(self, name, base, height):
        """Initialize a triangle with a name, base, and height."""

        # TODO: Write your solution here.

        return

    def area(self):
        """Return the area of this triangle (base * height // 2)."""

        # TODO: Write your solution here.

        return 0

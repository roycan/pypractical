"""Screen Grid -- Family 08, Assessment 04 (starter).

The Screen class is provided and complete. Complete the Standard and Compact
classes.
"""


# Provided class. Do NOT modify it.
class Screen:
    """An abstract screen. Subclasses must implement pixels()."""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Return the screen's name."""
        return self.name

    def pixels(self):
        """Return the number of pixels on the screen.

        A standard and a compact screen compute pixels differently, so the
        base Screen does not implement this method. Subclasses must provide
        their own.
        """
        raise NotImplementedError("Subclasses must implement pixels().")


class Standard(Screen):
    """A standard screen. Its pixels are rows * cols."""

    def __init__(self, name, rows, cols):
        """Initialize a standard screen with a name, rows, and cols."""

        # TODO: Write your solution here.

        return

    def pixels(self):
        """Return the pixels of this screen (rows * cols)."""

        # TODO: Write your solution here.

        return 0


class Compact(Screen):
    """A compact screen. Its pixels are rows * cols // 2."""

    def __init__(self, name, rows, cols):
        """Initialize a compact screen with a name, rows, and cols."""

        # TODO: Write your solution here.

        return

    def pixels(self):
        """Return the pixels of this screen (rows * cols // 2)."""

        # TODO: Write your solution here.

        return 0

"""Fabric Order -- Family 08, Assessment 03 (starter).

The Cloth class is provided and complete. Complete the FullRoll and HalfRoll
classes.
"""


# Provided class. Do NOT modify it.
class Cloth:
    """An abstract cloth order. Subclasses must implement units()."""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Return the cloth order's name."""
        return self.name

    def units(self):
        """Return the number of units in the cloth order.

        A full roll and a half roll compute units differently, so the base
        Cloth does not implement this method. Subclasses must provide their
        own.
        """
        raise NotImplementedError("Subclasses must implement units().")


class FullRoll(Cloth):
    """A full roll of cloth. Its units are length * width."""

    def __init__(self, name, length, width):
        """Initialize a full roll with a name, length, and width."""

        # TODO: Write your solution here.

        return

    def units(self):
        """Return the units of this roll (length * width)."""

        # TODO: Write your solution here.

        return 0


class HalfRoll(Cloth):
    """A half roll of cloth. Its units are length * width // 2."""

    def __init__(self, name, length, width):
        """Initialize a half roll with a name, length, and width."""

        # TODO: Write your solution here.

        return

    def units(self):
        """Return the units of this roll (length * width // 2)."""

        # TODO: Write your solution here.

        return 0

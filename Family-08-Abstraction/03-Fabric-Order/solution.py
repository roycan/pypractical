"""Fabric Order -- Family 08, Assessment 03 (teacher solution)."""


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
        super().__init__(name)
        self.length = length
        self.width = width

    def units(self):
        """Return the units of this roll (length * width)."""
        return self.length * self.width


class HalfRoll(Cloth):
    """A half roll of cloth. Its units are length * width // 2."""

    def __init__(self, name, length, width):
        """Initialize a half roll with a name, length, and width."""
        super().__init__(name)
        self.length = length
        self.width = width

    def units(self):
        """Return the units of this roll (length * width // 2)."""
        return self.length * self.width // 2


if __name__ == "__main__":
    full = FullRoll("C1", 4, 5)
    print(full.get_name())
    print(full.units())

    half = HalfRoll("C2", 6, 4)
    print(half.get_name())
    print(half.units())

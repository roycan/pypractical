"""Fuel Tank -- Family 04, Assessment 02 (teacher solution)."""


class FuelTank:
    """Represents one fuel tank with protected litres."""

    def __init__(self, name, starting_litres):
        """Initialize a fuel tank.

        Args:
            name (str): The tank's name.
            starting_litres (int): The starting litres (non-negative).
        """
        self.name = name
        self._litres = starting_litres

    def get_litres(self):
        """Return the protected litres.

        Returns:
            int: The current litres.
        """
        return self._litres

    def add_fuel(self, litres):
        """Add a valid amount of litres.

        Args:
            litres (int): The litres to add.
        """
        if litres > 0:
            self._litres = self._litres + litres
        return

    def draw_fuel(self, litres):
        """Remove a valid amount of litres.

        Args:
            litres (int): The litres to draw.
        """
        if litres > 0 and litres <= self._litres:
            self._litres = self._litres - litres
        return


if __name__ == "__main__":
    tank = FuelTank("Tank A", 1000)
    print(tank.name)
    print(tank.get_litres())
    tank.add_fuel(500)
    print(tank.get_litres())
    tank.draw_fuel(300)
    print(tank.get_litres())

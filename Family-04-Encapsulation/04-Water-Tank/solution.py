"""Water Tank -- Family 04, Assessment 04 (teacher solution)."""


class WaterTank:
    """Represents one water tank with protected litres."""

    def __init__(self, name, starting_litres):
        """Initialize a water tank.

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

    def fill(self, litres):
        """Add a valid amount of litres.

        Args:
            litres (int): The litres to add.
        """
        if litres > 0:
            self._litres = self._litres + litres
        return

    def drain(self, litres):
        """Remove a valid amount of litres.

        Args:
            litres (int): The litres to drain.
        """
        if litres > 0 and litres <= self._litres:
            self._litres = self._litres - litres
        return


if __name__ == "__main__":
    tank = WaterTank("Reservoir A", 1000)
    print(tank.name)
    print(tank.get_litres())
    tank.fill(500)
    print(tank.get_litres())
    tank.drain(300)
    print(tank.get_litres())

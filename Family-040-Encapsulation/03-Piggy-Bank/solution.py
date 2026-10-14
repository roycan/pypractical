"""Piggy Bank -- Family 04, Assessment 03 (teacher solution)."""


class PiggyBank:
    """Represents one piggy bank with protected coins."""

    def __init__(self, owner, starting_coins):
        """Initialize a piggy bank.

        Args:
            owner (str): The owner's name.
            starting_coins (int): The starting coins (non-negative).
        """
        self.owner = owner
        self._coins = starting_coins

    def get_coins(self):
        """Return the protected coins.

        Returns:
            int: The current coins.
        """
        return self._coins

    def add_coins(self, coins):
        """Add a valid amount of coins.

        Args:
            coins (int): The coins to add.
        """
        if coins > 0:
            self._coins = self._coins + coins
        return

    def take_coins(self, coins):
        """Remove a valid amount of coins.

        Args:
            coins (int): The coins to take.
        """
        if coins > 0 and coins <= self._coins:
            self._coins = self._coins - coins
        return


if __name__ == "__main__":
    bank = PiggyBank("Ada", 1000)
    print(bank.owner)
    print(bank.get_coins())
    bank.add_coins(500)
    print(bank.get_coins())
    bank.take_coins(300)
    print(bank.get_coins())

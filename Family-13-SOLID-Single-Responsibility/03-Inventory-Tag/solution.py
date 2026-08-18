"""Inventory Tag -- Family 11, Assessment 03 (teacher solution)."""


class Stock:
    """Stores quantities and computes the count and total."""

    def __init__(self):
        """Initialize a stock with an empty list of quantities."""
        self.quantities = []

    def add_quantity(self, quantity):
        """Record one quantity.

        Args:
            quantity (int): The quantity to add.
        """
        self.quantities.append(quantity)

    def count(self):
        """Return the number of recorded quantities.

        Returns:
            int: The number of quantities stored.
        """
        return len(self.quantities)

    def total(self):
        """Return the sum of all recorded quantities.

        Returns:
            int: The total of all quantities.
        """
        total = 0
        for quantity in self.quantities:
            total = total + quantity
        return total


class Tag:
    """Formats a readable summary string from a Stock."""

    def summary(self, stock):
        """Build a summary string from the given stock.

        Args:
            stock (Stock): The stock to summarize.

        Returns:
            str: A summary of the stock's count and total.
        """
        return "Items: " + str(stock.count()) + ", Units: " + str(stock.total())


if __name__ == "__main__":
    stock = Stock()
    stock.add_quantity(100)
    stock.add_quantity(200)
    print(stock.count())
    print(stock.total())

    tag = Tag()
    print(tag.summary(stock))

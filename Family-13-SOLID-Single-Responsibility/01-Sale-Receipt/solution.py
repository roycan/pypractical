"""Sale Receipt -- Family 11, Assessment 01 (teacher solution)."""


class Sale:
    """Stores sale amounts and computes the count and total."""

    def __init__(self):
        """Initialize a sale with an empty list of amounts."""
        self.amounts = []

    def add_amount(self, amount):
        """Record one sale amount.

        Args:
            amount (int): The sale amount to add.
        """
        self.amounts.append(amount)

    def count(self):
        """Return the number of recorded amounts.

        Returns:
            int: The number of amounts stored.
        """
        return len(self.amounts)

    def total(self):
        """Return the sum of all recorded amounts.

        Returns:
            int: The total of all amounts.
        """
        total = 0
        for amount in self.amounts:
            total = total + amount
        return total


class Receipt:
    """Formats a readable summary string from a Sale."""

    def summary(self, sale):
        """Build a summary string from the given sale.

        Args:
            sale (Sale): The sale to summarize.

        Returns:
            str: A summary of the sale's count and total.
        """
        return "Items: " + str(sale.count()) + ", Total: " + str(sale.total())


if __name__ == "__main__":
    sale = Sale()
    sale.add_amount(100)
    sale.add_amount(200)
    print(sale.count())
    print(sale.total())

    receipt = Receipt()
    print(receipt.summary(sale))

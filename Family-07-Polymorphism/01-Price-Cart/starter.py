"""Price Cart -- Family 07, Assessment 01 (starter).

The FullPrice and HalfPrice classes are provided and complete. Complete the
Cart class.
"""


# Provided class. Do NOT modify it.
class FullPrice:
    """An item paid at full price."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def amount(self):
        """Return the amount to pay (full price)."""
        return self.price


# Provided class. Do NOT modify it.
class HalfPrice:
    """An item paid at half price."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def amount(self):
        """Return the amount to pay (half price)."""
        return self.price // 2


class Cart:
    """A shopping cart that collects items and reports their amounts."""

    def __init__(self):
        """Initialize an empty cart.

        The cart starts with no items.
        """

        # TODO: Write your solution here.

        return

    def add(self, item):
        """Add an item to the cart.

        Args:
            item: An item that has an amount() method.
        """

        # TODO: Write your solution here.

        return

    def amounts(self):
        """Return the amount of each item in the cart.

        Returns:
            list: The amount of each item.
        """

        # TODO: Write your solution here.

        return []

    def total(self):
        """Return the total amount of all items in the cart.

        Returns:
            int: The total amount of all items.
        """

        # TODO: Write your solution here.

        return 0

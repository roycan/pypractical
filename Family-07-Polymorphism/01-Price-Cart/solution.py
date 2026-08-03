"""Price Cart -- Family 07, Assessment 01 (teacher solution)."""


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
        self.items = []

    def add(self, item):
        """Add an item to the cart.

        Args:
            item: An item that has an amount() method.
        """
        self.items.append(item)

    def amounts(self):
        """Return the amount of each item in the cart.

        Returns:
            list: The amount of each item.
        """
        result = []
        for item in self.items:
            result.append(item.amount())
        return result

    def total(self):
        """Return the total amount of all items in the cart.

        Returns:
            int: The total amount of all items.
        """
        result = 0
        for item in self.items:
            result = result + item.amount()
        return result


if __name__ == "__main__":
    cart = Cart()
    cart.add(FullPrice("Book", 100))
    cart.add(HalfPrice("Magazine", 100))
    print(cart.amounts())
    print(cart.total())

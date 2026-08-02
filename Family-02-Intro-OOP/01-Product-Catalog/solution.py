"""Product Catalog -- Family 02, Assessment 01 (teacher solution)."""


class Product:
    """Represents one product in the shop catalog."""

    def __init__(self, name, price, quantity):
        """Initialize a product.

        Args:
            name (str): Product name.
            price (int): Price for one unit.
            quantity (int): Number of units in stock.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        """Return the total value of this product's stock.

        Returns:
            int: price multiplied by quantity.
        """
        return self.price * self.quantity


if __name__ == "__main__":
    product = Product("Notebook", 50, 3)
    print(product.name)
    print(product.price)
    print(product.quantity)
    print(product.total_value())

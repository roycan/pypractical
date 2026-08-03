"""Unit tests for Product Catalog -- Family 02, Assessment 01."""

import unittest

from solution import Product


class TestProductCatalog(unittest.TestCase):

    # --- Product attributes ---

    def test_name_stored(self):
        product = Product("Notebook", 50, 3)
        self.assertEqual(product.name, "Notebook")

    def test_price_stored(self):
        product = Product("Notebook", 50, 3)
        self.assertEqual(product.price, 50)

    def test_quantity_stored(self):
        product = Product("Notebook", 50, 3)
        self.assertEqual(product.quantity, 3)

    # --- total_value (basic) ---

    def test_total_value_basic(self):
        product = Product("Notebook", 50, 3)
        self.assertEqual(product.total_value(), 150)

    def test_total_value_single_unit(self):
        product = Product("Pen", 25, 1)
        self.assertEqual(product.total_value(), 25)

    # --- Boundary ---

    def test_total_value_zero_quantity(self):
        product = Product("Bag", 200, 0)
        self.assertEqual(product.total_value(), 0)

    # --- Typical ---

    def test_total_value_typical(self):
        product = Product("Pencil", 10, 12)
        self.assertEqual(product.total_value(), 120)

    # --- Objects are independent ---

    def test_two_products_independent(self):
        first = Product("Notebook", 50, 3)
        second = Product("Pen", 25, 4)
        self.assertEqual(first.total_value(), 150)
        self.assertEqual(second.total_value(), 100)

    def test_changing_one_does_not_affect_other(self):
        first = Product("Notebook", 50, 3)
        second = Product("Pen", 25, 4)
        first.quantity = 10
        self.assertEqual(first.total_value(), 500)
        self.assertEqual(second.total_value(), 100)

    # --- Hidden ---

    def test_hidden_large_values(self):
        product = Product("Tablet", 8000, 15)
        self.assertEqual(product.total_value(), 120000)

    def test_hidden_small_values(self):
        product = Product("Eraser", 5, 7)
        self.assertEqual(product.total_value(), 35)

    def test_hidden_mixed(self):
        product = Product("Marker", 35, 9)
        self.assertEqual(product.total_value(), 315)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

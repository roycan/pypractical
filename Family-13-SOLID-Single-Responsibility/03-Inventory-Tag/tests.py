"""Unit tests for Inventory Tag -- Family 13, Assessment 03."""

import unittest

try:
    from solution import Stock, Tag
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestInventoryTag(unittest.TestCase):

    # --- Stock (data) ---

    def test_stock_count(self):
        stock = Stock()
        stock.add_quantity(100)
        stock.add_quantity(200)
        self.assertEqual(stock.count(), 2)

    def test_stock_total(self):
        stock = Stock()
        stock.add_quantity(100)
        stock.add_quantity(200)
        self.assertEqual(stock.total(), 300)

    def test_stock_empty(self):
        stock = Stock()
        self.assertEqual(stock.count(), 0)
        self.assertEqual(stock.total(), 0)

    def test_stock_single(self):
        stock = Stock()
        stock.add_quantity(100)
        self.assertEqual(stock.count(), 1)
        self.assertEqual(stock.total(), 100)

    # --- Tag (presentation) ---

    def test_tag_summary(self):
        stock = Stock()
        stock.add_quantity(100)
        stock.add_quantity(200)
        tag = Tag()
        self.assertEqual(tag.summary(stock), "Items: 2, Units: 300")

    def test_tag_summary_empty(self):
        tag = Tag()
        self.assertEqual(tag.summary(Stock()), "Items: 0, Units: 0")

    def test_tag_summary_single(self):
        stock = Stock()
        stock.add_quantity(50)
        tag = Tag()
        self.assertEqual(tag.summary(stock), "Items: 1, Units: 50")

    def test_tag_does_not_store_data(self):
        tag1 = Tag()
        stock_a = Stock()
        stock_a.add_quantity(100)
        tag2 = Tag()
        stock_b = Stock()
        stock_b.add_quantity(999)
        self.assertEqual(tag1.summary(stock_a), "Items: 1, Units: 100")
        self.assertEqual(tag2.summary(stock_b), "Items: 1, Units: 999")

    # --- Hidden ---

    def test_hidden_summary_three(self):
        stock = Stock()
        stock.add_quantity(10)
        stock.add_quantity(20)
        stock.add_quantity(30)
        tag = Tag()
        self.assertEqual(tag.summary(stock), "Items: 3, Units: 60")

    def test_hidden_two_stocks_independent(self):
        stock1 = Stock()
        stock1.add_quantity(100)
        stock1.add_quantity(200)
        stock2 = Stock()
        stock2.add_quantity(5)
        self.assertEqual(Tag().summary(stock1), "Items: 2, Units: 300")
        self.assertEqual(Tag().summary(stock2), "Items: 1, Units: 5")

    def test_hidden_large(self):
        stock = Stock()
        stock.add_quantity(1000)
        stock.add_quantity(2000)
        tag = Tag()
        self.assertEqual(tag.summary(stock), "Items: 2, Units: 3000")

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

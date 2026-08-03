"""Unit tests for Book Inventory -- Family 02, Assessment 02."""

import unittest

from solution import Book


class TestBookInventory(unittest.TestCase):

    # --- Book attributes ---

    def test_title_stored(self):
        book = Book("Python Basics", 300, 4)
        self.assertEqual(book.title, "Python Basics")

    def test_price_stored(self):
        book = Book("Python Basics", 300, 4)
        self.assertEqual(book.price, 300)

    def test_copies_stored(self):
        book = Book("Python Basics", 300, 4)
        self.assertEqual(book.copies, 4)

    # --- stock_value (basic) ---

    def test_stock_value_basic(self):
        book = Book("Python Basics", 300, 4)
        self.assertEqual(book.stock_value(), 1200)

    def test_stock_value_single_copy(self):
        book = Book("Pamphlet", 300, 1)
        self.assertEqual(book.stock_value(), 300)

    # --- Boundary ---

    def test_stock_value_zero_copies(self):
        book = Book("Catalog", 200, 0)
        self.assertEqual(book.stock_value(), 0)

    # --- Typical ---

    def test_stock_value_typical(self):
        book = Book("Novel", 250, 6)
        self.assertEqual(book.stock_value(), 1500)

    # --- Objects are independent ---

    def test_two_books_independent(self):
        first = Book("Python Basics", 300, 4)
        second = Book("Comic", 120, 5)
        self.assertEqual(first.stock_value(), 1200)
        self.assertEqual(second.stock_value(), 600)

    def test_changing_one_does_not_affect_other(self):
        first = Book("Python Basics", 300, 4)
        second = Book("Comic", 120, 5)
        first.copies = 10
        self.assertEqual(first.stock_value(), 3000)
        self.assertEqual(second.stock_value(), 600)

    # --- Hidden ---

    def test_hidden_large_values(self):
        book = Book("Atlas", 1500, 20)
        self.assertEqual(book.stock_value(), 30000)

    def test_hidden_small_values(self):
        book = Book("Leaflet", 8, 3)
        self.assertEqual(book.stock_value(), 24)

    def test_hidden_mixed(self):
        book = Book("Cookbook", 450, 7)
        self.assertEqual(book.stock_value(), 3150)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

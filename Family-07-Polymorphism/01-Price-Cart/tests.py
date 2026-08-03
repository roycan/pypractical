"""Unit tests for Price Cart -- Family 07, Assessment 01."""

import unittest

try:
    from solution import Cart, FullPrice, HalfPrice
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestPriceCart(unittest.TestCase):

    # --- Empty cart ---

    def test_cart_starts_empty(self):
        cart = Cart()
        self.assertEqual(cart.amounts(), [])

    # --- amounts() ---

    def test_amounts_one_full(self):
        cart = Cart()
        cart.add(FullPrice("A", 100))
        self.assertEqual(cart.amounts(), [100])

    def test_amounts_one_half(self):
        cart = Cart()
        cart.add(HalfPrice("B", 100))
        self.assertEqual(cart.amounts(), [50])

    def test_amounts_mixed(self):
        cart = Cart()
        cart.add(FullPrice("A", 100))
        cart.add(HalfPrice("B", 100))
        self.assertEqual(cart.amounts(), [100, 50])

    def test_amounts_order(self):
        cart = Cart()
        cart.add(HalfPrice("B", 100))
        cart.add(FullPrice("A", 100))
        self.assertEqual(cart.amounts(), [50, 100])

    # --- total() ---

    def test_total_mixed(self):
        cart = Cart()
        cart.add(FullPrice("A", 100))
        cart.add(HalfPrice("B", 100))
        self.assertEqual(cart.total(), 150)

    def test_total_single_full(self):
        cart = Cart()
        cart.add(FullPrice("A", 100))
        self.assertEqual(cart.total(), 100)

    def test_total_all_full(self):
        cart = Cart()
        cart.add(FullPrice("A", 10))
        cart.add(FullPrice("B", 20))
        self.assertEqual(cart.amounts(), [10, 20])
        self.assertEqual(cart.total(), 30)

    def test_total_all_half(self):
        cart = Cart()
        cart.add(HalfPrice("A", 10))
        cart.add(HalfPrice("B", 20))
        self.assertEqual(cart.amounts(), [5, 10])
        self.assertEqual(cart.total(), 15)

    # --- Hidden ---

    def test_hidden_three_mixed(self):
        cart = Cart()
        cart.add(FullPrice("A", 200))
        cart.add(HalfPrice("B", 200))
        cart.add(FullPrice("C", 50))
        self.assertEqual(cart.amounts(), [200, 100, 50])
        self.assertEqual(cart.total(), 350)

    def test_hidden_half_odd_price(self):
        cart = Cart()
        cart.add(HalfPrice("C", 101))
        self.assertEqual(cart.amounts(), [50])

    def test_hidden_large_mixed(self):
        cart = Cart()
        cart.add(FullPrice("A", 1000))
        cart.add(HalfPrice("B", 1000))
        self.assertEqual(cart.amounts(), [1000, 500])
        self.assertEqual(cart.total(), 1500)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

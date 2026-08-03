"""Unit tests for Piggy Bank -- Family 04, Assessment 03."""

import unittest

from solution import PiggyBank


class TestPiggyBank(unittest.TestCase):

    # --- Basic ---

    def test_owner_stored(self):
        bank = PiggyBank("Ada", 1000)
        self.assertEqual(bank.owner, "Ada")

    def test_initial_coins(self):
        bank = PiggyBank("Ada", 1000)
        self.assertEqual(bank.get_coins(), 1000)

    def test_add_coins_increases(self):
        bank = PiggyBank("Ada", 1000)
        bank.add_coins(500)
        self.assertEqual(bank.get_coins(), 1500)

    def test_take_coins_decreases(self):
        bank = PiggyBank("Ada", 1000)
        bank.take_coins(300)
        self.assertEqual(bank.get_coins(), 700)

    # --- Validation ---

    def test_add_coins_zero_ignored(self):
        bank = PiggyBank("Ada", 1000)
        bank.add_coins(0)
        self.assertEqual(bank.get_coins(), 1000)

    def test_add_coins_negative_ignored(self):
        bank = PiggyBank("Ada", 1000)
        bank.add_coins(-200)
        self.assertEqual(bank.get_coins(), 1000)

    def test_take_coins_more_than_coins_ignored(self):
        bank = PiggyBank("Ada", 1000)
        bank.take_coins(2000)
        self.assertEqual(bank.get_coins(), 1000)

    def test_take_coins_negative_ignored(self):
        bank = PiggyBank("Ada", 1000)
        bank.take_coins(-50)
        self.assertEqual(bank.get_coins(), 1000)

    def test_take_coins_exact_coins_to_zero(self):
        bank = PiggyBank("Bob", 500)
        bank.take_coins(500)
        self.assertEqual(bank.get_coins(), 0)

    # --- Typical ---

    def test_multiple_operations(self):
        bank = PiggyBank("Ada", 1000)
        bank.add_coins(500)
        bank.take_coins(200)
        bank.take_coins(300)
        self.assertEqual(bank.get_coins(), 1000)

    # --- Hidden ---

    def test_hidden_large_values(self):
        bank = PiggyBank("Cy", 10000)
        bank.add_coins(5000)
        bank.take_coins(15000)
        self.assertEqual(bank.get_coins(), 0)

    def test_hidden_cannot_overdraft_sequence(self):
        bank = PiggyBank("Dee", 200)
        bank.take_coins(150)
        bank.take_coins(100)
        self.assertEqual(bank.get_coins(), 50)

    def test_hidden_add_coins_then_take_coins_equal(self):
        bank = PiggyBank("Eve", 0)
        bank.add_coins(250)
        bank.take_coins(250)
        self.assertEqual(bank.get_coins(), 0)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

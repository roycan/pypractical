"""Unit tests for Fabric Order -- Family 08, Assessment 03."""

import unittest

from solution import Cloth, FullRoll, HalfRoll


class TestFabricOrder(unittest.TestCase):

    # --- FullRoll ---

    def test_full_roll_units(self):
        full = FullRoll("C1", 4, 5)
        self.assertEqual(full.units(), 20)

    def test_full_roll_stores_dimensions(self):
        full = FullRoll("C1", 4, 5)
        self.assertEqual(full.length, 4)
        self.assertEqual(full.width, 5)

    # --- HalfRoll ---

    def test_half_roll_units(self):
        half = HalfRoll("C2", 6, 4)
        self.assertEqual(half.units(), 12)

    # --- Inheritance ---

    def test_full_roll_inherits_get_name(self):
        full = FullRoll("C1", 4, 5)
        self.assertEqual(full.get_name(), "C1")

    def test_half_roll_inherits_get_name(self):
        half = HalfRoll("C2", 6, 4)
        self.assertEqual(half.get_name(), "C2")

    def test_full_roll_is_a_cloth(self):
        full = FullRoll("C1", 4, 5)
        self.assertIsInstance(full, Cloth)

    def test_half_roll_is_a_cloth(self):
        half = HalfRoll("C2", 6, 4)
        self.assertIsInstance(half, Cloth)

    # --- Hidden ---

    def test_different_full_roll(self):
        full = FullRoll("C3", 3, 7)
        self.assertEqual(full.units(), 21)

    def test_different_half_roll(self):
        half = HalfRoll("C4", 10, 5)
        self.assertEqual(half.units(), 25)

    def test_hidden_full_roll_large(self):
        full = FullRoll("C5", 20, 30)
        self.assertEqual(full.units(), 600)

    def test_hidden_half_roll_odd(self):
        half = HalfRoll("C6", 7, 3)
        self.assertEqual(half.units(), 10)

    def test_hidden_both(self):
        full = FullRoll("C7", 2, 9)
        half = HalfRoll("C8", 8, 5)
        self.assertEqual(full.units(), 18)
        self.assertEqual(half.units(), 20)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

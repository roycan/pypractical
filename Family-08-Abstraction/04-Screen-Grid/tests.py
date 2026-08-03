"""Unit tests for Screen Grid -- Family 08, Assessment 04."""

import unittest

try:
    from solution import Screen, Standard, Compact
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestScreenGrid(unittest.TestCase):

    # --- Standard ---

    def test_standard_pixels(self):
        standard = Standard("S1", 4, 5)
        self.assertEqual(standard.pixels(), 20)

    def test_standard_stores_dimensions(self):
        standard = Standard("S1", 4, 5)
        self.assertEqual(standard.rows, 4)
        self.assertEqual(standard.cols, 5)

    # --- Compact ---

    def test_compact_pixels(self):
        compact = Compact("S2", 6, 4)
        self.assertEqual(compact.pixels(), 12)

    # --- Inheritance ---

    def test_standard_inherits_get_name(self):
        standard = Standard("S1", 4, 5)
        self.assertEqual(standard.get_name(), "S1")

    def test_compact_inherits_get_name(self):
        compact = Compact("S2", 6, 4)
        self.assertEqual(compact.get_name(), "S2")

    def test_standard_is_a_screen(self):
        standard = Standard("S1", 4, 5)
        self.assertIsInstance(standard, Screen)

    def test_compact_is_a_screen(self):
        compact = Compact("S2", 6, 4)
        self.assertIsInstance(compact, Screen)

    # --- Hidden ---

    def test_different_standard(self):
        standard = Standard("S3", 3, 7)
        self.assertEqual(standard.pixels(), 21)

    def test_different_compact(self):
        compact = Compact("S4", 10, 5)
        self.assertEqual(compact.pixels(), 25)

    def test_hidden_standard_large(self):
        standard = Standard("S5", 20, 30)
        self.assertEqual(standard.pixels(), 600)

    def test_hidden_compact_odd(self):
        compact = Compact("S6", 7, 3)
        self.assertEqual(compact.pixels(), 10)

    def test_hidden_both(self):
        standard = Standard("S7", 2, 9)
        compact = Compact("S8", 8, 5)
        self.assertEqual(standard.pixels(), 18)
        self.assertEqual(compact.pixels(), 20)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

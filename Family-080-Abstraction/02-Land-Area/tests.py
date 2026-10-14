"""Unit tests for Land Area -- Family 08, Assessment 02."""

import unittest

try:
    from solution import Plot, Rectangular, Triangular
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestLandArea(unittest.TestCase):

    # --- Rectangular ---

    def test_rectangular_area(self):
        rectangular = Rectangular("P1", 4, 5)
        self.assertEqual(rectangular.area(), 20)

    def test_rectangular_stores_dimensions(self):
        rectangular = Rectangular("P1", 4, 5)
        self.assertEqual(rectangular.length, 4)
        self.assertEqual(rectangular.width, 5)

    # --- Triangular ---

    def test_triangular_area(self):
        triangular = Triangular("P2", 6, 4)
        self.assertEqual(triangular.area(), 12)

    # --- Inheritance ---

    def test_rectangular_inherits_get_name(self):
        rectangular = Rectangular("P1", 4, 5)
        self.assertEqual(rectangular.get_name(), "P1")

    def test_triangular_inherits_get_name(self):
        triangular = Triangular("P2", 6, 4)
        self.assertEqual(triangular.get_name(), "P2")

    def test_rectangular_is_a_plot(self):
        rectangular = Rectangular("P1", 4, 5)
        self.assertIsInstance(rectangular, Plot)

    def test_triangular_is_a_plot(self):
        triangular = Triangular("P2", 6, 4)
        self.assertIsInstance(triangular, Plot)

    # --- Hidden ---

    def test_different_rectangular(self):
        rectangular = Rectangular("P3", 3, 7)
        self.assertEqual(rectangular.area(), 21)

    def test_different_triangular(self):
        triangular = Triangular("P4", 10, 5)
        self.assertEqual(triangular.area(), 25)

    def test_hidden_rectangular_large(self):
        rectangular = Rectangular("P5", 20, 30)
        self.assertEqual(rectangular.area(), 600)

    def test_hidden_triangular_odd(self):
        triangular = Triangular("P6", 7, 3)
        self.assertEqual(triangular.area(), 10)

    def test_hidden_both(self):
        rectangular = Rectangular("P7", 2, 9)
        triangular = Triangular("P8", 8, 5)
        self.assertEqual(rectangular.area(), 18)
        self.assertEqual(triangular.area(), 20)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

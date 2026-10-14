"""Unit tests for Shapes -- Family 08, Assessment 01."""

import unittest

try:
    from solution import Shape, Rectangle, Triangle
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestShapes(unittest.TestCase):

    # --- Rectangle ---

    def test_rectangle_area(self):
        rectangle = Rectangle("R1", 4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_rectangle_stores_dimensions(self):
        rectangle = Rectangle("R1", 4, 5)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)

    # --- Triangle ---

    def test_triangle_area(self):
        triangle = Triangle("T1", 6, 4)
        self.assertEqual(triangle.area(), 12)

    # --- Inheritance ---

    def test_rectangle_inherits_get_name(self):
        rectangle = Rectangle("R1", 4, 5)
        self.assertEqual(rectangle.get_name(), "R1")

    def test_triangle_inherits_get_name(self):
        triangle = Triangle("T1", 6, 4)
        self.assertEqual(triangle.get_name(), "T1")

    def test_rectangle_is_a_shape(self):
        rectangle = Rectangle("R1", 4, 5)
        self.assertIsInstance(rectangle, Shape)

    def test_triangle_is_a_shape(self):
        triangle = Triangle("T1", 6, 4)
        self.assertIsInstance(triangle, Shape)

    # --- Hidden ---

    def test_different_rectangle(self):
        rectangle = Rectangle("R2", 3, 7)
        self.assertEqual(rectangle.area(), 21)

    def test_different_triangle(self):
        triangle = Triangle("T2", 10, 5)
        self.assertEqual(triangle.area(), 25)

    def test_hidden_rectangle_large(self):
        rectangle = Rectangle("R3", 20, 30)
        self.assertEqual(rectangle.area(), 600)

    def test_hidden_triangle_odd(self):
        triangle = Triangle("T3", 7, 3)
        self.assertEqual(triangle.area(), 10)

    def test_hidden_both(self):
        rectangle = Rectangle("R", 2, 9)
        triangle = Triangle("T", 8, 5)
        self.assertEqual(rectangle.area(), 18)
        self.assertEqual(triangle.area(), 20)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

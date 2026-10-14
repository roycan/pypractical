"""Unit tests for Flashlight -- Family 10, Assessment 01."""

import unittest

try:
    from solution import Battery, Flashlight
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestFlashlight(unittest.TestCase):

    # --- count ---

    def test_creates_correct_count(self):
        flashlight = Flashlight(3, 100)
        self.assertEqual(flashlight.count_batteries(), 3)

    def test_one_battery(self):
        flashlight = Flashlight(1, 100)
        self.assertEqual(flashlight.count_batteries(), 1)
        self.assertEqual(flashlight.total_capacity(), 100)

    def test_zero_batteries(self):
        flashlight = Flashlight(0, 100)
        self.assertEqual(flashlight.count_batteries(), 0)
        self.assertEqual(flashlight.total_capacity(), 0)

    # --- total_capacity ---

    def test_total_capacity(self):
        flashlight = Flashlight(3, 100)
        self.assertEqual(flashlight.total_capacity(), 300)

    def test_different_capacity(self):
        flashlight = Flashlight(3, 50)
        self.assertEqual(flashlight.total_capacity(), 150)

    def test_large(self):
        flashlight = Flashlight(5, 1000)
        self.assertEqual(flashlight.total_capacity(), 5000)

    # --- parts created ---

    def test_each_battery_has_capacity(self):
        flashlight = Flashlight(2, 50)
        self.assertEqual(flashlight.batteries[0].get_capacity(), 50)
        self.assertEqual(flashlight.batteries[1].get_capacity(), 50)

    # --- Hidden ---

    def test_hidden_count_and_total(self):
        flashlight = Flashlight(4, 25)
        self.assertEqual(flashlight.count_batteries(), 4)
        self.assertEqual(flashlight.total_capacity(), 100)

    def test_hidden_total_six(self):
        flashlight = Flashlight(6, 30)
        self.assertEqual(flashlight.total_capacity(), 180)

    def test_hidden_single(self):
        flashlight = Flashlight(1, 500)
        self.assertEqual(flashlight.total_capacity(), 500)

    def test_hidden_zero_total(self):
        flashlight = Flashlight(0, 999)
        self.assertEqual(flashlight.total_capacity(), 0)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

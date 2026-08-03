"""Unit tests for Fuel Tank -- Family 04, Assessment 02."""

import unittest

try:
    from solution import FuelTank
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestFuelTank(unittest.TestCase):

    # --- Basic ---

    def test_name_stored(self):
        tank = FuelTank("Tank A", 1000)
        self.assertEqual(tank.name, "Tank A")

    def test_initial_litres(self):
        tank = FuelTank("Tank A", 1000)
        self.assertEqual(tank.get_litres(), 1000)

    def test_add_fuel_increases(self):
        tank = FuelTank("Tank A", 1000)
        tank.add_fuel(500)
        self.assertEqual(tank.get_litres(), 1500)

    def test_draw_fuel_decreases(self):
        tank = FuelTank("Tank A", 1000)
        tank.draw_fuel(300)
        self.assertEqual(tank.get_litres(), 700)

    # --- Validation ---

    def test_add_fuel_zero_ignored(self):
        tank = FuelTank("Tank A", 1000)
        tank.add_fuel(0)
        self.assertEqual(tank.get_litres(), 1000)

    def test_add_fuel_negative_ignored(self):
        tank = FuelTank("Tank A", 1000)
        tank.add_fuel(-200)
        self.assertEqual(tank.get_litres(), 1000)

    def test_draw_fuel_more_than_litres_ignored(self):
        tank = FuelTank("Tank A", 1000)
        tank.draw_fuel(2000)
        self.assertEqual(tank.get_litres(), 1000)

    def test_draw_fuel_negative_ignored(self):
        tank = FuelTank("Tank A", 1000)
        tank.draw_fuel(-50)
        self.assertEqual(tank.get_litres(), 1000)

    def test_draw_fuel_exact_litres_to_zero(self):
        tank = FuelTank("Tank B", 500)
        tank.draw_fuel(500)
        self.assertEqual(tank.get_litres(), 0)

    # --- Typical ---

    def test_multiple_operations(self):
        tank = FuelTank("Tank A", 1000)
        tank.add_fuel(500)
        tank.draw_fuel(200)
        tank.draw_fuel(300)
        self.assertEqual(tank.get_litres(), 1000)

    # --- Hidden ---

    def test_hidden_large_values(self):
        tank = FuelTank("Tank C", 10000)
        tank.add_fuel(5000)
        tank.draw_fuel(15000)
        self.assertEqual(tank.get_litres(), 0)

    def test_hidden_cannot_overdraft_sequence(self):
        tank = FuelTank("Tank D", 200)
        tank.draw_fuel(150)
        tank.draw_fuel(100)
        self.assertEqual(tank.get_litres(), 50)

    def test_hidden_add_fuel_then_draw_fuel_equal(self):
        tank = FuelTank("Tank E", 0)
        tank.add_fuel(250)
        tank.draw_fuel(250)
        self.assertEqual(tank.get_litres(), 0)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

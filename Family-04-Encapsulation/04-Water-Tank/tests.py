"""Unit tests for Water Tank -- Family 04, Assessment 04."""

import unittest

from solution import WaterTank


class TestWaterTank(unittest.TestCase):

    # --- Basic ---

    def test_name_stored(self):
        tank = WaterTank("Reservoir A", 1000)
        self.assertEqual(tank.name, "Reservoir A")

    def test_initial_litres(self):
        tank = WaterTank("Reservoir A", 1000)
        self.assertEqual(tank.get_litres(), 1000)

    def test_fill_increases(self):
        tank = WaterTank("Reservoir A", 1000)
        tank.fill(500)
        self.assertEqual(tank.get_litres(), 1500)

    def test_drain_decreases(self):
        tank = WaterTank("Reservoir A", 1000)
        tank.drain(300)
        self.assertEqual(tank.get_litres(), 700)

    # --- Validation ---

    def test_fill_zero_ignored(self):
        tank = WaterTank("Reservoir A", 1000)
        tank.fill(0)
        self.assertEqual(tank.get_litres(), 1000)

    def test_fill_negative_ignored(self):
        tank = WaterTank("Reservoir A", 1000)
        tank.fill(-200)
        self.assertEqual(tank.get_litres(), 1000)

    def test_drain_more_than_litres_ignored(self):
        tank = WaterTank("Reservoir A", 1000)
        tank.drain(2000)
        self.assertEqual(tank.get_litres(), 1000)

    def test_drain_negative_ignored(self):
        tank = WaterTank("Reservoir A", 1000)
        tank.drain(-50)
        self.assertEqual(tank.get_litres(), 1000)

    def test_drain_exact_litres_to_zero(self):
        tank = WaterTank("Reservoir B", 500)
        tank.drain(500)
        self.assertEqual(tank.get_litres(), 0)

    # --- Typical ---

    def test_multiple_operations(self):
        tank = WaterTank("Reservoir A", 1000)
        tank.fill(500)
        tank.drain(200)
        tank.drain(300)
        self.assertEqual(tank.get_litres(), 1000)

    # --- Hidden ---

    def test_hidden_large_values(self):
        tank = WaterTank("Reservoir C", 10000)
        tank.fill(5000)
        tank.drain(15000)
        self.assertEqual(tank.get_litres(), 0)

    def test_hidden_cannot_overdraft_sequence(self):
        tank = WaterTank("Reservoir D", 200)
        tank.drain(150)
        tank.drain(100)
        self.assertEqual(tank.get_litres(), 50)

    def test_hidden_fill_then_drain_equal(self):
        tank = WaterTank("Reservoir E", 0)
        tank.fill(250)
        tank.drain(250)
        self.assertEqual(tank.get_litres(), 0)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

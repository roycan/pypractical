"""Unit tests for Parking Garage Daily Report -- Family 01, Assessment 01."""

import unittest

from solution import calculate_total_revenue


class TestParkingGarage(unittest.TestCase):

    # --- Basic ---

    def test_one_customer_hourly_cheaper(self):
        self.assertEqual(calculate_total_revenue([3], 100, 450), 300)

    def test_one_customer_fixed_cheaper(self):
        self.assertEqual(calculate_total_revenue([8], 100, 450), 450)

    def test_two_customers(self):
        self.assertEqual(calculate_total_revenue([2, 4], 100, 450), 600)

    # --- Boundary ---

    def test_equal_cost(self):
        self.assertEqual(calculate_total_revenue([5], 100, 500), 500)

    def test_single_minimum_values(self):
        self.assertEqual(calculate_total_revenue([1], 1, 100), 1)

    # --- Typical ---

    def test_all_hourly(self):
        self.assertEqual(calculate_total_revenue([1, 2, 3], 50, 500), 300)

    def test_all_fixed(self):
        self.assertEqual(calculate_total_revenue([10, 12, 15], 100, 450), 1350)

    def test_many_small_customers(self):
        self.assertEqual(calculate_total_revenue([1, 1, 1, 1, 1], 100, 500), 500)

    # --- Mixed ---

    def test_mixed_customers(self):
        self.assertEqual(
            calculate_total_revenue([5, 3, 8, 2, 10], 100, 450),
            1850,
        )

    def test_large_mix(self):
        self.assertEqual(
            calculate_total_revenue([1, 5, 10, 20, 3, 7], 80, 500),
            2220,
        )

    # --- Hidden ---

    def test_hidden_case_1(self):
        self.assertEqual(calculate_total_revenue([6, 6, 6], 70, 500), 1260)

    def test_hidden_case_2(self):
        self.assertEqual(calculate_total_revenue([20], 100, 1500), 1500)


if __name__ == "__main__":
    unittest.main()

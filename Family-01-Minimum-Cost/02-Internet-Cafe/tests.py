"""Unit tests for Internet Cafe Daily Report -- Family 01, Assessment 02."""

import unittest

from solution import calculate_daily_revenue


class TestInternetCafe(unittest.TestCase):

    # --- Basic ---

    def test_one_customer_hourly_cheaper(self):
        self.assertEqual(calculate_daily_revenue([2], 60, 300), 120)

    def test_one_customer_day_pass_cheaper(self):
        self.assertEqual(calculate_daily_revenue([8], 60, 300), 300)

    def test_two_customers(self):
        self.assertEqual(calculate_daily_revenue([2, 3], 60, 300), 300)

    # --- Boundary ---

    def test_equal_cost(self):
        self.assertEqual(calculate_daily_revenue([5], 60, 300), 300)

    def test_single_minimum_values(self):
        self.assertEqual(calculate_daily_revenue([1], 1, 100), 1)

    # --- Typical ---

    def test_all_hourly(self):
        self.assertEqual(calculate_daily_revenue([1, 2, 3], 50, 500), 300)

    def test_all_day_pass(self):
        self.assertEqual(calculate_daily_revenue([10, 12, 15], 70, 400), 1200)

    def test_many_small_customers(self):
        self.assertEqual(calculate_daily_revenue([1, 1, 1, 1, 1], 50, 500), 250)

    # --- Mixed ---

    def test_mixed_customers(self):
        self.assertEqual(
            calculate_daily_revenue([2, 6, 4, 8], 60, 300),
            960,
        )

    def test_large_mix(self):
        self.assertEqual(
            calculate_daily_revenue([1, 5, 10, 12, 3, 7], 70, 450),
            1980,
        )

    # --- Hidden ---

    def test_hidden_case_1(self):
        self.assertEqual(calculate_daily_revenue([6, 6, 6], 50, 250), 750)

    def test_hidden_case_2(self):
        self.assertEqual(calculate_daily_revenue([20], 100, 1500), 1500)


# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

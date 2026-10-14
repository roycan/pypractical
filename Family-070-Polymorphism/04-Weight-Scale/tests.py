"""Unit tests for Weight Scale -- Family 07, Assessment 04."""

import unittest

try:
    from solution import Scale, Light, Heavy
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestWeightScale(unittest.TestCase):

    # --- Empty scale ---

    def test_scale_starts_empty(self):
        scale = Scale()
        self.assertEqual(scale.weights(), [])

    # --- weights() ---

    def test_weights_one_light(self):
        scale = Scale()
        scale.add(Light("A", 4))
        self.assertEqual(scale.weights(), [4])

    def test_weights_one_heavy(self):
        scale = Scale()
        scale.add(Heavy("B", 4))
        self.assertEqual(scale.weights(), [20])

    def test_weights_mixed(self):
        scale = Scale()
        scale.add(Light("A", 4))
        scale.add(Heavy("B", 4))
        self.assertEqual(scale.weights(), [4, 20])

    def test_weights_order(self):
        scale = Scale()
        scale.add(Heavy("B", 4))
        scale.add(Light("A", 4))
        self.assertEqual(scale.weights(), [20, 4])

    # --- total_weight() ---

    def test_total_weight_mixed(self):
        scale = Scale()
        scale.add(Light("A", 4))
        scale.add(Heavy("B", 4))
        self.assertEqual(scale.total_weight(), 24)

    def test_total_weight_single_light(self):
        scale = Scale()
        scale.add(Light("A", 4))
        self.assertEqual(scale.total_weight(), 4)

    def test_total_weight_all_light(self):
        scale = Scale()
        scale.add(Light("A", 3))
        scale.add(Light("B", 6))
        self.assertEqual(scale.weights(), [3, 6])
        self.assertEqual(scale.total_weight(), 9)

    def test_total_weight_all_heavy(self):
        scale = Scale()
        scale.add(Heavy("A", 3))
        scale.add(Heavy("B", 6))
        self.assertEqual(scale.weights(), [15, 30])
        self.assertEqual(scale.total_weight(), 45)

    # --- Hidden ---

    def test_hidden_three_mixed(self):
        scale = Scale()
        scale.add(Light("A", 10))
        scale.add(Heavy("B", 10))
        scale.add(Light("C", 2))
        self.assertEqual(scale.weights(), [10, 50, 2])
        self.assertEqual(scale.total_weight(), 62)

    def test_hidden_heavy_odd_count(self):
        scale = Scale()
        scale.add(Heavy("C", 9))
        self.assertEqual(scale.weights(), [45])

    def test_hidden_large_mixed(self):
        scale = Scale()
        scale.add(Light("A", 100))
        scale.add(Heavy("B", 100))
        self.assertEqual(scale.weights(), [100, 500])
        self.assertEqual(scale.total_weight(), 600)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

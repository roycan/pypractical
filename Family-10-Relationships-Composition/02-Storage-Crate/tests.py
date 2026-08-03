"""Unit tests for Storage Crate -- Family 10, Assessment 02."""

import unittest

from solution import Box, Crate


class TestCrate(unittest.TestCase):

    # --- count ---

    def test_creates_correct_count(self):
        crate = Crate(3, 100)
        self.assertEqual(crate.count_boxes(), 3)

    def test_one_box(self):
        crate = Crate(1, 100)
        self.assertEqual(crate.count_boxes(), 1)
        self.assertEqual(crate.total_size(), 100)

    def test_zero_boxes(self):
        crate = Crate(0, 100)
        self.assertEqual(crate.count_boxes(), 0)
        self.assertEqual(crate.total_size(), 0)

    # --- total_size ---

    def test_total_size(self):
        crate = Crate(3, 100)
        self.assertEqual(crate.total_size(), 300)

    def test_different_size(self):
        crate = Crate(3, 50)
        self.assertEqual(crate.total_size(), 150)

    def test_large(self):
        crate = Crate(5, 1000)
        self.assertEqual(crate.total_size(), 5000)

    # --- parts created ---

    def test_each_box_has_size(self):
        crate = Crate(2, 50)
        self.assertEqual(crate.boxes[0].get_size(), 50)
        self.assertEqual(crate.boxes[1].get_size(), 50)

    # --- Hidden ---

    def test_hidden_count_and_total(self):
        crate = Crate(4, 25)
        self.assertEqual(crate.count_boxes(), 4)
        self.assertEqual(crate.total_size(), 100)

    def test_hidden_total_six(self):
        crate = Crate(6, 30)
        self.assertEqual(crate.total_size(), 180)

    def test_hidden_single(self):
        crate = Crate(1, 500)
        self.assertEqual(crate.total_size(), 500)

    def test_hidden_zero_total(self):
        crate = Crate(0, 999)
        self.assertEqual(crate.total_size(), 0)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

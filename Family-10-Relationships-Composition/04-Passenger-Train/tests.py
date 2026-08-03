"""Unit tests for Passenger Train -- Family 10, Assessment 04."""

import unittest

from solution import Carriage, Train


class TestTrain(unittest.TestCase):

    # --- count ---

    def test_creates_correct_count(self):
        train = Train(3, 100)
        self.assertEqual(train.count_carriages(), 3)

    def test_one_carriage(self):
        train = Train(1, 100)
        self.assertEqual(train.count_carriages(), 1)
        self.assertEqual(train.total_seats(), 100)

    def test_zero_carriages(self):
        train = Train(0, 100)
        self.assertEqual(train.count_carriages(), 0)
        self.assertEqual(train.total_seats(), 0)

    # --- total_seats ---

    def test_total_seats(self):
        train = Train(3, 100)
        self.assertEqual(train.total_seats(), 300)

    def test_different_seats(self):
        train = Train(3, 50)
        self.assertEqual(train.total_seats(), 150)

    def test_large(self):
        train = Train(5, 1000)
        self.assertEqual(train.total_seats(), 5000)

    # --- parts created ---

    def test_each_carriage_has_seats(self):
        train = Train(2, 50)
        self.assertEqual(train.carriages[0].get_seats(), 50)
        self.assertEqual(train.carriages[1].get_seats(), 50)

    # --- Hidden ---

    def test_hidden_count_and_total(self):
        train = Train(4, 25)
        self.assertEqual(train.count_carriages(), 4)
        self.assertEqual(train.total_seats(), 100)

    def test_hidden_total_six(self):
        train = Train(6, 30)
        self.assertEqual(train.total_seats(), 180)

    def test_hidden_single(self):
        train = Train(1, 500)
        self.assertEqual(train.total_seats(), 500)

    def test_hidden_zero_total(self):
        train = Train(0, 999)
        self.assertEqual(train.total_seats(), 0)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

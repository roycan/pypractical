"""Unit tests for Points Board -- Family 07, Assessment 02."""

import unittest

try:
    from solution import Board, Easy, Hard
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestPointsBoard(unittest.TestCase):

    # --- Empty board ---

    def test_board_starts_empty(self):
        board = Board()
        self.assertEqual(board.points_list(), [])

    # --- points_list() ---

    def test_points_list_one_easy(self):
        board = Board()
        board.add(Easy("A", 10))
        self.assertEqual(board.points_list(), [10])

    def test_points_list_one_hard(self):
        board = Board()
        board.add(Hard("B", 10))
        self.assertEqual(board.points_list(), [30])

    def test_points_list_mixed(self):
        board = Board()
        board.add(Easy("A", 10))
        board.add(Hard("B", 10))
        self.assertEqual(board.points_list(), [10, 30])

    def test_points_list_order(self):
        board = Board()
        board.add(Hard("B", 10))
        board.add(Easy("A", 10))
        self.assertEqual(board.points_list(), [30, 10])

    # --- total_points() ---

    def test_total_points_mixed(self):
        board = Board()
        board.add(Easy("A", 10))
        board.add(Hard("B", 10))
        self.assertEqual(board.total_points(), 40)

    def test_total_points_single_easy(self):
        board = Board()
        board.add(Easy("A", 10))
        self.assertEqual(board.total_points(), 10)

    def test_total_points_all_easy(self):
        board = Board()
        board.add(Easy("A", 10))
        board.add(Easy("B", 20))
        self.assertEqual(board.points_list(), [10, 20])
        self.assertEqual(board.total_points(), 30)

    def test_total_points_all_hard(self):
        board = Board()
        board.add(Hard("A", 10))
        board.add(Hard("B", 20))
        self.assertEqual(board.points_list(), [30, 60])
        self.assertEqual(board.total_points(), 90)

    # --- Hidden ---

    def test_hidden_three_mixed(self):
        board = Board()
        board.add(Easy("A", 20))
        board.add(Hard("B", 20))
        board.add(Easy("C", 5))
        self.assertEqual(board.points_list(), [20, 60, 5])
        self.assertEqual(board.total_points(), 85)

    def test_hidden_easy_level(self):
        board = Board()
        board.add(Easy("C", 7))
        self.assertEqual(board.points_list(), [7])

    def test_hidden_large_mixed(self):
        board = Board()
        board.add(Easy("A", 100))
        board.add(Hard("B", 100))
        self.assertEqual(board.points_list(), [100, 300])
        self.assertEqual(board.total_points(), 400)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

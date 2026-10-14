"""Unit tests for Computer Memory -- Family 10, Assessment 03."""

import unittest

try:
    from solution import Module, Computer
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestComputer(unittest.TestCase):

    # --- count ---

    def test_creates_correct_count(self):
        computer = Computer(3, 100)
        self.assertEqual(computer.count_modules(), 3)

    def test_one_module(self):
        computer = Computer(1, 100)
        self.assertEqual(computer.count_modules(), 1)
        self.assertEqual(computer.total_memory(), 100)

    def test_zero_modules(self):
        computer = Computer(0, 100)
        self.assertEqual(computer.count_modules(), 0)
        self.assertEqual(computer.total_memory(), 0)

    # --- total_memory ---

    def test_total_memory(self):
        computer = Computer(3, 100)
        self.assertEqual(computer.total_memory(), 300)

    def test_different_size(self):
        computer = Computer(3, 50)
        self.assertEqual(computer.total_memory(), 150)

    def test_large(self):
        computer = Computer(5, 1000)
        self.assertEqual(computer.total_memory(), 5000)

    # --- parts created ---

    def test_each_module_has_size(self):
        computer = Computer(2, 50)
        self.assertEqual(computer.modules[0].get_size(), 50)
        self.assertEqual(computer.modules[1].get_size(), 50)

    # --- Hidden ---

    def test_hidden_count_and_total(self):
        computer = Computer(4, 25)
        self.assertEqual(computer.count_modules(), 4)
        self.assertEqual(computer.total_memory(), 100)

    def test_hidden_total_six(self):
        computer = Computer(6, 30)
        self.assertEqual(computer.total_memory(), 180)

    def test_hidden_single(self):
        computer = Computer(1, 500)
        self.assertEqual(computer.total_memory(), 500)

    def test_hidden_zero_total(self):
        computer = Computer(0, 999)
        self.assertEqual(computer.total_memory(), 0)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

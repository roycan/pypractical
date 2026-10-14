"""Unit tests for Computer Peripherals -- Family 12, Assessment 01."""

import unittest

try:
    from solution import Peripheral, Computer
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestComputerPeripherals(unittest.TestCase):

    # --- empty ---

    def test_empty_count(self):
        computer = Computer("MyPC")
        self.assertEqual(computer.count_peripherals(), 0)

    def test_empty_names(self):
        computer = Computer("MyPC")
        self.assertEqual(computer.list_peripheral_names(), [])

    def test_empty_has_type(self):
        computer = Computer("MyPC")
        self.assertFalse(computer.has_type("keyboard"))

    # --- add ---

    def test_add_one(self):
        computer = Computer("MyPC")
        computer.add_peripheral(Peripheral("K120", "keyboard"))
        self.assertEqual(computer.count_peripherals(), 1)

    def test_add_two(self):
        computer = Computer("MyPC")
        computer.add_peripheral(Peripheral("K120", "keyboard"))
        computer.add_peripheral(Peripheral("M100", "mouse"))
        self.assertEqual(computer.count_peripherals(), 2)

    # --- list names ---

    def test_list_names(self):
        computer = Computer("MyPC")
        computer.add_peripheral(Peripheral("K120", "keyboard"))
        computer.add_peripheral(Peripheral("M100", "mouse"))
        self.assertEqual(computer.list_peripheral_names(), ["K120", "M100"])

    # --- has_type ---

    def test_has_type_true(self):
        computer = Computer("MyPC")
        computer.add_peripheral(Peripheral("K120", "keyboard"))
        self.assertTrue(computer.has_type("keyboard"))

    def test_has_type_false(self):
        computer = Computer("MyPC")
        computer.add_peripheral(Peripheral("K120", "keyboard"))
        self.assertFalse(computer.has_type("monitor"))

    # --- remove ---

    def test_remove_found(self):
        computer = Computer("MyPC")
        computer.add_peripheral(Peripheral("K120", "keyboard"))
        self.assertTrue(computer.remove_peripheral("K120"))
        self.assertEqual(computer.count_peripherals(), 0)

    def test_remove_not_found(self):
        computer = Computer("MyPC")
        computer.add_peripheral(Peripheral("K120", "keyboard"))
        self.assertFalse(computer.remove_peripheral("M100"))
        self.assertEqual(computer.count_peripherals(), 1)

    def test_remove_middle(self):
        computer = Computer("MyPC")
        computer.add_peripheral(Peripheral("A", "keyboard"))
        computer.add_peripheral(Peripheral("B", "mouse"))
        computer.add_peripheral(Peripheral("C", "monitor"))
        self.assertTrue(computer.remove_peripheral("B"))
        self.assertEqual(computer.list_peripheral_names(), ["A", "C"])

    # --- hidden ---

    def test_hidden_count_three(self):
        computer = Computer("PC")
        computer.add_peripheral(Peripheral("A", "keyboard"))
        computer.add_peripheral(Peripheral("B", "mouse"))
        computer.add_peripheral(Peripheral("C", "monitor"))
        self.assertEqual(computer.count_peripherals(), 3)

    def test_hidden_has_type_among_many(self):
        computer = Computer("PC")
        computer.add_peripheral(Peripheral("A", "keyboard"))
        computer.add_peripheral(Peripheral("B", "mouse"))
        computer.add_peripheral(Peripheral("C", "monitor"))
        self.assertTrue(computer.has_type("monitor"))

    def test_hidden_independent_computers(self):
        c1 = Computer("PC1")
        c2 = Computer("PC2")
        c1.add_peripheral(Peripheral("K120", "keyboard"))
        c2.add_peripheral(Peripheral("M100", "mouse"))
        self.assertEqual(c1.count_peripherals(), 1)
        self.assertEqual(c2.count_peripherals(), 1)

    def test_hidden_peripheral_getters(self):
        p = Peripheral("K120", "keyboard")
        self.assertEqual(p.get_name(), "K120")
        self.assertEqual(p.get_type(), "keyboard")

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()
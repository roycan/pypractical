"""Unit tests for Ticket Price -- Family 06, Assessment 03."""

import unittest

try:
    from solution import Ticket, FirstClass
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestTicketPrice(unittest.TestCase):

    # --- Base method ---

    def test_ticket_price_base(self):
        ticket = Ticket("Economy", 300)
        self.assertEqual(ticket.price(), 600)

    def test_ticket_get_name(self):
        ticket = Ticket("Economy", 300)
        self.assertEqual(ticket.get_name(), "Economy")

    # --- Override ---

    def test_first_class_overrides_price(self):
        first = FirstClass("Economy", 300)
        self.assertEqual(first.price(), 1200)

    def test_same_distance_different_price(self):
        self.assertEqual(Ticket("Route", 150).price(), 300)
        self.assertEqual(FirstClass("Route", 150).price(), 600)

    def test_first_class_larger_distance(self):
        first = FirstClass("Long", 500)
        self.assertEqual(first.price(), 2000)

    # --- Inherited methods ---

    def test_first_class_inherits_get_name(self):
        first = FirstClass("Economy", 300)
        self.assertEqual(first.get_name(), "Economy")

    def test_first_class_inherits_get_distance(self):
        first = FirstClass("Economy", 300)
        self.assertEqual(first.get_distance(), 300)

    # --- Hidden ---

    def test_hidden_ticket_base(self):
        self.assertEqual(Ticket("Hop", 50).price(), 100)

    def test_hidden_first_class_override(self):
        self.assertEqual(FirstClass("Route", 250).price(), 1000)

    def test_hidden_inherited_getters(self):
        first = FirstClass("Economy", 300)
        self.assertEqual(first.get_name(), "Economy")
        self.assertEqual(first.get_distance(), 300)

    def test_hidden_parent_and_child_coexist(self):
        self.assertEqual(Ticket("Economy", 300).price(), 600)
        self.assertEqual(FirstClass("Economy", 300).price(), 1200)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

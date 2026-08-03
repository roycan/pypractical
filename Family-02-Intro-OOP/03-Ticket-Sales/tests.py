"""Unit tests for Ticket Sales -- Family 02, Assessment 03."""

import unittest

try:
    from solution import Ticket
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestTicketSales(unittest.TestCase):

    # --- Ticket attributes ---

    def test_event_stored(self):
        ticket = Ticket("Concert", 500, 2)
        self.assertEqual(ticket.event, "Concert")

    def test_price_stored(self):
        ticket = Ticket("Concert", 500, 2)
        self.assertEqual(ticket.price, 500)

    def test_seats_stored(self):
        ticket = Ticket("Concert", 500, 2)
        self.assertEqual(ticket.seats, 2)

    # --- potential_revenue (basic) ---

    def test_potential_revenue_basic(self):
        ticket = Ticket("Concert", 500, 2)
        self.assertEqual(ticket.potential_revenue(), 1000)

    def test_potential_revenue_single_seat(self):
        ticket = Ticket("Talk", 500, 1)
        self.assertEqual(ticket.potential_revenue(), 500)

    # --- Boundary ---

    def test_potential_revenue_zero_seats(self):
        ticket = Ticket("Webinar", 150, 0)
        self.assertEqual(ticket.potential_revenue(), 0)

    # --- Typical ---

    def test_potential_revenue_typical(self):
        ticket = Ticket("Play", 350, 8)
        self.assertEqual(ticket.potential_revenue(), 2800)

    # --- Objects are independent ---

    def test_two_tickets_independent(self):
        first = Ticket("Concert", 500, 2)
        second = Ticket("Movie", 300, 5)
        self.assertEqual(first.potential_revenue(), 1000)
        self.assertEqual(second.potential_revenue(), 1500)

    def test_changing_one_does_not_affect_other(self):
        first = Ticket("Concert", 500, 2)
        second = Ticket("Movie", 300, 5)
        first.seats = 10
        self.assertEqual(first.potential_revenue(), 5000)
        self.assertEqual(second.potential_revenue(), 1500)

    # --- Hidden ---

    def test_hidden_large_values(self):
        ticket = Ticket("Final", 2000, 30)
        self.assertEqual(ticket.potential_revenue(), 60000)

    def test_hidden_small_values(self):
        ticket = Ticket("Open Mic", 12, 4)
        self.assertEqual(ticket.potential_revenue(), 48)

    def test_hidden_mixed(self):
        ticket = Ticket("Festival", 180, 9)
        self.assertEqual(ticket.potential_revenue(), 1620)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

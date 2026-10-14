"""Unit tests for Fee Report -- Family 07, Assessment 03."""

import unittest

try:
    from solution import Report, Cash, Card
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestFeeReport(unittest.TestCase):

    # --- Empty report ---

    def test_report_starts_empty(self):
        report = Report()
        self.assertEqual(report.fees(), [])

    # --- fees() ---

    def test_fees_one_cash(self):
        report = Report()
        report.add(Cash("A", 100))
        self.assertEqual(report.fees(), [0])

    def test_fees_one_card(self):
        report = Report()
        report.add(Card("B", 100))
        self.assertEqual(report.fees(), [10])

    def test_fees_mixed(self):
        report = Report()
        report.add(Cash("A", 100))
        report.add(Card("B", 100))
        self.assertEqual(report.fees(), [0, 10])

    def test_fees_order(self):
        report = Report()
        report.add(Card("B", 100))
        report.add(Cash("A", 100))
        self.assertEqual(report.fees(), [10, 0])

    # --- total_fees() ---

    def test_total_fees_mixed(self):
        report = Report()
        report.add(Cash("A", 100))
        report.add(Card("B", 100))
        self.assertEqual(report.total_fees(), 10)

    def test_total_fees_single_cash(self):
        report = Report()
        report.add(Cash("A", 100))
        self.assertEqual(report.total_fees(), 0)

    def test_total_fees_all_cash(self):
        report = Report()
        report.add(Cash("A", 50))
        report.add(Cash("B", 70))
        self.assertEqual(report.fees(), [0, 0])
        self.assertEqual(report.total_fees(), 0)

    def test_total_fees_all_card(self):
        report = Report()
        report.add(Card("A", 50))
        report.add(Card("B", 70))
        self.assertEqual(report.fees(), [5, 7])
        self.assertEqual(report.total_fees(), 12)

    # --- Hidden ---

    def test_hidden_three_mixed(self):
        report = Report()
        report.add(Cash("A", 200))
        report.add(Card("B", 200))
        report.add(Cash("C", 50))
        self.assertEqual(report.fees(), [0, 20, 0])
        self.assertEqual(report.total_fees(), 20)

    def test_hidden_card_odd_amount(self):
        report = Report()
        report.add(Card("C", 101))
        self.assertEqual(report.fees(), [10])

    def test_hidden_large_mixed(self):
        report = Report()
        report.add(Card("A", 1000))
        report.add(Cash("B", 1000))
        self.assertEqual(report.fees(), [100, 0])
        self.assertEqual(report.total_fees(), 100)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

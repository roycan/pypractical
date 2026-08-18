"""Unit tests for Sale Receipt -- Family 13, Assessment 01."""

import unittest

try:
    from solution import Sale, Receipt
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestSaleReceipt(unittest.TestCase):

    # --- Sale (data) ---

    def test_sale_count(self):
        sale = Sale()
        sale.add_amount(100)
        sale.add_amount(200)
        self.assertEqual(sale.count(), 2)

    def test_sale_total(self):
        sale = Sale()
        sale.add_amount(100)
        sale.add_amount(200)
        self.assertEqual(sale.total(), 300)

    def test_sale_empty(self):
        sale = Sale()
        self.assertEqual(sale.count(), 0)
        self.assertEqual(sale.total(), 0)

    def test_sale_single(self):
        sale = Sale()
        sale.add_amount(100)
        self.assertEqual(sale.count(), 1)
        self.assertEqual(sale.total(), 100)

    # --- Receipt (presentation) ---

    def test_receipt_summary(self):
        sale = Sale()
        sale.add_amount(100)
        sale.add_amount(200)
        receipt = Receipt()
        self.assertEqual(receipt.summary(sale), "Items: 2, Total: 300")

    def test_receipt_summary_empty(self):
        receipt = Receipt()
        self.assertEqual(receipt.summary(Sale()), "Items: 0, Total: 0")

    def test_receipt_summary_single(self):
        sale = Sale()
        sale.add_amount(50)
        receipt = Receipt()
        self.assertEqual(receipt.summary(sale), "Items: 1, Total: 50")

    def test_receipt_does_not_store_data(self):
        receipt1 = Receipt()
        sale_a = Sale()
        sale_a.add_amount(100)
        receipt2 = Receipt()
        sale_b = Sale()
        sale_b.add_amount(999)
        self.assertEqual(receipt1.summary(sale_a), "Items: 1, Total: 100")
        self.assertEqual(receipt2.summary(sale_b), "Items: 1, Total: 999")

    # --- Hidden ---

    def test_hidden_summary_three(self):
        sale = Sale()
        sale.add_amount(10)
        sale.add_amount(20)
        sale.add_amount(30)
        receipt = Receipt()
        self.assertEqual(receipt.summary(sale), "Items: 3, Total: 60")

    def test_hidden_two_sales_independent(self):
        sale1 = Sale()
        sale1.add_amount(100)
        sale1.add_amount(200)
        sale2 = Sale()
        sale2.add_amount(5)
        self.assertEqual(Receipt().summary(sale1), "Items: 2, Total: 300")
        self.assertEqual(Receipt().summary(sale2), "Items: 1, Total: 5")

    def test_hidden_large(self):
        sale = Sale()
        sale.add_amount(1000)
        sale.add_amount(2000)
        receipt = Receipt()
        self.assertEqual(receipt.summary(sale), "Items: 2, Total: 3000")

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

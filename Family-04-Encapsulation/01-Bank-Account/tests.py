"""Unit tests for Bank Account -- Family 04, Assessment 01."""

import unittest

from solution import BankAccount


class TestBankAccount(unittest.TestCase):

    # --- Basic ---

    def test_owner_stored(self):
        account = BankAccount("Ada", 1000)
        self.assertEqual(account.owner, "Ada")

    def test_initial_balance(self):
        account = BankAccount("Ada", 1000)
        self.assertEqual(account.get_balance(), 1000)

    def test_deposit_increases(self):
        account = BankAccount("Ada", 1000)
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)

    def test_withdraw_decreases(self):
        account = BankAccount("Ada", 1000)
        account.withdraw(300)
        self.assertEqual(account.get_balance(), 700)

    # --- Validation ---

    def test_deposit_zero_ignored(self):
        account = BankAccount("Ada", 1000)
        account.deposit(0)
        self.assertEqual(account.get_balance(), 1000)

    def test_deposit_negative_ignored(self):
        account = BankAccount("Ada", 1000)
        account.deposit(-200)
        self.assertEqual(account.get_balance(), 1000)

    def test_withdraw_more_than_balance_ignored(self):
        account = BankAccount("Ada", 1000)
        account.withdraw(2000)
        self.assertEqual(account.get_balance(), 1000)

    def test_withdraw_negative_ignored(self):
        account = BankAccount("Ada", 1000)
        account.withdraw(-50)
        self.assertEqual(account.get_balance(), 1000)

    def test_withdraw_exact_balance_to_zero(self):
        account = BankAccount("Bob", 500)
        account.withdraw(500)
        self.assertEqual(account.get_balance(), 0)

    # --- Typical ---

    def test_multiple_operations(self):
        account = BankAccount("Ada", 1000)
        account.deposit(500)
        account.withdraw(200)
        account.withdraw(300)
        self.assertEqual(account.get_balance(), 1000)

    # --- Hidden ---

    def test_hidden_large_values(self):
        account = BankAccount("Cy", 10000)
        account.deposit(5000)
        account.withdraw(15000)
        self.assertEqual(account.get_balance(), 0)

    def test_hidden_cannot_overdraft_sequence(self):
        account = BankAccount("Dee", 200)
        account.withdraw(150)
        account.withdraw(100)
        self.assertEqual(account.get_balance(), 50)

    def test_hidden_deposit_then_withdraw_equal(self):
        account = BankAccount("Eve", 0)
        account.deposit(250)
        account.withdraw(250)
        self.assertEqual(account.get_balance(), 0)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

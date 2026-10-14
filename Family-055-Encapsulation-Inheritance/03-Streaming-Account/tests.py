"""Unit tests for Streaming Account -- Family 055, Assessment 03."""

import contextlib
import io
import unittest

try:
    from solution import Account, PremiumAccount
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


def _construction_output(cls, *args):
    """Construct cls(*args) while capturing stdout.

    Capturing only what is printed DURING the call keeps demo output from
    polluting the validation checks.

    Args:
        cls (type): The class to instantiate.
        *args: The constructor arguments.

    Returns:
        tuple: The text printed during construction and the new object.
    """
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        obj = cls(*args)
    return buffer.getvalue().strip(), obj


class TestStreamingAccount(unittest.TestCase):

    # --- Inheritance ---

    def test_premium_account_is_subclass_of_account(self):
        self.assertTrue(issubclass(PremiumAccount, Account))

    def test_premium_account_instance_is_an_account(self):
        premium = PremiumAccount("ben@mail.com", "Ben", 4)
        self.assertIsInstance(premium, PremiumAccount)
        self.assertIsInstance(premium, Account)

    def test_premium_account_inherits_email_via_super(self):
        premium = PremiumAccount("ben@mail.com", "Ben", 4)
        self.assertEqual(premium.email, "ben@mail.com")

    def test_premium_account_inherits_owner_via_super(self):
        premium = PremiumAccount("ben@mail.com", "Ben", 4)
        self.assertEqual(premium.owner, "Ben")

    def test_premium_account_uses_inherited_display_info(self):
        premium = PremiumAccount("ben@mail.com", "Ben", 4)
        result = premium.display_info()
        self.assertIsInstance(result, str)
        self.assertIn("ben@mail.com", result)
        self.assertIn("Ben", result)

    # --- Encapsulation ---

    def test_value_stored_in_protected_attribute(self):
        premium = PremiumAccount("ben@mail.com", "Ben", 4)
        self.assertTrue(hasattr(premium, "_max_screens"))
        self.assertEqual(premium.get_max_screens(), 4)

    def test_zero_screens_prints_warning(self):
        out, _ = _construction_output(PremiumAccount, "cy@mail.com", "Cy", 0)
        self.assertIn("positive", out.lower())

    def test_negative_screens_prints_warning(self):
        out, _ = _construction_output(PremiumAccount, "cy@mail.com", "Cy", -1)
        self.assertIn("positive", out.lower())

    def test_invalid_screens_stored_as_zero_fallback(self):
        _, premium = _construction_output(PremiumAccount, "cy@mail.com", "Cy", -1)
        self.assertEqual(premium.get_max_screens(), 0)

    def test_valid_premium_account_prints_no_warning(self):
        out, _ = _construction_output(PremiumAccount, "ben@mail.com", "Ben", 4)
        self.assertNotIn("positive", out.lower())

    # --- Integration ---

    def test_two_premium_accounts_are_independent(self):
        first = PremiumAccount("ben@mail.com", "Ben", 4)
        second = PremiumAccount("dee@mail.com", "Dee", 2)
        self.assertEqual(first.get_max_screens(), 4)
        self.assertEqual(second.get_max_screens(), 2)

    # --- Hidden ---

    def test_hidden_account_works_standalone(self):
        account = Account("ada@mail.com", "Ada")
        self.assertEqual(account.email, "ada@mail.com")
        self.assertEqual(account.owner, "Ada")
        self.assertIn("ada@mail.com", account.display_info())

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

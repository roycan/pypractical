"""Streaming Account -- Family 055, Assessment 03 (teacher solution)."""


# Provided class. Do NOT modify it.
class Account:
    """Represents a basic streaming account."""

    def __init__(self, email, owner):
        self.email = email
        self.owner = owner

    def display_info(self):
        """Return a one-line description of the account.

        Returns:
            str: The account's email and owner.
        """
        return f"Email: {self.email}, Owner: {self.owner}"


class PremiumAccount(Account):
    """Represents a premium account with a protected screen limit."""

    def __init__(self, email, owner, max_screens):
        """Initialize a premium account.

        Args:
            email (str): The account's email.
            owner (str): The account's owner.
            max_screens (int): The maximum number of screens.
        """
        super().__init__(email, owner)
        if max_screens <= 0:
            print("The number of screens must be positive")
            self._max_screens = 0
        else:
            self._max_screens = max_screens

    def get_max_screens(self):
        """Return the protected screen limit.

        Returns:
            int: The maximum number of screens (0 when it was not recorded).
        """
        return self._max_screens


if __name__ == "__main__":
    account = Account("ada@mail.com", "Ada")
    print(account.display_info())

    premium = PremiumAccount("ben@mail.com", "Ben", 4)
    print(premium.display_info())
    print(premium.get_max_screens())

    bad_premium = PremiumAccount("cy@mail.com", "Cy", -1)
    print(bad_premium.get_max_screens())

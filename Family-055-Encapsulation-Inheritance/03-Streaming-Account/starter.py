"""Streaming Account -- Family 055, Assessment 03 (starter).

The Account class is provided and complete. Complete the PremiumAccount class.
"""


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


class PremiumAccount():                        # TODO 1: make PremiumAccount inherit from Account
    """Represents a premium account with a protected screen limit."""

    def __init__(self, email, owner, max_screens):
        """Initialize a premium account.

        Args:
            email (str): The account's email.
            owner (str): The account's owner.
            max_screens (int): The maximum number of screens.
        """

        # TODO 2: Call super().__init__(email, owner).
        # TODO 3: If max_screens is zero or negative, print
        #         "The number of screens must be positive" and store 0
        #         (0 means "not recorded"); otherwise store the value in the
        #         protected attribute _max_screens.

        return

    def get_max_screens(self):
        """Return the protected screen limit.

        Returns:
            int: The maximum number of screens (0 when it was not recorded).
        """

        # TODO 4: Return the protected _max_screens.

        return 0

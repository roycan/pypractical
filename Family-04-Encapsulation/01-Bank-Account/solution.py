"""Bank Account -- Family 04, Assessment 01 (teacher solution)."""


class BankAccount:
    """Represents one bank account with a protected balance."""

    def __init__(self, owner, starting_balance):
        """Initialize a bank account.

        Args:
            owner (str): The owner's name.
            starting_balance (int): The starting balance (non-negative).
        """
        self.owner = owner
        self._balance = starting_balance

    def get_balance(self):
        """Return the protected balance.

        Returns:
            int: The current balance.
        """
        return self._balance

    def deposit(self, amount):
        """Add a valid amount to the balance.

        Args:
            amount (int): The amount to deposit.
        """
        if amount > 0:
            self._balance = self._balance + amount
        return

    def withdraw(self, amount):
        """Remove a valid amount from the balance.

        Args:
            amount (int): The amount to withdraw.
        """
        if amount > 0 and amount <= self._balance:
            self._balance = self._balance - amount
        return


if __name__ == "__main__":
    account = BankAccount("Ada", 1000)
    print(account.owner)
    print(account.get_balance())
    account.deposit(500)
    print(account.get_balance())
    account.withdraw(300)
    print(account.get_balance())

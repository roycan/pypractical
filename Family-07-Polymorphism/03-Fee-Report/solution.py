"""Fee Report -- Family 07, Assessment 03 (teacher solution)."""


# Provided class. Do NOT modify it.
class Cash:
    """A cash payment with no fee."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def fee(self):
        """Return the fee for this payment (0)."""
        return 0


# Provided class. Do NOT modify it.
class Card:
    """A card payment with a 10 percent fee."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def fee(self):
        """Return the fee for this payment (amount // 10)."""
        return self.amount // 10


class Report:
    """A report that collects payments and reports their fees."""

    def __init__(self):
        """Initialize an empty report.

        The report starts with no payments.
        """
        self.payments = []

    def add(self, payment):
        """Add a payment to the report.

        Args:
            payment: A payment that has a fee() method.
        """
        self.payments.append(payment)

    def fees(self):
        """Return the fee of each payment in the report.

        Returns:
            list: The fee of each payment.
        """
        result = []
        for payment in self.payments:
            result.append(payment.fee())
        return result

    def total_fees(self):
        """Return the total fees of all payments in the report.

        Returns:
            int: The total fees of all payments.
        """
        result = 0
        for payment in self.payments:
            result = result + payment.fee()
        return result


if __name__ == "__main__":
    report = Report()
    report.add(Cash("A", 100))
    report.add(Card("B", 100))
    print(report.fees())
    print(report.total_fees())

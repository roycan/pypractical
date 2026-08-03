"""Ticket Sales -- Family 02, Assessment 03 (teacher solution)."""


class Ticket:
    """Represents one event at the venue."""

    def __init__(self, event, price, seats):
        """Initialize a ticket.

        Args:
            event (str): Event name.
            price (int): Price for one ticket.
            seats (int): Number of seats sold.
        """
        self.event = event
        self.price = price
        self.seats = seats

    def potential_revenue(self):
        """Return the potential revenue for this event.

        Returns:
            int: price multiplied by seats.
        """
        return self.price * self.seats


if __name__ == "__main__":
    ticket = Ticket("Concert", 500, 2)
    print(ticket.event)
    print(ticket.price)
    print(ticket.seats)
    print(ticket.potential_revenue())

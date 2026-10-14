"""Ticket Price -- Family 06, Assessment 03 (teacher solution)."""


# Provided class. Do NOT modify it.
class Ticket:
    """Represents a standard ticket."""

    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def get_name(self):
        """Return the ticket's name."""
        return self.name

    def get_distance(self):
        """Return the ticket's distance."""
        return self.distance

    def price(self):
        """Return the ticket price (2 per unit of distance)."""
        return self.distance * 2


class FirstClass(Ticket):
    """Represents a first-class ticket."""

    def __init__(self, name, distance):
        """Initialize a first-class ticket.

        Args:
            name (str): The ticket's name.
            distance (int): The ticket's distance.
        """
        super().__init__(name, distance)

    def price(self):
        """Return the first-class price (4 per unit of distance).

        Returns:
            int: The first-class price.
        """
        return self.distance * 4


if __name__ == "__main__":
    ticket = Ticket("Economy", 300)
    print(ticket.get_name())
    print(ticket.price())

    first = FirstClass("Economy", 300)
    print(first.get_name())
    print(first.price())

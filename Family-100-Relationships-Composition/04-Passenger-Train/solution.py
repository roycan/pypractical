"""Passenger Train -- Family 10, Assessment 04 (teacher solution)."""


# Provided class. Do NOT modify it.
class Carriage:
    """Represents one passenger carriage."""

    def __init__(self, seats):
        self.seats = seats

    def get_seats(self):
        """Return the carriage's number of seats."""
        return self.seats


class Train:
    """Represents a train that creates and owns its carriages."""

    def __init__(self, carriage_count, seats):
        """Create the carriages that belong to this train.

        Args:
            carriage_count (int): How many carriages to create.
            seats (int): The number of seats in each carriage.
        """
        self.carriages = []
        for i in range(carriage_count):
            self.carriages.append(Carriage(seats))

    def count_carriages(self):
        """Return the number of carriages in the train."""
        return len(self.carriages)

    def total_seats(self):
        """Return the total number of seats across all carriages."""
        total = 0
        for carriage in self.carriages:
            total = total + carriage.get_seats()
        return total


if __name__ == "__main__":
    train = Train(3, 100)
    print(train.count_carriages())
    print(train.total_seats())

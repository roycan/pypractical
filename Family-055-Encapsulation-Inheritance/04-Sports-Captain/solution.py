"""Sports Captain -- Family 055, Assessment 04 (teacher solution)."""


# Provided class. Do NOT modify it.
class Member:
    """Represents a basic club member."""

    def __init__(self, name, club):
        self.name = name
        self.club = club

    def display_info(self):
        """Return a one-line description of the member.

        Returns:
            str: The member's name and club.
        """
        return f"Name: {self.name}, Club: {self.club}"


class Captain(Member):
    """Represents a captain with a protected trophy count."""

    def __init__(self, name, club, trophies_won):
        """Initialize a captain.

        Args:
            name (str): The member's name.
            club (str): The member's club.
            trophies_won (int): The number of trophies won.
        """
        super().__init__(name, club)
        self.trophies_won = trophies_won

    @property
    def trophies_won(self):
        """Return the protected trophy count.

        Returns:
            int: The number of trophies won (0 when it was not recorded).
        """
        return self._trophies_won

    @trophies_won.setter
    def trophies_won(self, value):
        """Validate and store the trophy count.

        Args:
            value (int): The proposed number of trophies won.
        """
        if value <= 0:
            print("The number of trophies must be positive")
            self._trophies_won = 0
        else:
            self._trophies_won = value


if __name__ == "__main__":
    member = Member("Ana", "Chess")
    print(member.display_info())

    captain = Captain("Ben", "Football", 3)
    print(captain.display_info())
    print(captain.trophies_won)

    bad_captain = Captain("Cal", "Basketball", -1)
    print(bad_captain.trophies_won)

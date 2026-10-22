"""Sports Captain -- Family 055, Assessment 04 (starter).

The Member class is provided and complete. Complete the Captain class.
"""


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


class Captain():                               # TODO 1: make Captain inherit from Member
    """Represents a captain with a protected trophy count."""

    def __init__(self, name, club, trophies_won):
        """Initialize a captain.

        Args:
            name (str): The member's name.
            club (str): The member's club.
            trophies_won (int): The number of trophies won.
        """

        # TODO 2: Call super().__init__(name, club).
        # TODO 3: Assign trophies_won to self.trophies_won so the setter
        #         below validates and stores it.

        return

    @property
    def trophies_won(self):
        """Return the protected trophy count.

        Returns:
            int: The number of trophies won (0 when it was not recorded).
        """

        # TODO 4: Return the protected _trophies_won.

        return 0

    @trophies_won.setter
    def trophies_won(self, value):
        """Validate and store the trophy count.

        Args:
            value (int): The proposed number of trophies won.
        """

        # TODO 5: If value is zero or negative, print
        #         "The number of trophies must be positive" and store 0
        #         (0 means "not recorded"); otherwise store value in the
        #         protected attribute _trophies_won.

        return

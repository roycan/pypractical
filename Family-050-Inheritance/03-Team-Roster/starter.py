"""Team Roster -- Family 05, Assessment 03 (starter).

The Player class is provided and complete. Complete the Captain class.
"""


# Provided class. Do NOT modify it.
class Player:
    """Represents a basic player."""

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def get_name(self):
        """Return the player's name."""
        return self.name

    def get_number(self):
        """Return the player's number."""
        return self.number


class Captain(Player):
    """Represents a player who leads a team."""

    def __init__(self, name, number, team):
        """Initialize a captain.

        Args:
            name (str): The captain's name.
            number (int): The captain's number.
            team (str): The captain's team.
        """

        # TODO: Write your solution here.

        return

    def get_team(self):
        """Return the captain's team.

        Returns:
            str: The captain's team.
        """

        # TODO: Write your solution here.

        return ""

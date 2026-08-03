"""Team Roster -- Family 05, Assessment 03 (teacher solution)."""


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
        super().__init__(name, number)
        self.team = team

    def get_team(self):
        """Return the captain's team.

        Returns:
            str: The captain's team.
        """
        return self.team


if __name__ == "__main__":
    player = Player("Ada", 9)
    print(player.get_name())
    print(player.get_number())

    captain = Captain("Bo", 10, "Tigers")
    print(captain.get_name())
    print(captain.get_number())
    print(captain.get_team())

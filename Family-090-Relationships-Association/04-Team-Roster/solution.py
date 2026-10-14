"""Team Roster -- Family 09, Assessment 04 (teacher solution)."""


# Provided class. Do NOT modify it.
class Player:
    """Represents one player on a team."""

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_name(self):
        """Return the player's name."""
        return self.name

    def get_position(self):
        """Return the player's position."""
        return self.position


class Team:
    """Represents a team that holds many players."""

    def __init__(self):
        """Initialize a team with an empty list of players."""
        self.players = []

    def add_player(self, player):
        """Add one player to the team."""
        self.players.append(player)

    def count_players(self):
        """Return the number of players on the team."""
        return len(self.players)

    def find_by_name(self, name):
        """Return the first player with the given name, or None."""
        for player in self.players:
            if player.get_name() == name:
                return player
        return None


if __name__ == "__main__":
    team = Team()
    team.add_player(Player("Ada", "Guard"))
    team.add_player(Player("Bo", "Forward"))
    print(team.count_players())

    found = team.find_by_name("Ada")
    print(found.get_position())

    missing = team.find_by_name("Cy")
    print(missing)

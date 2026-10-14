"""Video Game Edition -- Family 055, Assessment 02 (teacher solution)."""


# Provided class. Do NOT modify it.
class Game:
    """Represents a basic game."""

    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def display_info(self):
        """Return a one-line description of the game.

        Returns:
            str: The game's title and genre.
        """
        return f"Title: {self.title}, Genre: {self.genre}"


class DeluxeEdition(Game):
    """Represents a deluxe edition with a protected bonus level count."""

    def __init__(self, title, genre, bonus_levels):
        """Initialize a deluxe edition.

        Args:
            title (str): The game's title.
            genre (str): The game's genre.
            bonus_levels (int): The number of bonus levels.
        """
        super().__init__(title, genre)
        if bonus_levels <= 0:
            print("The number of bonus levels must be positive")
            self._bonus_levels = 0
        else:
            self._bonus_levels = bonus_levels

    def get_bonus_levels(self):
        """Return the protected bonus level count.

        Returns:
            int: The number of bonus levels (0 when it was not recorded).
        """
        return self._bonus_levels


if __name__ == "__main__":
    game = Game("Chess", "Board")
    print(game.display_info())

    deluxe = DeluxeEdition("Elden Ring", "RPG", 40)
    print(deluxe.display_info())
    print(deluxe.get_bonus_levels())

    bad_deluxe = DeluxeEdition("Mystery Quest", "Puzzle", -2)
    print(bad_deluxe.get_bonus_levels())

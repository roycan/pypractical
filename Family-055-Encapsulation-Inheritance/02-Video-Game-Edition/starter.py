"""Video Game Edition -- Family 055, Assessment 02 (starter).

The Game class is provided and complete. Complete the DeluxeEdition class.
"""


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


class DeluxeEdition():                         # TODO 1: make DeluxeEdition inherit from Game
    """Represents a deluxe edition with a protected bonus level count."""

    def __init__(self, title, genre, bonus_levels):
        """Initialize a deluxe edition.

        Args:
            title (str): The game's title.
            genre (str): The game's genre.
            bonus_levels (int): The number of bonus levels.
        """

        # TODO 2: Call super().__init__(title, genre).
        # TODO 3: Assign bonus_levels to self.bonus_levels so the setter
        #         below validates and stores it.

        return

    @property
    def bonus_levels(self):
        """Return the protected bonus level count.

        Returns:
            int: The number of bonus levels (0 when it was not recorded).
        """

        # TODO 4: Return the protected _bonus_levels.

        return 0

    @bonus_levels.setter
    def bonus_levels(self, value):
        """Validate and store the bonus level count.

        Args:
            value (int): The proposed number of bonus levels.
        """

        # TODO 5: If value is zero or negative, print
        #         "The number of bonus levels must be positive" and store 0
        #         (0 means "not recorded"); otherwise store value in the
        #         protected attribute _bonus_levels.

        return

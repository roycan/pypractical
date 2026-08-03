"""Points Board -- Family 07, Assessment 02 (starter).

The Easy and Hard classes are provided and complete. Complete the Board class.
"""


# Provided class. Do NOT modify it.
class Easy:
    """An easy task that gives level * 1 points."""

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def points(self):
        """Return the points for this task (level * 1)."""
        return self.level * 1


# Provided class. Do NOT modify it.
class Hard:
    """A hard task that gives level * 3 points."""

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def points(self):
        """Return the points for this task (level * 3)."""
        return self.level * 3


class Board:
    """A game board that collects tasks and reports their points."""

    def __init__(self):
        """Initialize an empty board.

        The board starts with no entries.
        """

        # TODO: Write your solution here.

        return

    def add(self, entry):
        """Add a task to the board.

        Args:
            entry: A task that has a points() method.
        """

        # TODO: Write your solution here.

        return

    def points_list(self):
        """Return the points of each task on the board.

        Returns:
            list: The points of each task.
        """

        # TODO: Write your solution here.

        return []

    def total_points(self):
        """Return the total points of all tasks on the board.

        Returns:
            int: The total points of all tasks.
        """

        # TODO: Write your solution here.

        return 0

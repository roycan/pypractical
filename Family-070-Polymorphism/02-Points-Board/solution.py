"""Points Board -- Family 07, Assessment 02 (teacher solution)."""


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
        self.entries = []

    def add(self, entry):
        """Add a task to the board.

        Args:
            entry: A task that has a points() method.
        """
        self.entries.append(entry)

    def points_list(self):
        """Return the points of each task on the board.

        Returns:
            list: The points of each task.
        """
        result = []
        for entry in self.entries:
            result.append(entry.points())
        return result

    def total_points(self):
        """Return the total points of all tasks on the board.

        Returns:
            int: The total points of all tasks.
        """
        result = 0
        for entry in self.entries:
            result = result + entry.points()
        return result


if __name__ == "__main__":
    board = Board()
    board.add(Easy("A", 10))
    board.add(Hard("B", 10))
    print(board.points_list())
    print(board.total_points())

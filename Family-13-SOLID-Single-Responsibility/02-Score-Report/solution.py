"""Score Report -- Family 11, Assessment 02 (teacher solution)."""


class Score:
    """Stores points and computes the count and sum."""

    def __init__(self):
        """Initialize a score with an empty list of points."""
        self.points = []

    def add_point(self, point):
        """Record one point.

        Args:
            point (int): The point to add.
        """
        self.points.append(point)

    def count(self):
        """Return the number of recorded points.

        Returns:
            int: The number of points stored.
        """
        return len(self.points)

    def total(self):
        """Return the sum of all recorded points.

        Returns:
            int: The total of all points.
        """
        total = 0
        for point in self.points:
            total = total + point
        return total


class Report:
    """Formats a readable summary string from a Score."""

    def summary(self, score):
        """Build a summary string from the given score.

        Args:
            score (Score): The score to summarize.

        Returns:
            str: A summary of the score's count and sum.
        """
        return "Points: " + str(score.count()) + ", Sum: " + str(score.total())


if __name__ == "__main__":
    score = Score()
    score.add_point(100)
    score.add_point(200)
    print(score.count())
    print(score.total())

    report = Report()
    print(report.summary(score))

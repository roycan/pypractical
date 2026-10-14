"""Grade Checker -- Family 11, Assessment 01 (starter).

The Answer class is provided and complete. Complete the GradeChecker class.
"""


# Provided class. Do NOT modify it.
class Answer:
    """Represents one student's answer."""

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):
        """Return the student's name."""
        return self.name

    def get_score(self):
        """Return the student's score."""
        return self.score


class GradeChecker:
    """Checks answers without storing them."""

    def check_pass(self, answer, passing_score):
        """Return True if the answer's score is at least passing_score.

        Args:
            answer (Answer): The answer to check.
            passing_score (int): The minimum score to pass.

        Returns:
            bool: True if the answer passes.
        """

        # TODO: Write your solution here.

        return False

    def get_grade(self, answer):
        """Return the letter grade for the answer's score.

        Args:
            answer (Answer): The answer to grade.

        Returns:
            str: The letter grade (A, B, C, D, or F).
        """

        # TODO: Write your solution here.

        return ""

    def compare(self, answer1, answer2):
        """Return the name of the higher scorer, or "Tie".

        Args:
            answer1 (Answer): The first answer.
            answer2 (Answer): The second answer.

        Returns:
            str: The higher scorer's name, or "Tie" if equal.
        """

        # TODO: Write your solution here.

        return ""
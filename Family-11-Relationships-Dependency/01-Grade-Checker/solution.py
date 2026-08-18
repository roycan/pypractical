"""Grade Checker -- Family 11, Assessment 01 (teacher solution)."""


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
        """Return True if the answer's score is at least passing_score."""
        return answer.get_score() >= passing_score

    def get_grade(self, answer):
        """Return the letter grade for the answer's score."""
        score = answer.get_score()
        if score >= 90:
            return "A"
        if score >= 80:
            return "B"
        if score >= 70:
            return "C"
        if score >= 60:
            return "D"
        return "F"

    def compare(self, answer1, answer2):
        """Return the name of the higher scorer, or "Tie"."""
        score1 = answer1.get_score()
        score2 = answer2.get_score()
        if score1 > score2:
            return answer1.get_name()
        if score2 > score1:
            return answer2.get_name()
        return "Tie"


if __name__ == "__main__":
    checker = GradeChecker()
    answer = Answer("Ada", 85)
    print(checker.check_pass(answer, 60))
    print(checker.get_grade(answer))
    print(checker.compare(Answer("Ada", 85), Answer("Bo", 70)))
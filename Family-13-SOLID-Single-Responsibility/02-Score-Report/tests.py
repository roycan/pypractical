"""Unit tests for Score Report -- Family 11, Assessment 02."""

import unittest

try:
    from solution import Score, Report
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestScoreReport(unittest.TestCase):

    # --- Score (data) ---

    def test_score_count(self):
        score = Score()
        score.add_point(100)
        score.add_point(200)
        self.assertEqual(score.count(), 2)

    def test_score_total(self):
        score = Score()
        score.add_point(100)
        score.add_point(200)
        self.assertEqual(score.total(), 300)

    def test_score_empty(self):
        score = Score()
        self.assertEqual(score.count(), 0)
        self.assertEqual(score.total(), 0)

    def test_score_single(self):
        score = Score()
        score.add_point(100)
        self.assertEqual(score.count(), 1)
        self.assertEqual(score.total(), 100)

    # --- Report (presentation) ---

    def test_report_summary(self):
        score = Score()
        score.add_point(100)
        score.add_point(200)
        report = Report()
        self.assertEqual(report.summary(score), "Points: 2, Sum: 300")

    def test_report_summary_empty(self):
        report = Report()
        self.assertEqual(report.summary(Score()), "Points: 0, Sum: 0")

    def test_report_summary_single(self):
        score = Score()
        score.add_point(50)
        report = Report()
        self.assertEqual(report.summary(score), "Points: 1, Sum: 50")

    def test_report_does_not_store_data(self):
        report1 = Report()
        score_a = Score()
        score_a.add_point(100)
        report2 = Report()
        score_b = Score()
        score_b.add_point(999)
        self.assertEqual(report1.summary(score_a), "Points: 1, Sum: 100")
        self.assertEqual(report2.summary(score_b), "Points: 1, Sum: 999")

    # --- Hidden ---

    def test_hidden_summary_three(self):
        score = Score()
        score.add_point(10)
        score.add_point(20)
        score.add_point(30)
        report = Report()
        self.assertEqual(report.summary(score), "Points: 3, Sum: 60")

    def test_hidden_two_scores_independent(self):
        score1 = Score()
        score1.add_point(100)
        score1.add_point(200)
        score2 = Score()
        score2.add_point(5)
        self.assertEqual(Report().summary(score1), "Points: 2, Sum: 300")
        self.assertEqual(Report().summary(score2), "Points: 1, Sum: 5")

    def test_hidden_large(self):
        score = Score()
        score.add_point(1000)
        score.add_point(2000)
        report = Report()
        self.assertEqual(report.summary(score), "Points: 2, Sum: 3000")

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

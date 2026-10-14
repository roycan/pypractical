"""Unit tests for Grade Checker -- Family 11, Assessment 01."""

import unittest

try:
    from solution import Answer, GradeChecker
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestGradeChecker(unittest.TestCase):

    def setUp(self):
        self.checker = GradeChecker()

    # --- check_pass ---

    def test_pass_above_threshold(self):
        self.assertTrue(self.checker.check_pass(Answer("Ada", 75), 60))

    def test_pass_exact_threshold(self):
        self.assertTrue(self.checker.check_pass(Answer("Ada", 60), 60))

    def test_fail_below_threshold(self):
        self.assertFalse(self.checker.check_pass(Answer("Ada", 59), 60))

    # --- get_grade ---

    def test_grade_a(self):
        self.assertEqual(self.checker.get_grade(Answer("Ada", 95)), "A")

    def test_grade_b(self):
        self.assertEqual(self.checker.get_grade(Answer("Ada", 85)), "B")

    def test_grade_c(self):
        self.assertEqual(self.checker.get_grade(Answer("Ada", 75)), "C")

    def test_grade_d(self):
        self.assertEqual(self.checker.get_grade(Answer("Ada", 65)), "D")

    def test_grade_f(self):
        self.assertEqual(self.checker.get_grade(Answer("Ada", 55)), "F")

    def test_grade_boundary_90(self):
        self.assertEqual(self.checker.get_grade(Answer("Ada", 90)), "A")

    def test_grade_boundary_60(self):
        self.assertEqual(self.checker.get_grade(Answer("Ada", 60)), "D")

    def test_grade_boundary_59(self):
        self.assertEqual(self.checker.get_grade(Answer("Ada", 59)), "F")

    # --- compare ---

    def test_compare_first_higher(self):
        result = self.checker.compare(Answer("Ada", 85), Answer("Bo", 70))
        self.assertEqual(result, "Ada")

    def test_compare_second_higher(self):
        result = self.checker.compare(Answer("Ada", 70), Answer("Bo", 85))
        self.assertEqual(result, "Bo")

    def test_compare_tie(self):
        result = self.checker.compare(Answer("Ada", 85), Answer("Bo", 85))
        self.assertEqual(result, "Tie")

    # --- hidden ---

    def test_hidden_pass_high_threshold(self):
        self.assertFalse(self.checker.check_pass(Answer("Cy", 80), 90))

    def test_hidden_grade_boundary_80(self):
        self.assertEqual(self.checker.get_grade(Answer("Cy", 80)), "B")

    def test_hidden_compare_large_gap(self):
        result = self.checker.compare(Answer("Cy", 100), Answer("Da", 0))
        self.assertEqual(result, "Cy")

    def test_hidden_answer_getters(self):
        answer = Answer("Eve", 42)
        self.assertEqual(answer.get_name(), "Eve")
        self.assertEqual(answer.get_score(), 42)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()
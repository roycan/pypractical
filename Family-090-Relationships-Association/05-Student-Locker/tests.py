"""Unit tests for Student Locker -- Family 09, Assessment 05."""

import unittest

try:
    from solution import Locker, Student
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestStudentLocker(unittest.TestCase):

    # --- no locker ---

    def test_no_locker_by_default(self):
        student = Student("Ada")
        self.assertFalse(student.has_locker())

    def test_no_locker_number(self):
        student = Student("Ada")
        self.assertEqual(student.get_locker_number(), "No locker")

    # --- assign locker ---

    def test_assign_locker(self):
        student = Student("Ada")
        student.assign_locker(Locker(123, "12-24-36"))
        self.assertTrue(student.has_locker())

    def test_locker_number_after_assign(self):
        student = Student("Ada")
        student.assign_locker(Locker(123, "12-24-36"))
        self.assertEqual(student.get_locker_number(), 123)

    def test_locker_combination(self):
        locker = Locker(123, "12-24-36")
        self.assertEqual(locker.get_combination(), "12-24-36")

    # --- hidden ---

    def test_hidden_different_locker(self):
        student = Student("Bo")
        student.assign_locker(Locker(456, "10-20-30"))
        self.assertEqual(student.get_locker_number(), 456)

    def test_hidden_two_students_independent(self):
        s1 = Student("Ada")
        s2 = Student("Bo")
        s1.assign_locker(Locker(123, "12-24-36"))
        self.assertTrue(s1.has_locker())
        self.assertFalse(s2.has_locker())

    def test_hidden_locker_combination_number(self):
        locker = Locker(789, "99-88-77")
        self.assertEqual(locker.get_number(), 789)
        self.assertEqual(locker.get_combination(), "99-88-77")

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()
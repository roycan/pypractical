"""Unit tests for Student Club -- Family 09, Assessment 07."""

import unittest

try:
    from solution import Club, Student
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestStudentClub(unittest.TestCase):

    # --- empty ---

    def test_empty_clubs(self):
        student = Student("Ada")
        self.assertEqual(student.list_clubs(), [])

    def test_not_member_by_default(self):
        student = Student("Ada")
        self.assertFalse(student.is_member("Chess"))

    # --- join ---

    def test_join_one(self):
        student = Student("Ada")
        student.join_club(Club("Chess", "Play chess"))
        self.assertTrue(student.is_member("Chess"))

    def test_join_two(self):
        student = Student("Ada")
        student.join_club(Club("Chess", "Play chess"))
        student.join_club(Club("Art", "Paint"))
        self.assertEqual(student.list_clubs(), ["Chess", "Art"])

    def test_join_duplicate_no_effect(self):
        student = Student("Ada")
        club = Club("Chess", "Play chess")
        student.join_club(club)
        student.join_club(club)
        self.assertEqual(student.list_clubs(), ["Chess"])

    # --- is_member ---

    def test_member_true(self):
        student = Student("Ada")
        student.join_club(Club("Chess", "Play chess"))
        self.assertTrue(student.is_member("Chess"))

    def test_member_false(self):
        student = Student("Ada")
        student.join_club(Club("Chess", "Play chess"))
        self.assertFalse(student.is_member("Art"))

    # --- leave ---

    def test_leave_found(self):
        student = Student("Ada")
        student.join_club(Club("Chess", "Play chess"))
        self.assertTrue(student.leave_club("Chess"))
        self.assertFalse(student.is_member("Chess"))

    def test_leave_not_found(self):
        student = Student("Ada")
        student.join_club(Club("Chess", "Play chess"))
        self.assertFalse(student.leave_club("Art"))
        self.assertEqual(student.list_clubs(), ["Chess"])

    # --- hidden ---

    def test_hidden_join_three(self):
        student = Student("Bo")
        student.join_club(Club("Chess", "Play chess"))
        student.join_club(Club("Art", "Paint"))
        student.join_club(Club("Robotics", "Build robots"))
        self.assertEqual(student.list_clubs(), ["Chess", "Art", "Robotics"])

    def test_hidden_leave_middle(self):
        student = Student("Bo")
        student.join_club(Club("Chess", "Play chess"))
        student.join_club(Club("Art", "Paint"))
        student.join_club(Club("Robotics", "Build robots"))
        student.leave_club("Art")
        self.assertEqual(student.list_clubs(), ["Chess", "Robotics"])

    def test_hidden_independent_students(self):
        s1 = Student("Ada")
        s2 = Student("Bo")
        s1.join_club(Club("Chess", "Play chess"))
        s2.join_club(Club("Art", "Paint"))
        self.assertTrue(s1.is_member("Chess"))
        self.assertFalse(s1.is_member("Art"))
        self.assertTrue(s2.is_member("Art"))

    def test_hidden_club_getters(self):
        club = Club("Robotics", "Build robots")
        self.assertEqual(club.get_name(), "Robotics")
        self.assertEqual(club.get_description(), "Build robots")

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()
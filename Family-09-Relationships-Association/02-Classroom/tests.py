"""Unit tests for Classroom -- Family 09, Assessment 02."""

import unittest

from solution import Student, Classroom


class TestClassroom(unittest.TestCase):

    # --- count ---

    def test_empty_classroom_count(self):
        classroom = Classroom()
        self.assertEqual(classroom.count_students(), 0)

    def test_add_one_student(self):
        classroom = Classroom()
        classroom.add_student(Student("Ada", "9A"))
        self.assertEqual(classroom.count_students(), 1)

    def test_add_two_students(self):
        classroom = Classroom()
        classroom.add_student(Student("Ada", "9A"))
        classroom.add_student(Student("Bo", "9B"))
        self.assertEqual(classroom.count_students(), 2)

    # --- find_by_name ---

    def test_find_returns_student(self):
        classroom = Classroom()
        classroom.add_student(Student("Ada", "9A"))
        self.assertEqual(classroom.find_by_name("Ada").get_grade(), "9A")

    def test_find_not_found_returns_none(self):
        classroom = Classroom()
        classroom.add_student(Student("Ada", "9A"))
        result = classroom.find_by_name("Cy")
        self.assertIsNone(result)

    def test_find_correct_student_among_many(self):
        classroom = Classroom()
        classroom.add_student(Student("A", "X"))
        classroom.add_student(Student("B", "Y"))
        classroom.add_student(Student("C", "Z"))
        self.assertEqual(classroom.find_by_name("B").get_grade(), "Y")

    def test_find_first_match(self):
        classroom = Classroom()
        classroom.add_student(Student("Ada", "9A"))
        classroom.add_student(Student("Ada", "9X"))
        self.assertEqual(classroom.find_by_name("Ada").get_grade(), "9A")

    # --- Hidden ---

    def test_hidden_count_three(self):
        classroom = Classroom()
        classroom.add_student(Student("A", "X"))
        classroom.add_student(Student("B", "Y"))
        classroom.add_student(Student("C", "Z"))
        self.assertEqual(classroom.count_students(), 3)

    def test_hidden_find_among_many(self):
        classroom = Classroom()
        classroom.add_student(Student("Alpha", "1"))
        classroom.add_student(Student("Beta", "2"))
        classroom.add_student(Student("Gamma", "3"))
        self.assertEqual(classroom.find_by_name("Gamma").get_grade(), "3")

    def test_hidden_not_found_among_many(self):
        classroom = Classroom()
        classroom.add_student(Student("Alpha", "1"))
        classroom.add_student(Student("Beta", "2"))
        classroom.add_student(Student("Gamma", "3"))
        self.assertIsNone(classroom.find_by_name("Delta"))

    def test_hidden_independent_classrooms(self):
        classroom1 = Classroom()
        classroom2 = Classroom()
        classroom1.add_student(Student("A", "X"))
        classroom2.add_student(Student("B", "Y"))
        self.assertEqual(classroom1.count_students(), 1)
        self.assertEqual(classroom2.count_students(), 1)
        self.assertIsNone(classroom1.find_by_name("B"))

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

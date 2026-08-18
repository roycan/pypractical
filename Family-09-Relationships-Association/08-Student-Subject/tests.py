"""Unit tests for Student Subject -- Family 09, Assessment 08."""

import unittest

try:
    from solution import Subject, Student
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestStudentSubject(unittest.TestCase):

    # --- enroll updates both sides ---

    def test_enroll_adds_to_student(self):
        student = Student("Ada")
        subject = Subject("MATH101", "Mathematics")
        student.enroll(subject)
        self.assertTrue(student.is_enrolled("MATH101"))

    def test_enroll_adds_to_subject(self):
        student = Student("Ada")
        subject = Subject("MATH101", "Mathematics")
        student.enroll(subject)
        self.assertTrue(subject.has_student("Ada"))

    def test_enroll_two_subjects(self):
        student = Student("Ada")
        math = Subject("MATH101", "Mathematics")
        sci = Subject("SCI101", "Science")
        student.enroll(math)
        student.enroll(sci)
        self.assertEqual(student.list_subjects(), ["Mathematics", "Science"])

    def test_two_students_same_subject(self):
        s1 = Student("Ada")
        s2 = Student("Bo")
        subject = Subject("MATH101", "Mathematics")
        s1.enroll(subject)
        s2.enroll(subject)
        self.assertEqual(subject.count_students(), 2)
        self.assertTrue(subject.has_student("Ada"))
        self.assertTrue(subject.has_student("Bo"))

    # --- is_enrolled ---

    def test_not_enrolled(self):
        student = Student("Ada")
        self.assertFalse(student.is_enrolled("MATH101"))

    def test_enrolled_true(self):
        student = Student("Ada")
        student.enroll(Subject("MATH101", "Mathematics"))
        self.assertTrue(student.is_enrolled("MATH101"))

    # --- drop updates both sides ---

    def test_drop_removes_from_student(self):
        student = Student("Ada")
        subject = Subject("MATH101", "Mathematics")
        student.enroll(subject)
        self.assertTrue(student.drop("MATH101"))
        self.assertFalse(student.is_enrolled("MATH101"))

    def test_drop_removes_from_subject(self):
        student = Student("Ada")
        subject = Subject("MATH101", "Mathematics")
        student.enroll(subject)
        student.drop("MATH101")
        self.assertFalse(subject.has_student("Ada"))
        self.assertEqual(subject.count_students(), 0)

    def test_drop_not_found(self):
        student = Student("Ada")
        self.assertFalse(student.drop("MATH101"))

    # --- hidden ---

    def test_hidden_enroll_three(self):
        student = Student("Cy")
        student.enroll(Subject("A", "Alpha"))
        student.enroll(Subject("B", "Beta"))
        student.enroll(Subject("C", "Gamma"))
        self.assertEqual(student.list_subjects(), ["Alpha", "Beta", "Gamma"])

    def test_hidden_drop_middle(self):
        student = Student("Cy")
        math = Subject("MATH101", "Mathematics")
        sci = Subject("SCI101", "Science")
        art = Subject("ART101", "Art")
        student.enroll(math)
        student.enroll(sci)
        student.enroll(art)
        student.drop("SCI101")
        self.assertEqual(student.list_subjects(), ["Mathematics", "Art"])
        self.assertEqual(sci.count_students(), 0)

    def test_hidden_many_students(self):
        s1 = Student("Ada")
        s2 = Student("Bo")
        s3 = Student("Cy")
        subject = Subject("MATH101", "Mathematics")
        s1.enroll(subject)
        s2.enroll(subject)
        s3.enroll(subject)
        self.assertEqual(subject.count_students(), 3)

    def test_hidden_subject_getters(self):
        subject = Subject("SCI101", "Science")
        self.assertEqual(subject.get_code(), "SCI101")
        self.assertEqual(subject.get_title(), "Science")

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()
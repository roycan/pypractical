"""Classroom -- Family 09, Assessment 02 (teacher solution)."""


# Provided class. Do NOT modify it.
class Student:
    """Represents one student in a classroom."""

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_name(self):
        """Return the student's name."""
        return self.name

    def get_grade(self):
        """Return the student's grade."""
        return self.grade


class Classroom:
    """Represents a classroom that holds many students."""

    def __init__(self):
        """Initialize a classroom with an empty list of students."""
        self.students = []

    def add_student(self, student):
        """Add one student to the classroom."""
        self.students.append(student)

    def count_students(self):
        """Return the number of students in the classroom."""
        return len(self.students)

    def find_by_name(self, name):
        """Return the first student with the given name, or None."""
        for student in self.students:
            if student.get_name() == name:
                return student
        return None


if __name__ == "__main__":
    classroom = Classroom()
    classroom.add_student(Student("Ada", "9A"))
    classroom.add_student(Student("Bo", "9B"))
    print(classroom.count_students())

    found = classroom.find_by_name("Ada")
    print(found.get_grade())

    missing = classroom.find_by_name("Cy")
    print(missing)

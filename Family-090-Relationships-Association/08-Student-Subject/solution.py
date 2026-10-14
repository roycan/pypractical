"""Student Subject -- Family 09, Assessment 08 (teacher solution)."""


# Provided class. Do NOT modify it.
class Subject:
    """Represents one school subject."""

    def __init__(self, code, title):
        self.code = code
        self.title = title
        self.students = []

    def get_code(self):
        """Return the subject's code."""
        return self.code

    def get_title(self):
        """Return the subject's title."""
        return self.title

    def add_student(self, name):
        """Add a student's name to the subject's enrollment list."""
        self.students.append(name)

    def remove_student(self, name):
        """Remove a student's name from the subject's enrollment list."""
        if name in self.students:
            self.students.remove(name)

    def count_students(self):
        """Return the number of enrolled students."""
        return len(self.students)

    def has_student(self, name):
        """Return True if the student is enrolled."""
        return name in self.students


class Student:
    """Represents a student who enrolls in subjects."""

    def __init__(self, name):
        """Initialize a student with no subjects."""
        self.name = name
        self.subjects = []

    def enroll(self, subject):
        """Enroll in a subject, updating both sides."""
        self.subjects.append(subject)
        subject.add_student(self.name)

    def drop(self, subject_code):
        """Drop a subject by code, updating both sides."""
        for subject in self.subjects:
            if subject.get_code() == subject_code:
                self.subjects.remove(subject)
                subject.remove_student(self.name)
                return True
        return False

    def is_enrolled(self, subject_code):
        """Return True if enrolled in the subject with the given code."""
        for subject in self.subjects:
            if subject.get_code() == subject_code:
                return True
        return False

    def list_subjects(self):
        """Return a list of enrolled subject titles."""
        titles = []
        for subject in self.subjects:
            titles.append(subject.get_title())
        return titles


if __name__ == "__main__":
    math = Subject("MATH101", "Mathematics")
    sci = Subject("SCI101", "Science")
    student = Student("Ada")
    student.enroll(math)
    student.enroll(sci)
    print(student.list_subjects())
    print(math.count_students())
    print(math.has_student("Ada"))
    print(student.drop("MATH101"))
    print(math.count_students())
"""Student Subject -- Family 09, Assessment 08 (starter).

The Subject class is provided and complete. Complete the Student class.
"""


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
        """Initialize a student with no subjects.

        Args:
            name (str): The student's name.
        """

        # TODO: Write your solution here.

        return

    def enroll(self, subject):
        """Enroll in a subject, updating both sides.

        Args:
            subject (Subject): The subject to enroll in.
        """

        # TODO: Write your solution here.

        return

    def drop(self, subject_code):
        """Drop a subject by code, updating both sides.

        Args:
            subject_code (str): The code of the subject to drop.

        Returns:
            bool: True if dropped, False if not enrolled.
        """

        # TODO: Write your solution here.

        return False

    def is_enrolled(self, subject_code):
        """Return True if enrolled in the subject with the given code.

        Args:
            subject_code (str): The subject code to check.

        Returns:
            bool: True if enrolled.
        """

        # TODO: Write your solution here.

        return False

    def list_subjects(self):
        """Return a list of enrolled subject titles.

        Returns:
            list: A list of subject title strings.
        """

        # TODO: Write your solution here.

        return []
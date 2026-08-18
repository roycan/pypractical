"""Student Locker -- Family 09, Assessment 05 (starter).

The Locker class is provided and complete. Complete the Student class.
"""


# Provided class. Do NOT modify it.
class Locker:
    """Represents one school locker."""

    def __init__(self, number, combination):
        self.number = number
        self.combination = combination

    def get_number(self):
        """Return the locker's number."""
        return self.number

    def get_combination(self):
        """Return the locker's combination."""
        return self.combination


class Student:
    """Represents a student who may be assigned one locker."""

    def __init__(self, name):
        """Initialize a student with no locker.

        Args:
            name (str): The student's name.
        """

        # TODO: Write your solution here.

        return

    def assign_locker(self, locker):
        """Assign a locker to the student.

        Args:
            locker (Locker): The locker to assign.
        """

        # TODO: Write your solution here.

        return

    def get_locker_number(self):
        """Return the assigned locker's number, or "No locker".

        Returns:
            int or str: The locker number, or "No locker" if none.
        """

        # TODO: Write your solution here.

        return ""

    def has_locker(self):
        """Return True if the student has a locker.

        Returns:
            bool: True if a locker is assigned.
        """

        # TODO: Write your solution here.

        return False
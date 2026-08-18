"""Student Locker -- Family 09, Assessment 05 (teacher solution)."""


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
        """Initialize a student with no locker."""
        self.name = name
        self.locker = None

    def assign_locker(self, locker):
        """Assign a locker to the student."""
        self.locker = locker

    def get_locker_number(self):
        """Return the assigned locker's number, or "No locker"."""
        if self.locker is None:
            return "No locker"
        return self.locker.get_number()

    def has_locker(self):
        """Return True if the student has a locker."""
        return self.locker is not None


if __name__ == "__main__":
    student = Student("Ada")
    print(student.has_locker())
    print(student.get_locker_number())

    student.assign_locker(Locker(123, "12-24-36"))
    print(student.has_locker())
    print(student.get_locker_number())
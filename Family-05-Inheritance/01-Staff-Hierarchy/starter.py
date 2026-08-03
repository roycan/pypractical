"""Staff Hierarchy -- Family 05, Assessment 01 (starter).

The Employee class is provided and complete. Complete the Manager class.
"""


# Provided class. Do NOT modify it.
class Employee:
    """Represents a basic employee."""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        """Return the employee's name."""
        return self.name

    def get_salary(self):
        """Return the employee's salary."""
        return self.salary


class Manager(Employee):
    """Represents an employee who leads a department."""

    def __init__(self, name, salary, department):
        """Initialize a manager.

        Args:
            name (str): The manager's name.
            salary (int): The manager's salary.
            department (str): The manager's department.
        """

        # TODO: Write your solution here.

        return

    def get_department(self):
        """Return the manager's department.

        Returns:
            str: The manager's department.
        """

        # TODO: Write your solution here.

        return ""

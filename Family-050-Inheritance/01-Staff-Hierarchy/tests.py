"""Unit tests for Staff Hierarchy -- Family 05, Assessment 01."""

import unittest

try:
    from solution import Employee, Manager
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestStaffHierarchy(unittest.TestCase):

    # --- Inherited methods ---

    def test_manager_inherits_get_name(self):
        manager = Manager("Ada", 50000, "Sales")
        self.assertEqual(manager.get_name(), "Ada")

    def test_manager_inherits_get_salary(self):
        manager = Manager("Ada", 50000, "Sales")
        self.assertEqual(manager.get_salary(), 50000)

    # --- Own method ---

    def test_manager_get_department(self):
        manager = Manager("Ada", 50000, "Sales")
        self.assertEqual(manager.get_department(), "Sales")

    # --- Parent still works ---

    def test_employee_get_name(self):
        employee = Employee("Cy", 40000)
        self.assertEqual(employee.get_name(), "Cy")

    def test_employee_get_salary(self):
        employee = Employee("Cy", 40000)
        self.assertEqual(employee.get_salary(), 40000)

    def test_manager_is_an_employee(self):
        manager = Manager("Ada", 50000, "Sales")
        self.assertIsInstance(manager, Employee)

    def test_manager_different_values(self):
        manager = Manager("Bo", 60000, "Engineering")
        self.assertEqual(manager.get_name(), "Bo")
        self.assertEqual(manager.get_salary(), 60000)
        self.assertEqual(manager.get_department(), "Engineering")

    def test_two_managers_independent(self):
        m1 = Manager("Ada", 50000, "Sales")
        m2 = Manager("Bo", 60000, "Engineering")
        self.assertEqual(m1.get_department(), "Sales")
        self.assertEqual(m2.get_department(), "Engineering")

    # --- Hidden ---

    def test_hidden_manager_high_salary(self):
        manager = Manager("Da", 120000, "Finance")
        self.assertEqual(manager.get_salary(), 120000)
        self.assertEqual(manager.get_department(), "Finance")

    def test_hidden_inherited_methods(self):
        manager = Manager("Eve", 45000, "Support")
        self.assertEqual(manager.get_name(), "Eve")
        self.assertEqual(manager.get_salary(), 45000)

    def test_hidden_parent_and_child_coexist(self):
        self.assertEqual(Employee("Cy", 40000).get_salary(), 40000)
        self.assertEqual(Manager("Ada", 50000, "Sales").get_department(), "Sales")

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

# Staff Hierarchy

## Story

Every manager is also an employee. The `Employee` class has already been written
and stores an employee's name and salary.

A manager inherits the employee's name and salary, and adds a department.

## Task

The `Employee` class is provided and complete. Do **not** modify it.

Complete the `Manager` class so a manager inherits `get_name` and `get_salary`
from `Employee` and also stores a `department`.

## Class Specification

### Employee (provided, do not modify)

An `Employee` object represents one basic employee.

Each employee stores:

- the employee's name (`name`)
- the employee's salary (`salary`)

### Manager

A `Manager` object represents one employee who leads a department.

Each manager should remember:

- the inherited employee's name and salary
- a department (`department`)

## Required Methods

### Manager.__init__(name, salary, department)

Call `super().__init__(name, salary)` to reuse the parent, then store the
manager's `department`.

### Manager.get_department()

Return the manager's `department`.

## Constraints

- name is a non-empty string
- salary is a positive integer
- department is a non-empty string

All inputs are valid.

## Example

```python
employee = Employee("Ada", 50000)
print(employee.get_name())
print(employee.get_salary())

manager = Manager("Bo", 60000, "Engineering")
print(manager.get_name())
print(manager.get_salary())
print(manager.get_department())
```

Output

```text
Ada
50000
Bo
60000
Engineering
```

## Explanation

A `Manager` inherits `get_name` and `get_salary` from `Employee`, so
`manager.get_name()` returns `"Bo"` and `manager.get_salary()` returns `60000`
even though `Manager` does not define those methods. `Manager` adds its own
`department`, returned by `get_department`. That is inheritance: the child
reuses the parent and adds something new.

## Hint

In the child `__init__`, call `super().__init__(name, salary)` to reuse the
parent, then set the new attribute with `self.department = department`.

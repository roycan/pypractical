"""Computer Peripherals -- Family 12, Assessment 01 (starter).

The Peripheral class is provided and complete. Complete the Computer class.
"""


# Provided class. Do NOT modify it.
class Peripheral:
    """Represents one peripheral device."""

    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type

    def get_name(self):
        """Return the peripheral's name."""
        return self.name

    def get_type(self):
        """Return the peripheral's type."""
        return self.device_type


class Computer:
    """Represents a computer that holds peripherals."""

    def __init__(self, name):
        """Initialize a computer with no peripherals.

        Args:
            name (str): The computer's name.
        """

        # TODO: Write your solution here.

        return

    def add_peripheral(self, peripheral):
        """Add a peripheral to the computer.

        Args:
            peripheral (Peripheral): The peripheral to add.
        """

        # TODO: Write your solution here.

        return

    def remove_peripheral(self, name):
        """Remove a peripheral by name.

        Args:
            name (str): The name of the peripheral to remove.

        Returns:
            bool: True if removed, False if not found.
        """

        # TODO: Write your solution here.

        return False

    def count_peripherals(self):
        """Return the number of peripherals.

        Returns:
            int: The number of peripherals.
        """

        # TODO: Write your solution here.

        return 0

    def list_peripheral_names(self):
        """Return a list of all peripheral names.

        Returns:
            list: A list of peripheral name strings.
        """

        # TODO: Write your solution here.

        return []

    def has_type(self, device_type):
        """Return True if any peripheral has the given type.

        Args:
            device_type (str): The type to check for.

        Returns:
            bool: True if at least one peripheral has that type.
        """

        # TODO: Write your solution here.

        return False
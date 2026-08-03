"""Rental Cost -- Family 06, Assessment 04 (starter).

The Tool class is provided and complete. Complete the PowerTool class.
"""


# Provided class. Do NOT modify it.
class Tool:
    """Represents a standard tool."""

    def __init__(self, name, days):
        self.name = name
        self.days = days

    def get_name(self):
        """Return the tool's name."""
        return self.name

    def get_days(self):
        """Return the tool's days."""
        return self.days

    def cost(self):
        """Return the rental cost (10 per day)."""
        return self.days * 10


class PowerTool(Tool):
    """Represents a power tool rented at a higher rate."""

    def __init__(self, name, days):
        """Initialize a power tool.

        Args:
            name (str): The tool's name.
            days (int): The tool's days.
        """

        # TODO: Write your solution here.

        return

    def cost(self):
        """Return the power-tool rental cost (15 per day).

        Returns:
            int: The power-tool rental cost.
        """

        # TODO: Write your solution here.

        return 0

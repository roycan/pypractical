"""Rental Cost -- Family 06, Assessment 04 (teacher solution)."""


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
        super().__init__(name, days)

    def cost(self):
        """Return the power-tool rental cost (15 per day).

        Returns:
            int: The power-tool rental cost.
        """
        return self.days * 15


if __name__ == "__main__":
    tool = Tool("Hammer", 3)
    print(tool.get_name())
    print(tool.cost())

    power = PowerTool("Hammer", 3)
    print(power.get_name())
    print(power.cost())

"""Unit tests for Rental Cost -- Family 06, Assessment 04."""

import unittest

from solution import Tool, PowerTool


class TestRentalCost(unittest.TestCase):

    # --- Base method ---

    def test_tool_cost_base(self):
        tool = Tool("Hammer", 3)
        self.assertEqual(tool.cost(), 30)

    def test_tool_get_name(self):
        tool = Tool("Hammer", 3)
        self.assertEqual(tool.get_name(), "Hammer")

    # --- Override ---

    def test_power_tool_overrides_cost(self):
        power = PowerTool("Hammer", 3)
        self.assertEqual(power.cost(), 45)

    def test_same_days_different_cost(self):
        self.assertEqual(Tool("Saw", 6).cost(), 60)
        self.assertEqual(PowerTool("Saw", 6).cost(), 90)

    def test_power_tool_larger_days(self):
        power = PowerTool("Drill", 10)
        self.assertEqual(power.cost(), 150)

    # --- Inherited methods ---

    def test_power_tool_inherits_get_name(self):
        power = PowerTool("Hammer", 3)
        self.assertEqual(power.get_name(), "Hammer")

    def test_power_tool_inherits_get_days(self):
        power = PowerTool("Hammer", 3)
        self.assertEqual(power.get_days(), 3)

    # --- Hidden ---

    def test_hidden_tool_base(self):
        self.assertEqual(Tool("Wrench", 2).cost(), 20)

    def test_hidden_power_tool_override(self):
        self.assertEqual(PowerTool("Sander", 8).cost(), 120)

    def test_hidden_inherited_getters(self):
        power = PowerTool("Hammer", 3)
        self.assertEqual(power.get_name(), "Hammer")
        self.assertEqual(power.get_days(), 3)

    def test_hidden_parent_and_child_coexist(self):
        self.assertEqual(Tool("Hammer", 3).cost(), 30)
        self.assertEqual(PowerTool("Hammer", 3).cost(), 45)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

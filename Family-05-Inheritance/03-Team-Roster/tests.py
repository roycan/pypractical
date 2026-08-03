"""Unit tests for Team Roster -- Family 05, Assessment 03."""

import unittest

from solution import Player, Captain


class TestTeamRoster(unittest.TestCase):

    # --- Inherited methods ---

    def test_captain_inherits_get_name(self):
        captain = Captain("Bo", 10, "Tigers")
        self.assertEqual(captain.get_name(), "Bo")

    def test_captain_inherits_get_number(self):
        captain = Captain("Bo", 10, "Tigers")
        self.assertEqual(captain.get_number(), 10)

    # --- Own method ---

    def test_captain_get_team(self):
        captain = Captain("Bo", 10, "Tigers")
        self.assertEqual(captain.get_team(), "Tigers")

    # --- Parent still works ---

    def test_player_get_name(self):
        player = Player("Ada", 9)
        self.assertEqual(player.get_name(), "Ada")

    def test_player_get_number(self):
        player = Player("Ada", 9)
        self.assertEqual(player.get_number(), 9)

    def test_captain_is_a_player(self):
        captain = Captain("Bo", 10, "Tigers")
        self.assertIsInstance(captain, Player)

    def test_captain_different_values(self):
        captain = Captain("Cy", 7, "Eagles")
        self.assertEqual(captain.get_name(), "Cy")
        self.assertEqual(captain.get_number(), 7)
        self.assertEqual(captain.get_team(), "Eagles")

    def test_two_captains_independent(self):
        c1 = Captain("Bo", 10, "Tigers")
        c2 = Captain("Cy", 7, "Eagles")
        self.assertEqual(c1.get_team(), "Tigers")
        self.assertEqual(c2.get_team(), "Eagles")

    # --- Hidden ---

    def test_hidden_captain_high_number(self):
        captain = Captain("Dee", 11, "Lions")
        self.assertEqual(captain.get_number(), 11)
        self.assertEqual(captain.get_team(), "Lions")

    def test_hidden_inherited_methods(self):
        captain = Captain("Finn", 8, "Hawks")
        self.assertEqual(captain.get_name(), "Finn")
        self.assertEqual(captain.get_number(), 8)

    def test_hidden_parent_and_child_coexist(self):
        self.assertEqual(Player("Ada", 9).get_number(), 9)
        self.assertEqual(Captain("Bo", 10, "Tigers").get_team(), "Tigers")

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

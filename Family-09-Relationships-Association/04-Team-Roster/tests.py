"""Unit tests for Team Roster -- Family 09, Assessment 04."""

import unittest

from solution import Player, Team


class TestTeam(unittest.TestCase):

    # --- count ---

    def test_empty_team_count(self):
        team = Team()
        self.assertEqual(team.count_players(), 0)

    def test_add_one_player(self):
        team = Team()
        team.add_player(Player("Ada", "Guard"))
        self.assertEqual(team.count_players(), 1)

    def test_add_two_players(self):
        team = Team()
        team.add_player(Player("Ada", "Guard"))
        team.add_player(Player("Bo", "Forward"))
        self.assertEqual(team.count_players(), 2)

    # --- find_by_name ---

    def test_find_returns_player(self):
        team = Team()
        team.add_player(Player("Ada", "Guard"))
        self.assertEqual(team.find_by_name("Ada").get_position(), "Guard")

    def test_find_not_found_returns_none(self):
        team = Team()
        team.add_player(Player("Ada", "Guard"))
        result = team.find_by_name("Cy")
        self.assertIsNone(result)

    def test_find_correct_player_among_many(self):
        team = Team()
        team.add_player(Player("A", "X"))
        team.add_player(Player("B", "Y"))
        team.add_player(Player("C", "Z"))
        self.assertEqual(team.find_by_name("B").get_position(), "Y")

    def test_find_first_match(self):
        team = Team()
        team.add_player(Player("Ada", "Guard"))
        team.add_player(Player("Ada", "Backup"))
        self.assertEqual(team.find_by_name("Ada").get_position(), "Guard")

    # --- Hidden ---

    def test_hidden_count_three(self):
        team = Team()
        team.add_player(Player("A", "X"))
        team.add_player(Player("B", "Y"))
        team.add_player(Player("C", "Z"))
        self.assertEqual(team.count_players(), 3)

    def test_hidden_find_among_many(self):
        team = Team()
        team.add_player(Player("Alpha", "1"))
        team.add_player(Player("Beta", "2"))
        team.add_player(Player("Gamma", "3"))
        self.assertEqual(team.find_by_name("Gamma").get_position(), "3")

    def test_hidden_not_found_among_many(self):
        team = Team()
        team.add_player(Player("Alpha", "1"))
        team.add_player(Player("Beta", "2"))
        team.add_player(Player("Gamma", "3"))
        self.assertIsNone(team.find_by_name("Delta"))

    def test_hidden_independent_teams(self):
        team1 = Team()
        team2 = Team()
        team1.add_player(Player("A", "X"))
        team2.add_player(Player("B", "Y"))
        self.assertEqual(team1.count_players(), 1)
        self.assertEqual(team2.count_players(), 1)
        self.assertIsNone(team1.find_by_name("B"))

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

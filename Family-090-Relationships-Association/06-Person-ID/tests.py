"""Unit tests for Person ID -- Family 09, Assessment 06."""

import unittest

try:
    from solution import IDCard, Person
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestPersonID(unittest.TestCase):

    # --- no card ---

    def test_no_card_by_default(self):
        person = Person("Ada")
        self.assertIsNone(person.get_id_card())

    def test_no_id_number(self):
        person = Person("Ada")
        self.assertEqual(person.get_id_number(), "No ID")

    # --- set card ---

    def test_set_id_card(self):
        person = Person("Ada")
        card = IDCard("A-1001")
        person.set_id_card(card)
        self.assertEqual(person.get_id_card(), card)

    def test_id_number_after_set(self):
        person = Person("Ada")
        person.set_id_card(IDCard("A-1001"))
        self.assertEqual(person.get_id_number(), "A-1001")

    # --- replace card ---

    def test_replace_card(self):
        person = Person("Ada")
        person.set_id_card(IDCard("A-1001"))
        person.set_id_card(IDCard("B-2002"))
        self.assertEqual(person.get_id_number(), "B-2002")

    # --- hidden ---

    def test_hidden_different_card(self):
        person = Person("Bo")
        person.set_id_card(IDCard("C-3003"))
        self.assertEqual(person.get_id_number(), "C-3003")

    def test_hidden_two_people_independent(self):
        p1 = Person("Ada")
        p2 = Person("Bo")
        p1.set_id_card(IDCard("A-1001"))
        self.assertEqual(p1.get_id_number(), "A-1001")
        self.assertEqual(p2.get_id_number(), "No ID")

    def test_hidden_id_card_get_number(self):
        card = IDCard("D-4004")
        self.assertEqual(card.get_number(), "D-4004")

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()
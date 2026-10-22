"""Unit tests for Sports Captain -- Family 055, Assessment 04."""

import contextlib
import io
import unittest

try:
    from solution import Captain, Member
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


def _construction_output(cls, *args):
    """Construct cls(*args) while capturing stdout.

    Capturing only what is printed DURING the call keeps demo output from
    polluting the validation checks.

    Args:
        cls (type): The class to instantiate.
        *args: The constructor arguments.

    Returns:
        tuple: The text printed during construction and the new object.
    """
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        obj = cls(*args)
    return buffer.getvalue().strip(), obj


def _assignment_output(obj, attr, value):
    """Assign obj.attr = value while capturing stdout.

    Capturing only what is printed DURING the assignment keeps demo output from
    polluting the validation checks.

    Args:
        obj: The object to update.
        attr (str): The attribute name to assign.
        value: The value to assign.

    Returns:
        str: The text printed during the assignment.
    """
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        setattr(obj, attr, value)
    return buffer.getvalue().strip()


class TestSportsCaptain(unittest.TestCase):

    # --- Inheritance ---

    def test_captain_is_subclass_of_member(self):
        self.assertTrue(issubclass(Captain, Member))

    def test_captain_instance_is_a_member(self):
        captain = Captain("Ben", "Football", 3)
        self.assertIsInstance(captain, Captain)
        self.assertIsInstance(captain, Member)

    def test_captain_inherits_name_via_super(self):
        captain = Captain("Ben", "Football", 3)
        self.assertEqual(captain.name, "Ben")

    def test_captain_inherits_club_via_super(self):
        captain = Captain("Ben", "Football", 3)
        self.assertEqual(captain.club, "Football")

    def test_captain_uses_inherited_display_info(self):
        captain = Captain("Ben", "Football", 3)
        result = captain.display_info()
        self.assertIsInstance(result, str)
        self.assertIn("Ben", result)
        self.assertIn("Football", result)

    # --- Encapsulation ---

    def test_value_stored_in_protected_attribute(self):
        captain = Captain("Ben", "Football", 3)
        self.assertTrue(hasattr(captain, "_trophies_won"))
        self.assertEqual(captain.trophies_won, 3)

    def test_zero_trophies_prints_warning(self):
        out, _ = _construction_output(Captain, "Cal", "Basketball", 0)
        self.assertIn("positive", out.lower())

    def test_negative_trophies_prints_warning(self):
        out, _ = _construction_output(Captain, "Cal", "Basketball", -1)
        self.assertIn("positive", out.lower())

    def test_invalid_trophies_stored_as_zero_fallback(self):
        _, captain = _construction_output(Captain, "Cal", "Basketball", -1)
        self.assertEqual(captain.trophies_won, 0)

    def test_valid_captain_prints_no_warning(self):
        out, _ = _construction_output(Captain, "Ben", "Football", 3)
        self.assertNotIn("positive", out.lower())

    def test_post_construction_update_validates(self):
        captain = Captain("Ben", "Football", 3)
        out = _assignment_output(captain, "trophies_won", -1)
        self.assertIn("positive", out.lower())
        self.assertEqual(captain.trophies_won, 0)

    # --- Integration ---

    def test_two_captains_are_independent(self):
        first = Captain("Ben", "Football", 3)
        second = Captain("Dee", "Volleyball", 5)
        self.assertEqual(first.trophies_won, 3)
        self.assertEqual(second.trophies_won, 5)

    # --- Hidden ---

    def test_hidden_member_works_standalone(self):
        member = Member("Ana", "Chess")
        self.assertEqual(member.name, "Ana")
        self.assertEqual(member.club, "Chess")
        self.assertIn("Ana", member.display_info())

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

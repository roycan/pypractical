"""Unit tests for Video Game Edition -- Family 055, Assessment 02."""

import contextlib
import io
import unittest

try:
    from solution import DeluxeEdition, Game
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


class TestVideoGameEdition(unittest.TestCase):

    # --- Inheritance ---

    def test_deluxe_edition_is_subclass_of_game(self):
        self.assertTrue(issubclass(DeluxeEdition, Game))

    def test_deluxe_edition_instance_is_a_game(self):
        deluxe = DeluxeEdition("Elden Ring", "RPG", 40)
        self.assertIsInstance(deluxe, DeluxeEdition)
        self.assertIsInstance(deluxe, Game)

    def test_deluxe_edition_inherits_title_via_super(self):
        deluxe = DeluxeEdition("Elden Ring", "RPG", 40)
        self.assertEqual(deluxe.title, "Elden Ring")

    def test_deluxe_edition_inherits_genre_via_super(self):
        deluxe = DeluxeEdition("Elden Ring", "RPG", 40)
        self.assertEqual(deluxe.genre, "RPG")

    def test_deluxe_edition_uses_inherited_display_info(self):
        deluxe = DeluxeEdition("Elden Ring", "RPG", 40)
        result = deluxe.display_info()
        self.assertIsInstance(result, str)
        self.assertIn("Elden Ring", result)
        self.assertIn("RPG", result)

    # --- Encapsulation ---

    def test_value_stored_in_protected_attribute(self):
        deluxe = DeluxeEdition("Elden Ring", "RPG", 40)
        self.assertTrue(hasattr(deluxe, "_bonus_levels"))
        self.assertEqual(deluxe.bonus_levels, 40)

    def test_zero_bonus_levels_prints_warning(self):
        out, _ = _construction_output(DeluxeEdition, "Empty", "Puzzle", 0)
        self.assertIn("positive", out.lower())

    def test_negative_bonus_levels_prints_warning(self):
        out, _ = _construction_output(DeluxeEdition, "Mystery Quest", "Puzzle", -2)
        self.assertIn("positive", out.lower())

    def test_invalid_bonus_levels_stored_as_zero_fallback(self):
        _, deluxe = _construction_output(DeluxeEdition, "Mystery Quest", "Puzzle", -2)
        self.assertEqual(deluxe.bonus_levels, 0)

    def test_valid_deluxe_edition_prints_no_warning(self):
        out, _ = _construction_output(DeluxeEdition, "Elden Ring", "RPG", 40)
        self.assertNotIn("positive", out.lower())

    def test_post_construction_update_validates(self):
        deluxe = DeluxeEdition("Elden Ring", "RPG", 40)
        out = _assignment_output(deluxe, "bonus_levels", -2)
        self.assertIn("positive", out.lower())
        self.assertEqual(deluxe.bonus_levels, 0)

    # --- Integration ---

    def test_two_deluxe_editions_are_independent(self):
        first = DeluxeEdition("Elden Ring", "RPG", 40)
        second = DeluxeEdition("Mario Kart", "Racing", 8)
        self.assertEqual(first.bonus_levels, 40)
        self.assertEqual(second.bonus_levels, 8)

    # --- Hidden ---

    def test_hidden_game_works_standalone(self):
        game = Game("Chess", "Board")
        self.assertEqual(game.title, "Chess")
        self.assertEqual(game.genre, "Board")
        self.assertIn("Chess", game.display_info())

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

"""Unit tests for Race Car -- Family 055, Assessment 05."""

import contextlib
import io
import unittest

try:
    from solution import Racer, Vehicle
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


class TestRaceCar(unittest.TestCase):

    # --- Inheritance ---

    def test_racer_is_subclass_of_vehicle(self):
        self.assertTrue(issubclass(Racer, Vehicle))

    def test_racer_instance_is_a_vehicle(self):
        racer = Racer("Bolt", 200, 190)
        self.assertIsInstance(racer, Racer)
        self.assertIsInstance(racer, Vehicle)

    def test_racer_inherits_name_via_super(self):
        racer = Racer("Bolt", 200, 190)
        self.assertEqual(racer.name, "Bolt")

    def test_racer_inherits_max_speed_via_super(self):
        racer = Racer("Bolt", 200, 190)
        self.assertEqual(racer.max_speed, 200)

    def test_racer_uses_inherited_display_info(self):
        racer = Racer("Bolt", 200, 190)
        result = racer.display_info()
        self.assertIsInstance(result, str)
        self.assertIn("Bolt", result)
        self.assertIn("200", result)

    # --- Encapsulation ---

    def test_value_stored_in_protected_attribute(self):
        racer = Racer("Bolt", 200, 190)
        self.assertTrue(hasattr(racer, "_top_speed"))
        self.assertEqual(racer.get_top_speed(), 190)

    def test_top_speed_equal_to_max_is_valid(self):
        out, racer = _construction_output(Racer, "Bolt", 200, 200)
        self.assertNotIn("exceed", out.lower())
        self.assertNotIn("cannot", out.lower())
        self.assertEqual(racer.get_top_speed(), 200)

    def test_top_speed_exceeding_max_prints_warning(self):
        out, _ = _construction_output(Racer, "Dash", 150, 170)
        self.assertIn("exceed", out.lower())

    def test_exceeding_top_speed_falls_back_to_max(self):
        _, racer = _construction_output(Racer, "Dash", 150, 170)
        self.assertEqual(racer.get_top_speed(), 150)
        self.assertEqual(racer.get_top_speed(), racer.max_speed)

    def test_valid_top_speed_prints_no_warning(self):
        out, _ = _construction_output(Racer, "Bolt", 200, 190)
        self.assertNotIn("exceed", out.lower())

    # --- Integration ---

    def test_two_racers_are_independent(self):
        first = Racer("Bolt", 200, 190)
        second = Racer("Dash", 150, 140)
        self.assertEqual(first.get_top_speed(), 190)
        self.assertEqual(second.get_top_speed(), 140)

    # --- Hidden ---

    def test_hidden_vehicle_works_standalone(self):
        vehicle = Vehicle("Sedan", 180)
        self.assertEqual(vehicle.name, "Sedan")
        self.assertEqual(vehicle.max_speed, 180)
        self.assertIn("Sedan", vehicle.display_info())

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

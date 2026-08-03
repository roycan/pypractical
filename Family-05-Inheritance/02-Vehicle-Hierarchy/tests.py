"""Unit tests for Vehicle Hierarchy -- Family 05, Assessment 02."""

import unittest

try:
    from solution import Vehicle, Motorcycle
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestVehicleHierarchy(unittest.TestCase):

    # --- Inherited methods ---

    def test_motorcycle_inherits_get_brand(self):
        motorcycle = Motorcycle("Yamaha", 2022, "V-Twin")
        self.assertEqual(motorcycle.get_brand(), "Yamaha")

    def test_motorcycle_inherits_get_year(self):
        motorcycle = Motorcycle("Yamaha", 2022, "V-Twin")
        self.assertEqual(motorcycle.get_year(), 2022)

    # --- Own method ---

    def test_motorcycle_get_engine_type(self):
        motorcycle = Motorcycle("Yamaha", 2022, "V-Twin")
        self.assertEqual(motorcycle.get_engine_type(), "V-Twin")

    # --- Parent still works ---

    def test_vehicle_get_brand(self):
        vehicle = Vehicle("Honda", 2020)
        self.assertEqual(vehicle.get_brand(), "Honda")

    def test_vehicle_get_year(self):
        vehicle = Vehicle("Honda", 2020)
        self.assertEqual(vehicle.get_year(), 2020)

    def test_motorcycle_is_a_vehicle(self):
        motorcycle = Motorcycle("Yamaha", 2022, "V-Twin")
        self.assertIsInstance(motorcycle, Vehicle)

    def test_motorcycle_different_values(self):
        motorcycle = Motorcycle("Honda", 2021, "Inline-4")
        self.assertEqual(motorcycle.get_brand(), "Honda")
        self.assertEqual(motorcycle.get_year(), 2021)
        self.assertEqual(motorcycle.get_engine_type(), "Inline-4")

    def test_two_motorcycles_independent(self):
        m1 = Motorcycle("Yamaha", 2022, "V-Twin")
        m2 = Motorcycle("Honda", 2021, "Inline-4")
        self.assertEqual(m1.get_engine_type(), "V-Twin")
        self.assertEqual(m2.get_engine_type(), "Inline-4")

    # --- Hidden ---

    def test_hidden_motorcycle_high_year(self):
        motorcycle = Motorcycle("Ducati", 2023, "V4")
        self.assertEqual(motorcycle.get_year(), 2023)
        self.assertEqual(motorcycle.get_engine_type(), "V4")

    def test_hidden_inherited_methods(self):
        motorcycle = Motorcycle("Triumph", 2019, "Inline-3")
        self.assertEqual(motorcycle.get_brand(), "Triumph")
        self.assertEqual(motorcycle.get_year(), 2019)

    def test_hidden_parent_and_child_coexist(self):
        self.assertEqual(Vehicle("Honda", 2020).get_year(), 2020)
        self.assertEqual(
            Motorcycle("Yamaha", 2022, "V-Twin").get_engine_type(), "V-Twin"
        )

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

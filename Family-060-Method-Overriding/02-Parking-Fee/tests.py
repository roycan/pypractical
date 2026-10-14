"""Unit tests for Parking Fee -- Family 06, Assessment 02."""

import unittest

try:
    from solution import Vehicle, Truck
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestParkingFee(unittest.TestCase):

    # --- Base method ---

    def test_vehicle_fee_base(self):
        vehicle = Vehicle("Sedan", 4)
        self.assertEqual(vehicle.fee(), 20)

    def test_vehicle_get_name(self):
        vehicle = Vehicle("Sedan", 4)
        self.assertEqual(vehicle.get_name(), "Sedan")

    # --- Override ---

    def test_truck_overrides_fee(self):
        truck = Truck("Lorry", 4)
        self.assertEqual(truck.fee(), 32)

    def test_same_hours_different_fee(self):
        self.assertEqual(Vehicle("Bus", 10).fee(), 50)
        self.assertEqual(Truck("Bus", 10).fee(), 80)

    def test_truck_larger_hours(self):
        truck = Truck("Rig", 20)
        self.assertEqual(truck.fee(), 160)

    # --- Inherited methods ---

    def test_truck_inherits_get_name(self):
        truck = Truck("Lorry", 4)
        self.assertEqual(truck.get_name(), "Lorry")

    def test_truck_inherits_get_hours(self):
        truck = Truck("Lorry", 4)
        self.assertEqual(truck.get_hours(), 4)

    # --- Hidden ---

    def test_hidden_vehicle_base(self):
        self.assertEqual(Vehicle("Bike", 2).fee(), 10)

    def test_hidden_truck_override(self):
        self.assertEqual(Truck("Van", 9).fee(), 72)

    def test_hidden_inherited_getters(self):
        truck = Truck("Lorry", 4)
        self.assertEqual(truck.get_name(), "Lorry")
        self.assertEqual(truck.get_hours(), 4)

    def test_hidden_parent_and_child_coexist(self):
        self.assertEqual(Vehicle("Sedan", 4).fee(), 20)
        self.assertEqual(Truck("Lorry", 4).fee(), 32)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

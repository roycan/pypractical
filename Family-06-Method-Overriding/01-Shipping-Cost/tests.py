"""Unit tests for Shipping Cost -- Family 06, Assessment 01."""

import unittest

try:
    from solution import Parcel, ExpressParcel
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestShippingCost(unittest.TestCase):

    # --- Base method ---

    def test_parcel_shipping_base(self):
        parcel = Parcel("Box", 6)
        self.assertEqual(parcel.shipping(), 30)

    def test_parcel_get_name(self):
        parcel = Parcel("Box", 6)
        self.assertEqual(parcel.get_name(), "Box")

    # --- Override ---

    def test_express_overrides_shipping(self):
        express = ExpressParcel("Box", 6)
        self.assertEqual(express.shipping(), 60)

    def test_same_weight_different_shipping(self):
        self.assertEqual(Parcel("Crate", 10).shipping(), 50)
        self.assertEqual(ExpressParcel("Crate", 10).shipping(), 100)

    def test_express_larger_weight(self):
        express = ExpressParcel("Barrel", 20)
        self.assertEqual(express.shipping(), 200)

    # --- Inherited methods ---

    def test_express_inherits_get_name(self):
        express = ExpressParcel("Box", 6)
        self.assertEqual(express.get_name(), "Box")

    def test_express_inherits_get_weight(self):
        express = ExpressParcel("Box", 6)
        self.assertEqual(express.get_weight(), 6)

    # --- Hidden ---

    def test_hidden_parcel_base(self):
        self.assertEqual(Parcel("Pouch", 4).shipping(), 20)

    def test_hidden_express_override(self):
        self.assertEqual(ExpressParcel("Crate", 9).shipping(), 90)

    def test_hidden_inherited_getters(self):
        express = ExpressParcel("Box", 6)
        self.assertEqual(express.get_name(), "Box")
        self.assertEqual(express.get_weight(), 6)

    def test_hidden_parent_and_child_coexist(self):
        self.assertEqual(Parcel("Box", 6).shipping(), 30)
        self.assertEqual(ExpressParcel("Box", 6).shipping(), 60)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

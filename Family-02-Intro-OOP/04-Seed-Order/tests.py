"""Unit tests for Seed Order -- Family 02, Assessment 04."""

import unittest

from solution import SeedPacket


class TestSeedOrder(unittest.TestCase):

    # --- SeedPacket attributes ---

    def test_variety_stored(self):
        packet = SeedPacket("Basil", 25, 6)
        self.assertEqual(packet.variety, "Basil")

    def test_price_stored(self):
        packet = SeedPacket("Basil", 25, 6)
        self.assertEqual(packet.price, 25)

    def test_packets_stored(self):
        packet = SeedPacket("Basil", 25, 6)
        self.assertEqual(packet.packets, 6)

    # --- order_total (basic) ---

    def test_order_total_basic(self):
        packet = SeedPacket("Basil", 25, 6)
        self.assertEqual(packet.order_total(), 150)

    def test_order_total_single_packet(self):
        packet = SeedPacket("Parsley", 25, 1)
        self.assertEqual(packet.order_total(), 25)

    # --- Boundary ---

    def test_order_total_zero_packets(self):
        packet = SeedPacket("Sample", 15, 0)
        self.assertEqual(packet.order_total(), 0)

    # --- Typical ---

    def test_order_total_typical(self):
        packet = SeedPacket("Mint", 40, 7)
        self.assertEqual(packet.order_total(), 280)

    # --- Objects are independent ---

    def test_two_seed_packets_independent(self):
        first = SeedPacket("Basil", 25, 6)
        second = SeedPacket("Chive", 18, 4)
        self.assertEqual(first.order_total(), 150)
        self.assertEqual(second.order_total(), 72)

    def test_changing_one_does_not_affect_other(self):
        first = SeedPacket("Basil", 25, 6)
        second = SeedPacket("Chive", 18, 4)
        first.packets = 10
        self.assertEqual(first.order_total(), 250)
        self.assertEqual(second.order_total(), 72)

    # --- Hidden ---

    def test_hidden_large_values(self):
        packet = SeedPacket("Oak", 90, 50)
        self.assertEqual(packet.order_total(), 4500)

    def test_hidden_small_values(self):
        packet = SeedPacket("Cress", 3, 5)
        self.assertEqual(packet.order_total(), 15)

    def test_hidden_mixed(self):
        packet = SeedPacket("Tomato", 35, 12)
        self.assertEqual(packet.order_total(), 420)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

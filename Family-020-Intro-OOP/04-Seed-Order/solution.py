"""Seed Order -- Family 02, Assessment 04 (teacher solution)."""


class SeedPacket:
    """Represents one kind of seed packet in the store."""

    def __init__(self, variety, price, packets):
        """Initialize a seed packet.

        Args:
            variety (str): Seed packet variety name.
            price (int): Price for one packet.
            packets (int): Number of packets in the order.
        """
        self.variety = variety
        self.price = price
        self.packets = packets

    def order_total(self):
        """Return the order total for this seed packet.

        Returns:
            int: price multiplied by packets.
        """
        return self.price * self.packets


if __name__ == "__main__":
    packet = SeedPacket("Basil", 25, 6)
    print(packet.variety)
    print(packet.price)
    print(packet.packets)
    print(packet.order_total())

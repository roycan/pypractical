"""Storage Crate -- Family 10, Assessment 02 (teacher solution)."""


# Provided class. Do NOT modify it.
class Box:
    """Represents one box."""

    def __init__(self, size):
        self.size = size

    def get_size(self):
        """Return the box's size."""
        return self.size


class Crate:
    """Represents a crate that creates and owns its boxes."""

    def __init__(self, box_count, size):
        """Create the boxes that belong to this crate.

        Args:
            box_count (int): How many boxes to create.
            size (int): The size of each box.
        """
        self.boxes = []
        for i in range(box_count):
            self.boxes.append(Box(size))

    def count_boxes(self):
        """Return the number of boxes in the crate."""
        return len(self.boxes)

    def total_size(self):
        """Return the total size of all boxes combined."""
        total = 0
        for box in self.boxes:
            total = total + box.get_size()
        return total


if __name__ == "__main__":
    crate = Crate(3, 100)
    print(crate.count_boxes())
    print(crate.total_size())

"""Computer Peripherals -- Family 12, Assessment 01 (teacher solution)."""


# Provided class. Do NOT modify it.
class Peripheral:
    """Represents one peripheral device."""

    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type

    def get_name(self):
        """Return the peripheral's name."""
        return self.name

    def get_type(self):
        """Return the peripheral's type."""
        return self.device_type


class Computer:
    """Represents a computer that holds peripherals."""

    def __init__(self, name):
        """Initialize a computer with no peripherals."""
        self.name = name
        self.peripherals = []

    def add_peripheral(self, peripheral):
        """Add a peripheral to the computer."""
        self.peripherals.append(peripheral)

    def remove_peripheral(self, name):
        """Remove a peripheral by name."""
        for peripheral in self.peripherals:
            if peripheral.get_name() == name:
                self.peripherals.remove(peripheral)
                return True
        return False

    def count_peripherals(self):
        """Return the number of peripherals."""
        return len(self.peripherals)

    def list_peripheral_names(self):
        """Return a list of all peripheral names."""
        names = []
        for peripheral in self.peripherals:
            names.append(peripheral.get_name())
        return names

    def has_type(self, device_type):
        """Return True if any peripheral has the given type."""
        for peripheral in self.peripherals:
            if peripheral.get_type() == device_type:
                return True
        return False


if __name__ == "__main__":
    computer = Computer("MyPC")
    computer.add_peripheral(Peripheral("Logitech K120", "keyboard"))
    computer.add_peripheral(Peripheral("Razer DeathAdder", "mouse"))
    print(computer.count_peripherals())
    print(computer.list_peripheral_names())
    print(computer.has_type("mouse"))
    print(computer.has_type("monitor"))
    print(computer.remove_peripheral("Logitech K120"))
    print(computer.count_peripherals())
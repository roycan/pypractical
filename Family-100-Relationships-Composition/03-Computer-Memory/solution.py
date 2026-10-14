"""Computer Memory -- Family 10, Assessment 03 (teacher solution)."""


# Provided class. Do NOT modify it.
class Module:
    """Represents one memory module."""

    def __init__(self, size):
        self.size = size

    def get_size(self):
        """Return the module's size."""
        return self.size


class Computer:
    """Represents a computer that creates and owns its memory modules."""

    def __init__(self, module_count, size):
        """Create the memory modules that belong to this computer.

        Args:
            module_count (int): How many modules to create.
            size (int): The size of each module.
        """
        self.modules = []
        for i in range(module_count):
            self.modules.append(Module(size))

    def count_modules(self):
        """Return the number of modules in the computer."""
        return len(self.modules)

    def total_memory(self):
        """Return the total memory of all modules combined."""
        total = 0
        for module in self.modules:
            total = total + module.get_size()
        return total


if __name__ == "__main__":
    computer = Computer(3, 100)
    print(computer.count_modules())
    print(computer.total_memory())

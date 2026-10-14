"""Animal Bird -- Family 05, Assessment 05 (starter).

The Animal class is provided and complete. Complete the Bird class.
"""


# Provided class. Do NOT modify it.
class Animal:
    """Represents a basic animal."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        """Return the animal's name."""
        return self.name

    def get_species(self):
        """Return the animal's species."""
        return self.species


class Bird(Animal):
    """Represents a bird that inherits from Animal."""

    def __init__(self, name, species, wingspan):
        """Initialize a bird.

        Args:
            name (str): The bird's name.
            species (str): The bird's species.
            wingspan (int): The bird's wingspan in centimeters.
        """

        # TODO: Write your solution here.

        return

    def get_wingspan(self):
        """Return the bird's wingspan.

        Returns:
            int: The bird's wingspan in centimeters.
        """

        # TODO: Write your solution here.

        return 0

    def describe(self):
        """Return a description of the bird.

        Returns:
            str: A sentence describing the bird.
        """

        # TODO: Write your solution here.

        return ""
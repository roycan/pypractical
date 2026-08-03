"""Pet Registry -- Family 05, Assessment 04 (starter).

The Animal class is provided and complete. Complete the Pet class.
"""


# Provided class. Do NOT modify it.
class Animal:
    """Represents a basic animal."""

    def __init__(self, species, age):
        self.species = species
        self.age = age

    def get_species(self):
        """Return the animal's species."""
        return self.species

    def get_age(self):
        """Return the animal's age."""
        return self.age


class Pet(Animal):
    """Represents an animal that has an owner."""

    def __init__(self, species, age, owner):
        """Initialize a pet.

        Args:
            species (str): The pet's species.
            age (int): The pet's age.
            owner (str): The pet's owner.
        """

        # TODO: Write your solution here.

        return

    def get_owner(self):
        """Return the pet's owner.

        Returns:
            str: The pet's owner.
        """

        # TODO: Write your solution here.

        return ""

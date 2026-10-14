"""Pet Registry -- Family 05, Assessment 04 (teacher solution)."""


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
        super().__init__(species, age)
        self.owner = owner

    def get_owner(self):
        """Return the pet's owner.

        Returns:
            str: The pet's owner.
        """
        return self.owner


if __name__ == "__main__":
    animal = Animal("Dog", 3)
    print(animal.get_species())
    print(animal.get_age())

    pet = Pet("Cat", 2, "Ada")
    print(pet.get_species())
    print(pet.get_age())
    print(pet.get_owner())

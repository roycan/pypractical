"""Animal Bird -- Family 05, Assessment 05 (teacher solution)."""


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
        """Initialize a bird."""
        super().__init__(name, species)
        self.wingspan = wingspan

    def get_wingspan(self):
        """Return the bird's wingspan."""
        return self.wingspan

    def describe(self):
        """Return a description of the bird."""
        return f"{self.name} is a {self.species} with a {self.wingspan} cm wingspan"


if __name__ == "__main__":
    bird = Bird("Tweety", "canary", 25)
    print(bird.get_name())
    print(bird.get_species())
    print(bird.get_wingspan())
    print(bird.describe())
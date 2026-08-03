"""Unit tests for Pet Registry -- Family 05, Assessment 04."""

import unittest

try:
    from solution import Animal, Pet
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestPetRegistry(unittest.TestCase):

    # --- Inherited methods ---

    def test_pet_inherits_get_species(self):
        pet = Pet("Cat", 2, "Ada")
        self.assertEqual(pet.get_species(), "Cat")

    def test_pet_inherits_get_age(self):
        pet = Pet("Cat", 2, "Ada")
        self.assertEqual(pet.get_age(), 2)

    # --- Own method ---

    def test_pet_get_owner(self):
        pet = Pet("Cat", 2, "Ada")
        self.assertEqual(pet.get_owner(), "Ada")

    # --- Parent still works ---

    def test_animal_get_species(self):
        animal = Animal("Dog", 3)
        self.assertEqual(animal.get_species(), "Dog")

    def test_animal_get_age(self):
        animal = Animal("Dog", 3)
        self.assertEqual(animal.get_age(), 3)

    def test_pet_is_an_animal(self):
        pet = Pet("Cat", 2, "Ada")
        self.assertIsInstance(pet, Animal)

    def test_pet_different_values(self):
        pet = Pet("Rabbit", 1, "Bo")
        self.assertEqual(pet.get_species(), "Rabbit")
        self.assertEqual(pet.get_age(), 1)
        self.assertEqual(pet.get_owner(), "Bo")

    def test_two_pets_independent(self):
        p1 = Pet("Cat", 2, "Ada")
        p2 = Pet("Rabbit", 1, "Bo")
        self.assertEqual(p1.get_owner(), "Ada")
        self.assertEqual(p2.get_owner(), "Bo")

    # --- Hidden ---

    def test_hidden_pet_high_age(self):
        pet = Pet("Parrot", 5, "Cy")
        self.assertEqual(pet.get_age(), 5)
        self.assertEqual(pet.get_owner(), "Cy")

    def test_hidden_inherited_methods(self):
        pet = Pet("Hamster", 1, "Dee")
        self.assertEqual(pet.get_species(), "Hamster")
        self.assertEqual(pet.get_age(), 1)

    def test_hidden_parent_and_child_coexist(self):
        self.assertEqual(Animal("Dog", 3).get_age(), 3)
        self.assertEqual(Pet("Cat", 2, "Ada").get_owner(), "Ada")

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

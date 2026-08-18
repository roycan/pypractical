"""Unit tests for Animal Bird -- Family 05, Assessment 05."""

import unittest

try:
    from solution import Animal, Bird
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestAnimalBird(unittest.TestCase):

    # --- Inherited methods ---

    def test_bird_inherits_get_name(self):
        bird = Bird("Tweety", "canary", 25)
        self.assertEqual(bird.get_name(), "Tweety")

    def test_bird_inherits_get_species(self):
        bird = Bird("Tweety", "canary", 25)
        self.assertEqual(bird.get_species(), "canary")

    # --- Own methods ---

    def test_bird_get_wingspan(self):
        bird = Bird("Tweety", "canary", 25)
        self.assertEqual(bird.get_wingspan(), 25)

    def test_bird_describe(self):
        bird = Bird("Tweety", "canary", 25)
        self.assertEqual(bird.describe(), "Tweety is a canary with a 25 cm wingspan")

    # --- Parent still works ---

    def test_animal_get_name(self):
        animal = Animal("Leo", "lion")
        self.assertEqual(animal.get_name(), "Leo")

    def test_animal_get_species(self):
        animal = Animal("Leo", "lion")
        self.assertEqual(animal.get_species(), "lion")

    def test_bird_is_an_animal(self):
        bird = Bird("Tweety", "canary", 25)
        self.assertIsInstance(bird, Animal)

    # --- Different values ---

    def test_bird_different_values(self):
        bird = Bird("Rio", "macaw", 90)
        self.assertEqual(bird.get_name(), "Rio")
        self.assertEqual(bird.get_species(), "macaw")
        self.assertEqual(bird.get_wingspan(), 90)
        self.assertEqual(bird.describe(), "Rio is a macaw with a 90 cm wingspan")

    def test_two_birds_independent(self):
        b1 = Bird("Tweety", "canary", 25)
        b2 = Bird("Rio", "macaw", 90)
        self.assertEqual(b1.get_wingspan(), 25)
        self.assertEqual(b2.get_wingspan(), 90)

    # --- Hidden ---

    def test_hidden_bird_large_wingspan(self):
        bird = Bird("Albatross", "albatross", 350)
        self.assertEqual(bird.get_wingspan(), 350)
        self.assertEqual(
            bird.describe(), "Albatross is a albatross with a 350 cm wingspan"
        )

    def test_hidden_inherited_methods(self):
        bird = Bird("Hedwig", "owl", 120)
        self.assertEqual(bird.get_name(), "Hedwig")
        self.assertEqual(bird.get_species(), "owl")

    def test_hidden_parent_and_child_coexist(self):
        self.assertEqual(Animal("Leo", "lion").get_species(), "lion")
        self.assertEqual(Bird("Tweety", "canary", 25).get_wingspan(), 25)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()
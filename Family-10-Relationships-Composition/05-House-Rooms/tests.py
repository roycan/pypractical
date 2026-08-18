"""Unit tests for House Rooms -- Family 10, Assessment 05."""

import unittest

try:
    from solution import Room, House
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestHouseRooms(unittest.TestCase):

    # --- count ---

    def test_count_empty(self):
        house = House("Villa", [])
        self.assertEqual(house.count_rooms(), 0)

    def test_count_three(self):
        house = House("Villa", [("Kitchen", 12), ("Bedroom", 20), ("Bath", 6)])
        self.assertEqual(house.count_rooms(), 3)

    # --- total area ---

    def test_total_area(self):
        house = House("Villa", [("Kitchen", 12), ("Bedroom", 20), ("Bath", 6)])
        self.assertEqual(house.total_area(), 38)

    def test_total_area_single(self):
        house = House("Villa", [("Bedroom", 20)])
        self.assertEqual(house.total_area(), 20)

    # --- largest room ---

    def test_largest_room(self):
        house = House("Villa", [("Kitchen", 12), ("Bedroom", 20), ("Bath", 6)])
        self.assertEqual(house.get_largest_room(), "Bedroom")

    def test_largest_room_tie_first(self):
        house = House("Villa", [("Kitchen", 12), ("Study", 12)])
        self.assertEqual(house.get_largest_room(), "Kitchen")

    # --- list names ---

    def test_list_names(self):
        house = House("Villa", [("Kitchen", 12), ("Bedroom", 20)])
        self.assertEqual(house.list_room_names(), ["Kitchen", "Bedroom"])

    def test_list_names_empty(self):
        house = House("Villa", [])
        self.assertEqual(house.list_room_names(), [])

    # --- hidden ---

    def test_hidden_count_four(self):
        house = House(
            "Mansion",
            [("Kitchen", 15), ("Bedroom", 25), ("Bath", 8), ("Garage", 30)],
        )
        self.assertEqual(house.count_rooms(), 4)

    def test_hidden_total_area_four(self):
        house = House(
            "Mansion",
            [("Kitchen", 15), ("Bedroom", 25), ("Bath", 8), ("Garage", 30)],
        )
        self.assertEqual(house.total_area(), 78)

    def test_hidden_largest_among_four(self):
        house = House(
            "Mansion",
            [("Kitchen", 15), ("Bedroom", 25), ("Bath", 8), ("Garage", 30)],
        )
        self.assertEqual(house.get_largest_room(), "Garage")

    def test_hidden_room_getters(self):
        room = Room("Bedroom", 20)
        self.assertEqual(room.get_name(), "Bedroom")
        self.assertEqual(room.get_area(), 20)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()
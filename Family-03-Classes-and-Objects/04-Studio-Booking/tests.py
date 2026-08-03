"""Unit tests for Studio Booking -- Family 03, Assessment 04."""

import unittest

try:
    from solution import Session, Studio, minimum_studios
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestStudioBookingSystem(unittest.TestCase):

    # --- Session ---

    def test_session_start(self):
        session = Session(1, 4, 2)
        self.assertEqual(session.start, 1)

    def test_session_end(self):
        session = Session(1, 4, 2)
        self.assertEqual(session.end, 4)

    def test_session_musicians(self):
        session = Session(1, 4, 2)
        self.assertEqual(session.musicians, 2)

    # --- Studio ---

    def test_studio_initial_time(self):
        studio = Studio()
        self.assertEqual(studio.available_at, 0)

    def test_studio_initial_sessions(self):
        studio = Studio()
        self.assertEqual(len(studio.sessions), 0)

    def test_can_book_true(self):
        studio = Studio()
        session = Session(5, 8, 1)
        self.assertTrue(studio.can_book(session))

    def test_can_book_false(self):
        studio = Studio()
        studio.available_at = 6
        session = Session(5, 9, 1)
        self.assertFalse(studio.can_book(session))

    def test_book_updates_time(self):
        studio = Studio()
        session = Session(3, 10, 2)
        studio.book(session)
        self.assertEqual(studio.available_at, 10)

    def test_book_adds_session(self):
        studio = Studio()
        session = Session(3, 10, 2)
        studio.book(session)
        self.assertEqual(len(studio.sessions), 1)
        self.assertIs(studio.sessions[0], session)

    # --- Scheduler (integration) ---

    def test_scheduler_simple(self):
        data = [(1, 5, 1), (5, 8, 2)]
        self.assertEqual(minimum_studios(data), 1)

    # --- Hidden ---

    def test_scheduler_overlap(self):
        data = [(1, 5, 1), (2, 6, 2)]
        self.assertEqual(minimum_studios(data), 2)

    def test_scheduler_many(self):
        data = [(1, 4, 1), (2, 5, 2), (3, 6, 3), (6, 8, 1)]
        self.assertEqual(minimum_studios(data), 3)

    def test_scheduler_non_overlapping(self):
        data = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 5, 1)]
        self.assertEqual(minimum_studios(data), 1)

    def test_scheduler_complex(self):
        data = [(1, 7, 2), (3, 5, 3), (5, 9, 1), (8, 10, 2), (10, 12, 3)]
        self.assertEqual(minimum_studios(data), 2)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

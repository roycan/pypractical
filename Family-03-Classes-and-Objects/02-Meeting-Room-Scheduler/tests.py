"""Unit tests for Meeting Room Scheduler -- Family 03, Assessment 02."""

import unittest

from solution import Meeting, Room, minimum_rooms


class TestMeetingRoomSystem(unittest.TestCase):

    # --- Meeting ---

    def test_meeting_start(self):
        meeting = Meeting(1, 4, 2)
        self.assertEqual(meeting.start, 1)

    def test_meeting_end(self):
        meeting = Meeting(1, 4, 2)
        self.assertEqual(meeting.end, 4)

    def test_meeting_attendees(self):
        meeting = Meeting(1, 4, 2)
        self.assertEqual(meeting.attendees, 2)

    # --- Room ---

    def test_room_initial_time(self):
        room = Room()
        self.assertEqual(room.available_at, 0)

    def test_room_initial_meetings(self):
        room = Room()
        self.assertEqual(len(room.meetings), 0)

    def test_can_host_true(self):
        room = Room()
        meeting = Meeting(5, 8, 1)
        self.assertTrue(room.can_host(meeting))

    def test_can_host_false(self):
        room = Room()
        room.available_at = 6
        meeting = Meeting(5, 9, 1)
        self.assertFalse(room.can_host(meeting))

    def test_host_updates_time(self):
        room = Room()
        meeting = Meeting(3, 10, 2)
        room.host(meeting)
        self.assertEqual(room.available_at, 10)

    def test_host_adds_meeting(self):
        room = Room()
        meeting = Meeting(3, 10, 2)
        room.host(meeting)
        self.assertEqual(len(room.meetings), 1)
        self.assertIs(room.meetings[0], meeting)

    # --- Scheduler (integration) ---

    def test_scheduler_simple(self):
        data = [(1, 5, 1), (5, 8, 2)]
        self.assertEqual(minimum_rooms(data), 1)

    # --- Hidden ---

    def test_scheduler_overlap(self):
        data = [(1, 5, 1), (2, 6, 2)]
        self.assertEqual(minimum_rooms(data), 2)

    def test_scheduler_many(self):
        data = [(1, 4, 1), (2, 5, 2), (3, 6, 3), (6, 8, 1)]
        self.assertEqual(minimum_rooms(data), 3)

    def test_scheduler_non_overlapping(self):
        data = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 5, 1)]
        self.assertEqual(minimum_rooms(data), 1)

    def test_scheduler_complex(self):
        data = [(1, 7, 2), (3, 5, 3), (5, 9, 1), (8, 10, 2), (10, 12, 3)]
        self.assertEqual(minimum_rooms(data), 2)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

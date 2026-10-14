"""Meeting Room Scheduler -- Family 03, Assessment 02 (starter).

Complete the Meeting and Room classes. Do NOT modify minimum_rooms.
"""


class Meeting:
    """Represents one scheduled meeting."""

    def __init__(self, start, end, attendees):
        """Initialize a scheduled meeting.

        Args:
            start (int): Starting time.
            end (int): Ending time.
            attendees (int): Number of attendees.
        """

        # TODO: Write your solution here.

        return


class Room:
    """Represents one meeting room."""

    def __init__(self):
        """Initialize a room.

        A room starts available at time 0 and has no assigned meetings.
        """

        # TODO: Write your solution here.

        return

    def can_host(self, meeting):
        """Return True if this room can host the given meeting.

        Args:
            meeting (Meeting): The meeting to check.

        Returns:
            bool: True if the meeting can be hosted, False otherwise.
        """

        # TODO: Write your solution here.

        return False

    def host(self, meeting):
        """Assign a meeting to this room.

        Args:
            meeting (Meeting): The meeting to host.
        """

        # TODO: Write your solution here.

        return


def minimum_rooms(meeting_data):
    """The scheduling algorithm. Students do NOT modify this function."""
    # Meetings are processed in order of starting time.
    ordered_data = sorted(meeting_data)

    meetings = []
    for start, end, attendees in ordered_data:
        meetings.append(Meeting(start, end, attendees))

    rooms = []

    for meeting in meetings:
        assigned = False

        for room in rooms:
            if room.can_host(meeting):
                room.host(meeting)
                assigned = True
                break

        if not assigned:
            room = Room()
            room.host(meeting)
            rooms.append(room)

    return len(rooms)

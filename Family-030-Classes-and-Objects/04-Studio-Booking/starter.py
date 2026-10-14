"""Studio Booking -- Family 03, Assessment 04 (starter).

Complete the Session and Studio classes. Do NOT modify minimum_studios.
"""


class Session:
    """Represents one recording session."""

    def __init__(self, start, end, musicians):
        """Initialize a recording session.

        Args:
            start (int): Starting time.
            end (int): Ending time.
            musicians (int): Number of musicians.
        """

        # TODO: Write your solution here.

        return


class Studio:
    """Represents one recording studio."""

    def __init__(self):
        """Initialize a studio.

        A studio starts available at time 0 and has no assigned sessions.
        """

        # TODO: Write your solution here.

        return

    def can_book(self, session):
        """Return True if this studio can book the given session.

        Args:
            session (Session): The session to check.

        Returns:
            bool: True if the session can be booked, False otherwise.
        """

        # TODO: Write your solution here.

        return False

    def book(self, session):
        """Assign a session to this studio.

        Args:
            session (Session): The session to book.
        """

        # TODO: Write your solution here.

        return


def minimum_studios(session_data):
    """The scheduling algorithm. Students do NOT modify this function."""
    # Sessions are processed in order of starting time.
    ordered_data = sorted(session_data)

    sessions = []
    for start, end, musicians in ordered_data:
        sessions.append(Session(start, end, musicians))

    studios = []

    for session in sessions:
        assigned = False

        for studio in studios:
            if studio.can_book(session):
                studio.book(session)
                assigned = True
                break

        if not assigned:
            studio = Studio()
            studio.book(session)
            studios.append(studio)

    return len(studios)

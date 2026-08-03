"""Studio Booking -- Family 03, Assessment 04 (teacher solution)."""


class Session:
    """Represents one recording session."""

    def __init__(self, start, end, musicians):
        """Initialize a recording session.

        Args:
            start (int): Starting time.
            end (int): Ending time.
            musicians (int): Number of musicians.
        """
        self.start = start
        self.end = end
        self.musicians = musicians


class Studio:
    """Represents one recording studio."""

    def __init__(self):
        """Initialize a studio.

        A studio starts available at time 0 and has no assigned sessions.
        """
        self.available_at = 0
        self.sessions = []

    def can_book(self, session):
        """Return True if this studio can book the given session.

        Args:
            session (Session): The session to check.

        Returns:
            bool: True if the session can be booked, False otherwise.
        """
        return session.start >= self.available_at

    def book(self, session):
        """Assign a session to this studio.

        Args:
            session (Session): The session to book.
        """
        self.sessions.append(session)
        self.available_at = session.end


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


if __name__ == "__main__":
    session = Session(5, 8, 2)
    studio = Studio()

    print(studio.can_book(session))
    studio.book(session)
    print(studio.available_at)

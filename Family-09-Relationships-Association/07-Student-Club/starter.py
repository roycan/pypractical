"""Student Club -- Family 09, Assessment 07 (starter).

The Club class is provided and complete. Complete the Student class.
"""


# Provided class. Do NOT modify it.
class Club:
    """Represents one school club."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        """Return the club's name."""
        return self.name

    def get_description(self):
        """Return the club's description."""
        return self.description


class Student:
    """Represents a student who joins clubs."""

    def __init__(self, name):
        """Initialize a student with no clubs.

        Args:
            name (str): The student's name.
        """

        # TODO: Write your solution here.

        return

    def join_club(self, club):
        """Join a club, unless already a member.

        Args:
            club (Club): The club to join.
        """

        # TODO: Write your solution here.

        return

    def leave_club(self, club_name):
        """Leave a club by name.

        Args:
            club_name (str): The name of the club to leave.

        Returns:
            bool: True if removed, False if not a member.
        """

        # TODO: Write your solution here.

        return False

    def is_member(self, club_name):
        """Return True if the student belongs to the club.

        Args:
            club_name (str): The club name to check.

        Returns:
            bool: True if the student is a member.
        """

        # TODO: Write your solution here.

        return False

    def list_clubs(self):
        """Return a list of club names the student belongs to.

        Returns:
            list: A list of club name strings.
        """

        # TODO: Write your solution here.

        return []
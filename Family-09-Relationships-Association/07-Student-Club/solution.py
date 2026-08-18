"""Student Club -- Family 09, Assessment 07 (teacher solution)."""


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
        """Initialize a student with no clubs."""
        self.name = name
        self.clubs = []

    def join_club(self, club):
        """Join a club, unless already a member."""
        if self.is_member(club.get_name()):
            return
        self.clubs.append(club)

    def leave_club(self, club_name):
        """Leave a club by name."""
        for club in self.clubs:
            if club.get_name() == club_name:
                self.clubs.remove(club)
                return True
        return False

    def is_member(self, club_name):
        """Return True if the student belongs to the club."""
        for club in self.clubs:
            if club.get_name() == club_name:
                return True
        return False

    def list_clubs(self):
        """Return a list of club names the student belongs to."""
        names = []
        for club in self.clubs:
            names.append(club.get_name())
        return names


if __name__ == "__main__":
    student = Student("Ada")
    chess = Club("Chess", "Play chess")
    art = Club("Art", "Paint and draw")
    student.join_club(chess)
    student.join_club(art)
    student.join_club(chess)
    print(student.list_clubs())
    print(student.is_member("Art"))
    print(student.leave_club("Chess"))
    print(student.list_clubs())
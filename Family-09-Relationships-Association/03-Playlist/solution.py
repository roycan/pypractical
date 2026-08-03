"""Playlist -- Family 09, Assessment 03 (teacher solution)."""


# Provided class. Do NOT modify it.
class Song:
    """Represents one song in a playlist."""

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def get_title(self):
        """Return the song's title."""
        return self.title

    def get_artist(self):
        """Return the song's artist."""
        return self.artist


class Playlist:
    """Represents a playlist that holds many songs."""

    def __init__(self):
        """Initialize a playlist with an empty list of songs."""
        self.songs = []

    def add_song(self, song):
        """Add one song to the playlist."""
        self.songs.append(song)

    def count_songs(self):
        """Return the number of songs in the playlist."""
        return len(self.songs)

    def find_by_title(self, title):
        """Return the first song with the given title, or None."""
        for song in self.songs:
            if song.get_title() == title:
                return song
        return None


if __name__ == "__main__":
    playlist = Playlist()
    playlist.add_song(Song("Sunrise", "Ada"))
    playlist.add_song(Song("Nightfall", "Bo"))
    print(playlist.count_songs())

    found = playlist.find_by_title("Sunrise")
    print(found.get_artist())

    missing = playlist.find_by_title("Missing")
    print(missing)

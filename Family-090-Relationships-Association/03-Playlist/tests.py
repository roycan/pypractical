"""Unit tests for Playlist -- Family 09, Assessment 03."""

import unittest

try:
    from solution import Song, Playlist
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestPlaylist(unittest.TestCase):

    # --- count ---

    def test_empty_playlist_count(self):
        playlist = Playlist()
        self.assertEqual(playlist.count_songs(), 0)

    def test_add_one_song(self):
        playlist = Playlist()
        playlist.add_song(Song("Sunrise", "Ada"))
        self.assertEqual(playlist.count_songs(), 1)

    def test_add_two_songs(self):
        playlist = Playlist()
        playlist.add_song(Song("Sunrise", "Ada"))
        playlist.add_song(Song("Nightfall", "Bo"))
        self.assertEqual(playlist.count_songs(), 2)

    # --- find_by_title ---

    def test_find_returns_song(self):
        playlist = Playlist()
        playlist.add_song(Song("Sunrise", "Ada"))
        self.assertEqual(playlist.find_by_title("Sunrise").get_artist(), "Ada")

    def test_find_not_found_returns_none(self):
        playlist = Playlist()
        playlist.add_song(Song("Sunrise", "Ada"))
        result = playlist.find_by_title("Missing")
        self.assertIsNone(result)

    def test_find_correct_song_among_many(self):
        playlist = Playlist()
        playlist.add_song(Song("A", "X"))
        playlist.add_song(Song("B", "Y"))
        playlist.add_song(Song("C", "Z"))
        self.assertEqual(playlist.find_by_title("B").get_artist(), "Y")

    def test_find_first_match(self):
        playlist = Playlist()
        playlist.add_song(Song("Sunrise", "Ada"))
        playlist.add_song(Song("Sunrise", "Extra"))
        self.assertEqual(playlist.find_by_title("Sunrise").get_artist(), "Ada")

    # --- Hidden ---

    def test_hidden_count_three(self):
        playlist = Playlist()
        playlist.add_song(Song("A", "X"))
        playlist.add_song(Song("B", "Y"))
        playlist.add_song(Song("C", "Z"))
        self.assertEqual(playlist.count_songs(), 3)

    def test_hidden_find_among_many(self):
        playlist = Playlist()
        playlist.add_song(Song("Alpha", "1"))
        playlist.add_song(Song("Beta", "2"))
        playlist.add_song(Song("Gamma", "3"))
        self.assertEqual(playlist.find_by_title("Gamma").get_artist(), "3")

    def test_hidden_not_found_among_many(self):
        playlist = Playlist()
        playlist.add_song(Song("Alpha", "1"))
        playlist.add_song(Song("Beta", "2"))
        playlist.add_song(Song("Gamma", "3"))
        self.assertIsNone(playlist.find_by_title("Delta"))

    def test_hidden_independent_playlists(self):
        playlist1 = Playlist()
        playlist2 = Playlist()
        playlist1.add_song(Song("A", "X"))
        playlist2.add_song(Song("B", "Y"))
        self.assertEqual(playlist1.count_songs(), 1)
        self.assertEqual(playlist2.count_songs(), 1)
        self.assertIsNone(playlist1.find_by_title("B"))

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

# Playlist

## Story

A playlist holds many songs — that is a one-to-many relationship: one playlist,
many songs.

The `Song` class is already written. Complete the `Playlist` class so it stores
songs, counts them, and finds a song by title.

## Task

The `Song` class is provided and complete. Do **not** modify it.

Complete the `Playlist` class. A playlist stores a list of `Song` objects, can
add a song, count how many songs it holds, and find the first song with a given
title.

## Class Specification

### Song (provided, do not modify)

A `Song` object represents one song in a playlist.

It stores:

- the title (`title`)
- the artist (`artist`)

It provides `get_title` (returns the title) and `get_artist` (returns the
artist).

### Playlist

A `Playlist` object represents one playlist.

It stores:

- a list of songs (`songs`)

Initially the list is empty.

## Required Methods

### Playlist.__init__()

Create an empty list named `songs`.

### Playlist.add_song(song)

Append the given song to the end of `songs`.

### Playlist.count_songs()

Return the number of songs stored in the playlist.

### Playlist.find_by_title(title)

Loop over `songs`. Return the first song whose title matches the given title. If
no song matches, return `None`.

## Constraints

- Titles and artists are non-empty strings
- Titles may repeat; `find_by_title` returns the first match
- All inputs are valid

## Example

```python
playlist = Playlist()
playlist.add_song(Song("Sunrise", "Ada"))
playlist.add_song(Song("Nightfall", "Bo"))
print(playlist.count_songs())

found = playlist.find_by_title("Sunrise")
print(found.get_artist())

missing = playlist.find_by_title("Missing")
print(missing)
```

Output

```text
2
Ada
None
```

## Explanation

The playlist holds a list of songs. `count_songs` returns how many (2).
`find_by_title` loops over the songs and returns the first song whose title
matches — `"Sunrise"` is by `"Ada"`. When no song matches (`"Missing"`), it
returns `None`. One playlist, many songs: that is a one-to-many association.

## Hint

In `find_by_title`, loop over `self.songs`, compare `song.get_title()` with the
given title, and return the song on the first match. After the loop, return
`None`.

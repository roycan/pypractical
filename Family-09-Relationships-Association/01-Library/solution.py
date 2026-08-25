"""Library -- Family 09, Assessment 01 (teacher solution)."""


# Provided class. Do NOT modify it.
class Book:
    """Represents one book in a library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        """Return the book's title."""
        return self.title

    def get_author(self):
        """Return the book's author."""
        return self.author


class Library:
    """Represents a library that holds many books."""

    def __init__(self):
        """Initialize a library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add one book to the library."""
        self.books.append(book)

    def count_books(self):
        """Return the number of books in the library."""
        return len(self.books)

    def find_by_title(self, title):
        """Return the first book with the given title, or None."""
        for book in self.books:
            if book.get_title() == title:
                return book
        return None


if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Python Basics", "Ada"))
    library.add_book(Book("Data Works", "Bo"))
    print(library.count_books())

    found = library.find_by_title("Python Basics")
    if found is not None:
        print(found.get_author())
    else:
        print("Not found")

    missing = library.find_by_title("No Book")
    print(missing)

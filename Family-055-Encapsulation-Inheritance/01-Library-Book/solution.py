"""Library Book -- Family 055, Assessment 01 (teacher solution)."""


# Provided class. Do NOT modify it.
class Publication:
    """Represents a basic publication."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        """Return a one-line description of the publication.

        Returns:
            str: The publication's title and author.
        """
        return f"Title: {self.title}, Author: {self.author}"


class Book(Publication):
    """Represents a book with a protected page count."""

    def __init__(self, title, author, number_of_pages):
        """Initialize a book.

        Args:
            title (str): The book's title.
            author (str): The book's author.
            number_of_pages (int): The book's page count.
        """
        super().__init__(title, author)
        if number_of_pages <= 0:
            print("The number of pages must be positive")
            self._number_of_pages = 0
        else:
            self._number_of_pages = number_of_pages

    def get_number_of_pages(self):
        """Return the protected page count.

        Returns:
            int: The book's page count (0 when it was not recorded).
        """
        return self._number_of_pages


if __name__ == "__main__":
    publication = Publication("Poems", "A. Cruz")
    print(publication.display_info())

    book = Book("Clean Code", "R. Martin", 464)
    print(book.display_info())
    print(book.get_number_of_pages())

    bad_book = Book("Mystery", "J. Doe", -5)
    print(bad_book.get_number_of_pages())

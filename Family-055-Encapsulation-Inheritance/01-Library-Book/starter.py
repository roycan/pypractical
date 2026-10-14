"""Library Book -- Family 055, Assessment 01 (starter).

The Publication class is provided and complete. Complete the Book class.
"""


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


class Book():                                  # TODO 1: make Book inherit from Publication
    """Represents a book with a protected page count."""

    def __init__(self, title, author, number_of_pages):
        """Initialize a book.

        Args:
            title (str): The book's title.
            author (str): The book's author.
            number_of_pages (int): The book's page count.
        """

        # TODO 2: Call super().__init__(title, author).
        # TODO 3: If number_of_pages is zero or negative, print
        #         "The number of pages must be positive" and store 0
        #         (0 means "not recorded"); otherwise store the value in the
        #         protected attribute _number_of_pages.

        return

    def get_number_of_pages(self):
        """Return the protected page count.

        Returns:
            int: The book's page count (0 when it was not recorded).
        """

        # TODO 4: Return the protected _number_of_pages.

        return 0

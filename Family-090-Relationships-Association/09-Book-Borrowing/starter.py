"""Book Borrowing -- Family 090, Assessment 09 (starter).

Complete the Book and Member classes. The borrowing management
algorithm is provided and complete. Do not modify it.
"""


class Book:
    """Represents one library book."""

    def __init__(self, title, author, copies):
        """Initialize a book.

        Args:
            title (str): Book title.
            author (str): Author name.
            copies (int): Number of available copies.
        """

        # TODO: Save the values as instance variables.

        return


class Member:
    """Represents one library member."""

    def __init__(self, limit):
        """Initialize a member that has borrowed no books yet.

        Args:
            limit (int): Maximum number of books the
                member can borrow.
        """

        # TODO: Save the limit and create the empty list borrowed_books.

        return

    def can_borrow(self, book):
        """Return True if this member can borrow the given book.

        A member can borrow a book when the borrowing limit is
        not reached and the book has at least one available copy.

        Args:
            book (Book): The book to check.

        Returns:
            bool: True if borrowing is allowed, otherwise False.
        """

        # TODO: Check the limit and the available copies.

        return False

    def borrow(self, book):
        """Borrow one book.

        This should:

        1. Add the book to self.borrowed_books.
        2. Decrease the book's available copies by 1.

        Args:
            book (Book): The book to borrow.
        """

        # TODO: Remember the book and decrease its copies.

        return


# Provided function. Do NOT modify it.
def process_borrow_requests(requests):
    """The borrowing management algorithm.

    Students do NOT modify this function.
    """
    books = {}
    members = {}

    for action, *data in requests:
        if action == "ADD_BOOK":
            title, author, copies = data
            books[title] = Book(title, author, copies)

        elif action == "ADD_MEMBER":
            member_id, limit = data
            members[member_id] = Member(limit)

        elif action == "BORROW":
            member_id, title = data
            member = members[member_id]
            book = books[title]
            if member.can_borrow(book):
                member.borrow(book)

    return books, members

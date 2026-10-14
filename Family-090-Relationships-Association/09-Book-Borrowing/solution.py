"""Book Borrowing -- Family 090, Assessment 09 (teacher solution)."""


class Book:
    """Represents one library book."""

    def __init__(self, title, author, copies):
        """Initialize a book with its title, author, and copies."""
        self.title = title
        self.author = author
        self.copies = copies


class Member:
    """Represents one library member."""

    def __init__(self, limit):
        """Initialize a member with a borrowing limit and no books."""
        self.limit = limit
        self.borrowed_books = []

    def can_borrow(self, book):
        """Return True if this member can borrow the given book."""
        return len(self.borrowed_books) < self.limit and book.copies > 0

    def borrow(self, book):
        """Add the book to the member's list and decrease its copies."""
        self.borrowed_books.append(book)
        book.copies = book.copies - 1


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


if __name__ == "__main__":
    book = Book("Python Basics", "Smith", 3)
    member = Member(2)

    print(member.can_borrow(book))

    member.borrow(book)
    print(book.copies)
    print(len(member.borrowed_books))

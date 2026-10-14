"""Unit tests for Book Borrowing -- Family 090, Assessment 09."""

import unittest

try:
    from solution import Book, Member, process_borrow_requests
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestBookBorrowing(unittest.TestCase):

    # ---------- Book ----------

    def test_book_title(self):
        book = Book("Python Basics", "Smith", 3)
        self.assertEqual(book.title, "Python Basics")

    def test_book_author(self):
        book = Book("Python Basics", "Smith", 3)
        self.assertEqual(book.author, "Smith")

    def test_book_copies(self):
        book = Book("Python Basics", "Smith", 3)
        self.assertEqual(book.copies, 3)

    # ---------- Member ----------

    def test_member_limit(self):
        member = Member(2)
        self.assertEqual(member.limit, 2)

    def test_member_initial_books(self):
        member = Member(2)
        self.assertEqual(len(member.borrowed_books), 0)

    def test_can_borrow_true(self):
        member = Member(2)
        book = Book("Python Basics", "Smith", 3)
        self.assertTrue(member.can_borrow(book))

    def test_can_borrow_false_no_copies(self):
        member = Member(2)
        book = Book("Python Basics", "Smith", 0)
        self.assertFalse(member.can_borrow(book))

    def test_can_borrow_false_limit_reached(self):
        member = Member(1)
        book1 = Book("Book A", "Author A", 3)
        book2 = Book("Book B", "Author B", 3)
        member.borrow(book1)
        self.assertFalse(member.can_borrow(book2))

    def test_borrow_updates_copies(self):
        member = Member(2)
        book = Book("Python Basics", "Smith", 3)
        member.borrow(book)
        self.assertEqual(book.copies, 2)

    def test_borrow_adds_book(self):
        member = Member(2)
        book = Book("Python Basics", "Smith", 3)
        member.borrow(book)
        self.assertEqual(len(member.borrowed_books), 1)
        self.assertIs(member.borrowed_books[0], book)

    # ---------- Borrowing System ----------

    def test_borrowing_simple(self):
        requests = [
            ("ADD_BOOK", "Python Basics", "Smith", 3),
            ("ADD_MEMBER", "M001", 2),
            ("BORROW", "M001", "Python Basics"),
        ]

        books, members = process_borrow_requests(requests)

        self.assertEqual(books["Python Basics"].copies, 2)
        self.assertEqual(len(members["M001"].borrowed_books), 1)

    # ---------- Hidden Tests ----------

    def test_hidden_limit_reached(self):
        requests = [
            ("ADD_BOOK", "Book A", "Author A", 3),
            ("ADD_BOOK", "Book B", "Author B", 3),
            ("ADD_MEMBER", "M001", 1),
            ("BORROW", "M001", "Book A"),
            ("BORROW", "M001", "Book B"),
        ]

        books, members = process_borrow_requests(requests)

        self.assertEqual(len(members["M001"].borrowed_books), 1)
        self.assertEqual(books["Book B"].copies, 3)

    def test_hidden_no_copies(self):
        requests = [
            ("ADD_BOOK", "Python Basics", "Smith", 0),
            ("ADD_MEMBER", "M001", 2),
            ("BORROW", "M001", "Python Basics"),
        ]

        books, members = process_borrow_requests(requests)

        self.assertEqual(len(members["M001"].borrowed_books), 0)

    def test_hidden_multiple_books(self):
        requests = [
            ("ADD_BOOK", "Book A", "Author A", 3),
            ("ADD_BOOK", "Book B", "Author B", 2),
            ("ADD_MEMBER", "M001", 3),
            ("BORROW", "M001", "Book A"),
            ("BORROW", "M001", "Book B"),
        ]

        books, members = process_borrow_requests(requests)

        self.assertEqual(len(members["M001"].borrowed_books), 2)
        self.assertEqual(books["Book A"].copies, 2)
        self.assertEqual(books["Book B"].copies, 1)

    def test_hidden_multiple_members(self):
        requests = [
            ("ADD_BOOK", "Python Basics", "Smith", 1),
            ("ADD_MEMBER", "M001", 2),
            ("ADD_MEMBER", "M002", 2),
            ("BORROW", "M001", "Python Basics"),
            ("BORROW", "M002", "Python Basics"),
        ]

        books, members = process_borrow_requests(requests)

        self.assertEqual(books["Python Basics"].copies, 0)
        self.assertEqual(len(members["M001"].borrowed_books), 1)
        self.assertEqual(len(members["M002"].borrowed_books), 0)

    def test_hidden_exact_limit(self):
        requests = [
            ("ADD_BOOK", "Book A", "Author A", 5),
            ("ADD_BOOK", "Book B", "Author B", 5),
            ("ADD_MEMBER", "M001", 2),
            ("BORROW", "M001", "Book A"),
            ("BORROW", "M001", "Book B"),
        ]

        books, members = process_borrow_requests(requests)

        self.assertEqual(len(members["M001"].borrowed_books), 2)

    def test_hidden_exhaust_inventory(self):
        requests = [
            ("ADD_BOOK", "Book A", "Author A", 2),
            ("ADD_MEMBER", "M001", 3),
            ("ADD_MEMBER", "M002", 3),
            ("BORROW", "M001", "Book A"),
            ("BORROW", "M002", "Book A"),
        ]

        books, members = process_borrow_requests(requests)

        self.assertEqual(books["Book A"].copies, 0)
        self.assertEqual(len(members["M001"].borrowed_books), 1)
        self.assertEqual(len(members["M002"].borrowed_books), 1)


# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

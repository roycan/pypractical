"""Unit tests for Library -- Family 09, Assessment 01."""

import unittest

from solution import Book, Library


class TestLibrary(unittest.TestCase):

    # --- count ---

    def test_empty_library_count(self):
        library = Library()
        self.assertEqual(library.count_books(), 0)

    def test_add_one_book(self):
        library = Library()
        library.add_book(Book("A", "X"))
        self.assertEqual(library.count_books(), 1)

    def test_add_two_books(self):
        library = Library()
        library.add_book(Book("A", "X"))
        library.add_book(Book("B", "Y"))
        self.assertEqual(library.count_books(), 2)

    # --- find_by_title ---

    def test_find_returns_book(self):
        library = Library()
        library.add_book(Book("Python Basics", "Ada"))
        self.assertEqual(library.find_by_title("Python Basics").get_author(), "Ada")

    def test_find_not_found_returns_none(self):
        library = Library()
        library.add_book(Book("A", "X"))
        result = library.find_by_title("No Book")
        self.assertIsNone(result)

    def test_find_correct_book_among_many(self):
        library = Library()
        library.add_book(Book("A", "X"))
        library.add_book(Book("B", "Y"))
        library.add_book(Book("C", "Z"))
        self.assertEqual(library.find_by_title("B").get_author(), "Y")

    def test_find_first_match(self):
        library = Library()
        library.add_book(Book("A", "X"))
        library.add_book(Book("A", "W"))
        self.assertEqual(library.find_by_title("A").get_author(), "X")

    # --- Hidden ---

    def test_hidden_count_three(self):
        library = Library()
        library.add_book(Book("A", "X"))
        library.add_book(Book("B", "Y"))
        library.add_book(Book("C", "Z"))
        self.assertEqual(library.count_books(), 3)

    def test_hidden_find_among_many(self):
        library = Library()
        library.add_book(Book("Alpha", "1"))
        library.add_book(Book("Beta", "2"))
        library.add_book(Book("Gamma", "3"))
        self.assertEqual(library.find_by_title("Gamma").get_author(), "3")

    def test_hidden_not_found_among_many(self):
        library = Library()
        library.add_book(Book("Alpha", "1"))
        library.add_book(Book("Beta", "2"))
        library.add_book(Book("Gamma", "3"))
        self.assertIsNone(library.find_by_title("Delta"))

    def test_hidden_independent_libraries(self):
        library1 = Library()
        library2 = Library()
        library1.add_book(Book("A", "X"))
        library2.add_book(Book("B", "Y"))
        self.assertEqual(library1.count_books(), 1)
        self.assertEqual(library2.count_books(), 1)
        self.assertIsNone(library1.find_by_title("B"))

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

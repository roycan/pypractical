"""Unit tests for Library Book -- Family 055, Assessment 01."""

import contextlib
import io
import unittest

try:
    from solution import Book, Publication
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


def _construction_output(cls, *args):
    """Construct cls(*args) while capturing stdout.

    Capturing only what is printed DURING the call keeps demo output from
    polluting the validation checks.

    Args:
        cls (type): The class to instantiate.
        *args: The constructor arguments.

    Returns:
        tuple: The text printed during construction and the new object.
    """
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        obj = cls(*args)
    return buffer.getvalue().strip(), obj


class TestLibraryBook(unittest.TestCase):

    # --- Inheritance ---

    def test_book_is_subclass_of_publication(self):
        self.assertTrue(issubclass(Book, Publication))

    def test_book_instance_is_a_publication(self):
        book = Book("Clean Code", "R. Martin", 464)
        self.assertIsInstance(book, Book)
        self.assertIsInstance(book, Publication)

    def test_book_inherits_title_via_super(self):
        book = Book("Clean Code", "R. Martin", 464)
        self.assertEqual(book.title, "Clean Code")

    def test_book_inherits_author_via_super(self):
        book = Book("Clean Code", "R. Martin", 464)
        self.assertEqual(book.author, "R. Martin")

    def test_book_uses_inherited_display_info(self):
        book = Book("Clean Code", "R. Martin", 464)
        result = book.display_info()
        self.assertIsInstance(result, str)
        self.assertIn("Clean Code", result)
        self.assertIn("R. Martin", result)

    # --- Encapsulation ---

    def test_value_stored_in_protected_attribute(self):
        book = Book("Clean Code", "R. Martin", 464)
        self.assertTrue(hasattr(book, "_number_of_pages"))
        self.assertEqual(book.get_number_of_pages(), 464)

    def test_zero_pages_prints_warning(self):
        out, _ = _construction_output(Book, "Empty", "J. Doe", 0)
        self.assertIn("positive", out.lower())

    def test_negative_pages_prints_warning(self):
        out, _ = _construction_output(Book, "Mystery", "J. Doe", -5)
        self.assertIn("positive", out.lower())

    def test_invalid_pages_stored_as_zero_fallback(self):
        _, book = _construction_output(Book, "Mystery", "J. Doe", -5)
        self.assertEqual(book.get_number_of_pages(), 0)

    def test_valid_book_prints_no_warning(self):
        out, _ = _construction_output(Book, "Clean Code", "R. Martin", 464)
        self.assertNotIn("positive", out.lower())

    # --- Integration ---

    def test_two_books_are_independent(self):
        first = Book("Clean Code", "R. Martin", 464)
        second = Book("The Hobbit", "J.R.R. Tolkien", 310)
        self.assertEqual(first.get_number_of_pages(), 464)
        self.assertEqual(second.get_number_of_pages(), 310)

    # --- Hidden ---

    def test_hidden_publication_works_standalone(self):
        publication = Publication("Poems", "A. Cruz")
        self.assertEqual(publication.title, "Poems")
        self.assertEqual(publication.author, "A. Cruz")
        self.assertIn("Poems", publication.display_info())

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()

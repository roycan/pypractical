"""Book Inventory -- Family 02, Assessment 02 (teacher solution)."""


class Book:
    """Represents one book in the bookstore inventory."""

    def __init__(self, title, price, copies):
        """Initialize a book.

        Args:
            title (str): Book title.
            price (int): Price for one copy.
            copies (int): Number of copies in stock.
        """
        self.title = title
        self.price = price
        self.copies = copies

    def stock_value(self):
        """Return the total value of this book's stock.

        Returns:
            int: price multiplied by copies.
        """
        return self.price * self.copies


if __name__ == "__main__":
    book = Book("Python Basics", 300, 4)
    print(book.title)
    print(book.price)
    print(book.copies)
    print(book.stock_value())

# Book Inventory

## Story

A small bookstore keeps an inventory of books. Each book has a title, a price
for one copy, and a quantity showing how many copies are in stock.

A junior programmer wrote the store software using separate variables and a
function that takes three arguments. The bookstore clerk finds this confusing,
because every book's information is scattered.

You will model each book as an **object** that holds its own title, price, and
copies, and that can report its own total stock value.

## Task

Complete the `Book` class so each book object stores its own data and can
report its total stock value.

## Class Specification

### Book

A `Book` object represents one title in the bookstore inventory.

Each book stores:

- title
- price for one copy
- copies in stock

## Required Methods

### Book.__init__(title, price, copies)

Store the three values as instance variables.

### Book.stock_value()

Return the total value of this book's stock.

The total value is:

```text
price * copies
```

## Constraints

- The title is a non-empty string.
- The price is a positive integer (1 or more).
- The number of copies is zero or a positive integer (0 or more).

All input values are valid.

## Example

```python
book = Book("Python Basics", 300, 4)

print(book.title)
print(book.price)
print(book.copies)
print(book.stock_value())
```

Output

```text
Python Basics
300
4
1200
```

## Explanation

The book object stores its own three values: title `"Python Basics"`, price
`300`, and copies `4`.

The total stock value is `price * copies`, so `300 * 4 = 1200`.

Each book object remembers its own data, so two books never share or mix
their information.

## Hint

Objects store their own data in **instance variables** (written with `self.`).

- In `__init__`, save each parameter as an instance variable.
- In `stock_value`, use those instance variables. They belong to the object,
  so you do not pass them again.

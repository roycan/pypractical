# Price Cart

## Story

A shopping cart can hold different kinds of items: some are paid at full price,
some are paid at half price.

The item classes have already been written. The cart simply collects items and
reports each one's amount, calling the same `amount` method on every item no
matter which class it is.

## Task

The `FullPrice` and `HalfPrice` classes are provided and complete. Do **not**
modify them.

Complete the `Cart` class so it collects items and reports each one's amount and
the total.

## Class Specification

### FullPrice (provided, do not modify)

A `FullPrice` object represents one item paid at full price.

It stores:

- the item's name (`name`)
- the item's price (`price`)

Its `amount` method returns the full price.

### HalfPrice (provided, do not modify)

A `HalfPrice` object represents one item paid at half price.

It stores:

- the item's name (`name`)
- the item's price (`price`)

Its `amount` method returns half the price.

### Cart

A `Cart` object collects items and reports their amounts.

A cart should remember:

- every item added to it

## Required Methods

### Cart.__init__()

- Create an empty list named `items`.

### Cart.add(item)

Add the given item to the cart's list.

### Cart.amounts()

Loop over the cart's items, call `amount()` on each, and return the list of
results.

### Cart.total()

Loop over the cart's items, add each `amount()` to a running total, and return
the total (an integer).

## Constraints

- name is a non-empty string
- price is a positive integer
- `HalfPrice` uses integer division (half, rounded down)

All inputs are valid.

## Example

```python
cart = Cart()
cart.add(FullPrice("Book", 100))
cart.add(HalfPrice("Magazine", 100))
print(cart.amounts())
print(cart.total())
```

Output

```text
[100, 50]
150
```

## Explanation

`amounts()` calls `.amount()` on each item. A `FullPrice` returns its full price
(`100`); a `HalfPrice` returns half (`50`). The SAME method name gives different
results depending on the item's class — that is polymorphism. `total()` adds them
together: `100 + 50 = 150`.

## Hint

In `amounts` and `total`, loop over `self.items` and call `item.amount()` on each.
The cart does not need to know which class each item is — it just calls the
shared method.

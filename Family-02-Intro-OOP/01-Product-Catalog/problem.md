# Product Catalog

## Story

A small shop keeps a catalog of products. Each product has a name, a price for
one unit, and a quantity showing how many units are in stock.

A junior programmer wrote the shop software using separate variables and a
function that takes three arguments. The shop owner finds this confusing,
because every product's information is scattered.

You will model each product as an **object** that holds its own name, price, and
quantity, and that can report its own total stock value.

## Task

Complete the `Product` class so each product object stores its own data and can
report its total stock value.

## Class Specification

### Product

A `Product` object represents one item in the shop catalog.

Each product stores:

- name
- price for one unit
- quantity in stock

## Required Methods

### Product.__init__(name, price, quantity)

Store the three values as instance variables.

### Product.total_value()

Return the total value of this product's stock.

The total value is:

```text
price * quantity
```

## Constraints

- The name is a non-empty string.
- The price is a positive integer (1 or more).
- The quantity is zero or a positive integer (0 or more).

All input values are valid.

## Example

```python
product = Product("Notebook", 50, 3)

print(product.name)
print(product.price)
print(product.quantity)
print(product.total_value())
```

Output

```text
Notebook
50
3
150
```

## Explanation

The product object stores its own three values: name `"Notebook"`, price `50`,
and quantity `3`.

The total stock value is `price * quantity`, so `50 * 3 = 150`.

Each product object remembers its own data, so two products never share or mix
their information.

## Hint

Objects store their own data in **instance variables** (written with `self.`).

- In `__init__`, save each parameter as an instance variable.
- In `total_value`, use those instance variables. They belong to the object, so
  you do not pass them again.

# Inventory Tag

## Story

A warehouse records stock quantities and prints a tag.

A junior programmer put storing quantities, computing the total units, AND
formatting the tag all in one class. That class has too many jobs.

Your job is to apply the Single Responsibility Principle and split the work into
two classes.

## Task

Complete the **Stock** and **Tag** classes.

Give the **Stock** class one job: store quantities and compute the count and
total units. Give the **Tag** class a different job: format a summary string
from a Stock.

## Class Specification

### Stock

A `Stock` object records the quantities of warehouse items.

Each stock stores:

- a list of quantities

The Stock class is responsible for the **data**. It stores quantities and
computes the count and the total. It does **not** format any string.

### Tag

A `Tag` object builds a readable summary from a Stock.

The Tag class is responsible for the **presentation**. It does **not** store
any quantities. It reads them through the Stock it is given.

## Required Methods

### Stock.__init__()

- Create an empty list named `quantities`.

### Stock.add_quantity(quantity)

Append the quantity to the `quantities` list.

### Stock.count()

Return the number of recorded quantities.

### Stock.total()

Loop over `quantities`, sum them, and return the total.

### Tag.summary(stock)

Return the summary string built from the stock:

```text
"Items: " + str(stock.count()) + ", Units: " + str(stock.total())
```

## Constraints

- Quantities are positive integers.
- The summary string format is exactly `Items: <count>, Units: <total>`
  (note the space after each colon and the comma plus space).
- Use `str()` and string concatenation to build the summary. Do not use
  f-strings.
- Use an explicit loop to compute the total (not a comprehension).
- All inputs are valid.

## Example

```python
stock = Stock()
stock.add_quantity(100)
stock.add_quantity(200)
print(stock.count())
print(stock.total())

tag = Tag()
print(tag.summary(stock))
```

Output

```text
2
300
Items: 2, Units: 300
```

## Explanation

The Stock class has one responsibility: it stores quantities and computes
`count` and `total`. The Tag class has a different responsibility: it formats a
readable summary from a Stock. The Tag does not store quantities — it reads them
through the Stock it is given. Splitting the job this way is the Single
Responsibility Principle: each class has one reason to change.

## Hint

Keep the two responsibilities apart. Stock only stores and calculates. Tag only
builds the string:

`"Items: " + str(stock.count()) + ", Units: " + str(stock.total())`

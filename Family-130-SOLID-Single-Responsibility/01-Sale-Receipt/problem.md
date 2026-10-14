# Sale Receipt

## Story

A shop records sale amounts and prints a receipt.

A junior programmer put storing amounts, computing the total, AND formatting the
receipt all in one class. That class has too many jobs.

Your job is to apply the Single Responsibility Principle and split the work into
two classes.

## Task

Complete the **Sale** and **Receipt** classes.

Give the **Sale** class one job: store amounts and compute the count and total.
Give the **Receipt** class a different job: format a summary string from a Sale.

## Class Specification

### Sale

A `Sale` object records the amounts of a sale.

Each sale stores:

- a list of amounts

The Sale class is responsible for the **data**. It stores amounts and computes
the count and the total. It does **not** format any string.

### Receipt

A `Receipt` object builds a readable summary from a Sale.

The Receipt class is responsible for the **presentation**. It does **not** store
any amounts. It reads them through the Sale it is given.

## Required Methods

### Sale.__init__()

- Create an empty list named `amounts`.

### Sale.add_amount(amount)

Append the amount to the `amounts` list.

### Sale.count()

Return the number of recorded amounts.

### Sale.total()

Loop over `amounts`, sum them, and return the total.

### Receipt.summary(sale)

Return the summary string built from the sale:

```text
"Items: " + str(sale.count()) + ", Total: " + str(sale.total())
```

## Constraints

- Amounts are positive integers.
- The summary string format is exactly `Items: <count>, Total: <total>`
  (note the space after each colon and the comma plus space).
- Use `str()` and string concatenation to build the summary. Do not use
  f-strings.
- Use an explicit loop to compute the total (not a comprehension).
- All inputs are valid.

## Example

```python
sale = Sale()
sale.add_amount(100)
sale.add_amount(200)
print(sale.count())
print(sale.total())

receipt = Receipt()
print(receipt.summary(sale))
```

Output

```text
2
300
Items: 2, Total: 300
```

## Explanation

The Sale class has one responsibility: it stores amounts and computes `count`
and `total`. The Receipt class has a different responsibility: it formats a
readable summary from a Sale. The Receipt does not store amounts — it reads them
through the Sale it is given. Splitting the job this way is the Single
Responsibility Principle: each class has one reason to change.

## Hint

Keep the two responsibilities apart. Sale only stores and calculates. Receipt
only builds the string:

`"Items: " + str(sale.count()) + ", Total: " + str(sale.total())`

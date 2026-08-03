# Fee Report

## Story

A report lists payments made by customers. Some payments are in cash and some
are by card.

The payment classes have already been written. The report simply collects
payments and reports each one's fee, calling the same `fee` method on every
payment no matter which class it is.

## Task

The `Cash` and `Card` classes are provided and complete. Do **not** modify them.

Complete the `Report` class so it collects payments and reports each one's fee
and the total.

## Class Specification

### Cash (provided, do not modify)

A `Cash` object represents one payment made in cash.

It stores:

- the payment's name (`name`)
- the payment amount (`amount`)

Its `fee` method returns `0`.

### Card (provided, do not modify)

A `Card` object represents one payment made by card.

It stores:

- the payment's name (`name`)
- the payment amount (`amount`)

Its `fee` method returns `amount // 10`.

### Report

A `Report` object collects payments and reports their fees.

A report should remember:

- every payment added to it

## Required Methods

### Report.__init__()

- Create an empty list named `payments`.

### Report.add(payment)

Add the given payment to the report's list.

### Report.fees()

Loop over the report's payments, call `fee()` on each, and return the list of
results.

### Report.total_fees()

Loop over the report's payments, add each `fee()` to a running total, and return
the total (an integer).

## Constraints

- name is a non-empty string
- amount is a positive integer
- `Cash` has a fee of `0`
- `Card` has a fee of `amount // 10` (integer division)

All inputs are valid.

## Example

```python
report = Report()
report.add(Cash("A", 100))
report.add(Card("B", 100))
print(report.fees())
print(report.total_fees())
```

Output

```text
[0, 10]
10
```

## Explanation

`fees()` calls `.fee()` on each payment. A `Cash` payment returns `0`; a `Card`
payment returns `100 // 10 = 10`. The SAME method name gives different results
depending on the payment's class — that is polymorphism. `total_fees()` adds them
together: `0 + 10 = 10`.

## Hint

In `fees` and `total_fees`, loop over `self.payments` and call `payment.fee()` on
each. The report does not need to know which class each payment is — it just
calls the shared method.

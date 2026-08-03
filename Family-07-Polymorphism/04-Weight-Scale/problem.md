# Weight Scale

## Story

A scale records loads that need to be weighed. Some loads are light and some are
heavy.

The load classes have already been written. The scale simply collects loads and
reports each one's weight, calling the same `weight` method on every load no
matter which class it is.

## Task

The `Light` and `Heavy` classes are provided and complete. Do **not** modify
them.

Complete the `Scale` class so it collects loads and reports each one's weight and
the total.

## Class Specification

### Light (provided, do not modify)

A `Light` object represents one light load.

It stores:

- the load's name (`name`)
- the load's count (`count`)

Its `weight` method returns `count * 1`.

### Heavy (provided, do not modify)

A `Heavy` object represents one heavy load.

It stores:

- the load's name (`name`)
- the load's count (`count`)

Its `weight` method returns `count * 5`.

### Scale

A `Scale` object collects loads and reports their weights.

A scale should remember:

- every load added to it

## Required Methods

### Scale.__init__()

- Create an empty list named `loads`.

### Scale.add(load)

Add the given load to the scale's list.

### Scale.weights()

Loop over the scale's loads, call `weight()` on each, and return the list of
results.

### Scale.total_weight()

Loop over the scale's loads, add each `weight()` to a running total, and return
the total (an integer).

## Constraints

- name is a non-empty string
- count is a positive integer
- `Light` weighs `count * 1`
- `Heavy` weighs `count * 5`

All inputs are valid.

## Example

```python
scale = Scale()
scale.add(Light("A", 4))
scale.add(Heavy("B", 4))
print(scale.weights())
print(scale.total_weight())
```

Output

```text
[4, 20]
24
```

## Explanation

`weights()` calls `.weight()` on each load. A `Light` load returns `4 * 1 = 4`;
a `Heavy` load returns `4 * 5 = 20`. The SAME method name gives different results
depending on the load's class — that is polymorphism. `total_weight()` adds them
together: `4 + 20 = 24`.

## Hint

In `weights` and `total_weight`, loop over `self.loads` and call `load.weight()`
on each. The scale does not need to know which class each load is — it just calls
the shared method.

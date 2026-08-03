# Shipping Cost

## Story

An express parcel costs more to ship than a standard parcel. The `Parcel` class
has already been written and stores a parcel's name and weight.

A standard parcel ships for `5` per unit of weight. An express parcel ships for
`10` per unit of weight.

## Task

The `Parcel` class is provided and complete. Do **not** modify it.

Complete the `ExpressParcel` class so it inherits the parcel's data and
OVERRIDES the `shipping` method with the express rate.

## Class Specification

### Parcel (provided, do not modify)

A `Parcel` object represents one standard parcel.

Each parcel stores:

- the parcel's name (`name`)
- the parcel's weight (`weight`)

### ExpressParcel

An `ExpressParcel` object represents one parcel shipped at the express rate.

An express parcel inherits the parcel's name and weight.

## Required Methods

### ExpressParcel.__init__(name, weight)

Call `super().__init__(name, weight)` to reuse the parent's data.

### ExpressParcel.shipping()

Return the express shipping cost: `self.weight * 10`. This method OVERRIDES the
parent's `shipping` method.

## Constraints

- name is a non-empty string
- weight is a positive integer

All inputs are valid.

## Example

```python
parcel = Parcel("Box", 6)
print(parcel.get_name())
print(parcel.shipping())

express = ExpressParcel("Box", 6)
print(express.get_name())
print(express.shipping())
```

Output

```text
Box
30
Box
60
```

## Explanation

Both parcels have weight `6`. A standard parcel ships for `6 * 5 = 30`. An
express parcel OVERRIDES the `shipping` method, so `express.shipping()` uses the
express rate `6 * 10 = 60` instead. Same method name, different behavior in the
child — that is method overriding.

## Hint

In the child, call `super().__init__(name, weight)` to reuse the parent's data,
then write a `shipping` method with the express rate `self.weight * 10` to
override the parent's version.

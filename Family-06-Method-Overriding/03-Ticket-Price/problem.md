# Ticket Price

## Story

A first-class ticket costs more per unit of distance than a standard ticket. The
`Ticket` class has already been written and stores a ticket's name and its
distance.

A standard ticket costs `2` per unit of distance. A first-class ticket costs `4`
per unit of distance.

## Task

The `Ticket` class is provided and complete. Do **not** modify it.

Complete the `FirstClass` class so it inherits the ticket's data and OVERRIDES
the `price` method with the first-class rate.

## Class Specification

### Ticket (provided, do not modify)

A `Ticket` object represents one standard ticket.

Each ticket stores:

- the ticket's name (`name`)
- the ticket's distance (`distance`)

### FirstClass

A `FirstClass` object represents one ticket at the first-class rate.

A first-class ticket inherits the ticket's name and distance.

## Required Methods

### FirstClass.__init__(name, distance)

Call `super().__init__(name, distance)` to reuse the parent's data.

### FirstClass.price()

Return the first-class price: `self.distance * 4`. This method OVERRIDES the
parent's `price` method.

## Constraints

- name is a non-empty string
- distance is a positive integer

All inputs are valid.

## Example

```python
ticket = Ticket("Economy", 300)
print(ticket.get_name())
print(ticket.price())

first = FirstClass("Economy", 300)
print(first.get_name())
print(first.price())
```

Output

```text
Economy
600
Economy
1200
```

## Explanation

Both tickets cover a distance of `300`. A standard ticket costs `300 * 2 = 600`.
A first-class ticket OVERRIDES the `price` method, so `first.price()` uses the
first-class rate `300 * 4 = 1200` instead. Same method name, different behavior
in the child — that is method overriding.

## Hint

In the child, call `super().__init__(name, distance)` to reuse the parent's
data, then write a `price` method with the first-class rate
`self.distance * 4` to override the parent's version.

# Ticket Sales

## Story

A small venue keeps a record of ticket sales. Each event has a name, a ticket
price, and a number showing how many seats were sold.

A junior programmer wrote the venue software using separate variables and a
function that takes three arguments. The event staff finds this confusing,
because every event's information is scattered.

You will model each event as an **object** that holds its own name, ticket
price, and seats, and that can report its own potential revenue.

## Task

Complete the `Ticket` class so each event object stores its own data and can
report its potential revenue.

## Class Specification

### Ticket

A `Ticket` object represents one event at the venue.

Each ticket stores:

- event
- price for one ticket
- seats sold

## Required Methods

### Ticket.__init__(event, price, seats)

Store the three values as instance variables.

### Ticket.potential_revenue()

Return the potential revenue for this event.

The potential revenue is:

```text
price * seats
```

## Constraints

- The event is a non-empty string.
- The price is a positive integer (1 or more).
- The number of seats is zero or a positive integer (0 or more).

All input values are valid.

## Example

```python
ticket = Ticket("Concert", 500, 2)

print(ticket.event)
print(ticket.price)
print(ticket.seats)
print(ticket.potential_revenue())
```

Output

```text
Concert
500
2
1000
```

## Explanation

The ticket object stores its own three values: event `"Concert"`, price `500`,
and seats `2`.

The potential revenue is `price * seats`, so `500 * 2 = 1000`.

Each ticket object remembers its own data, so two tickets never share or mix
their information.

## Hint

Objects store their own data in **instance variables** (written with `self.`).

- In `__init__`, save each parameter as an instance variable.
- In `potential_revenue`, use those instance variables. They belong to the
  object, so you do not pass them again.

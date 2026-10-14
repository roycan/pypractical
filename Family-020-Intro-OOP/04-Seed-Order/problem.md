# Seed Order

## Story

A garden store keeps a shelf of seed packets. Each kind has a variety name, a
price for one packet, and a number showing how many packets are in the order.

A junior programmer wrote the store software using separate variables and a
function that takes three arguments. The garden staff finds this confusing,
because every kind's information is scattered.

You will model each kind of seed as an **object** that holds its own variety,
price, and packets, and that can report its own order total.

## Task

Complete the `SeedPacket` class so each kind object stores its own data and can
report its order total.

## Class Specification

### SeedPacket

A `SeedPacket` object represents one kind of seed packet in the store.

Each seed packet stores:

- variety
- price for one packet
- packets in the order

## Required Methods

### SeedPacket.__init__(variety, price, packets)

Store the three values as instance variables.

### SeedPacket.order_total()

Return the order total for this seed packet.

The order total is:

```text
price * packets
```

## Constraints

- The variety is a non-empty string.
- The price is a positive integer (1 or more).
- The number of packets is zero or a positive integer (0 or more).

All input values are valid.

## Example

```python
packet = SeedPacket("Basil", 25, 6)

print(packet.variety)
print(packet.price)
print(packet.packets)
print(packet.order_total())
```

Output

```text
Basil
25
6
150
```

## Explanation

The seed packet object stores its own three values: variety `"Basil"`, price
`25`, and packets `6`.

The order total is `price * packets`, so `25 * 6 = 150`.

Each seed packet object remembers its own data, so two packets never share or
mix their information.

## Hint

Objects store their own data in **instance variables** (written with `self.`).

- In `__init__`, save each parameter as an instance variable.
- In `order_total`, use those instance variables. They belong to the object,
  so you do not pass them again.

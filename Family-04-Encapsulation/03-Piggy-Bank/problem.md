# Piggy Bank

## Story

A piggy bank must never go below zero and must ignore invalid adds or takes.

The coins are protected inside the object. They are read with `get_coins` and
changed only through `add_coins` and `take_coins`.

## Task

Complete the `PiggyBank` class so a piggy bank protects its own coins.

## Class Specification

### PiggyBank

A `PiggyBank` object represents one piggy bank.

Each piggy bank stores:

- the owner's name (`owner`)
- protected coins (`_coins`)

## Required Methods

### PiggyBank.__init__(owner, starting_coins)

Store the owner's name as `owner`. Store the starting coins as a protected
attribute `_coins`.

### PiggyBank.get_coins()

Return the protected `_coins`.

### PiggyBank.add_coins(coins)

If `coins` is greater than `0`, add `coins` to `_coins`. Otherwise do nothing.

### PiggyBank.take_coins(coins)

If `coins` is greater than `0` and less than or equal to `_coins`, subtract
`coins` from `_coins`. Otherwise do nothing.

## Constraints

- owner is a non-empty string
- starting_coins is a non-negative integer
- add_coins and take_coins amounts are integers
- a take that exceeds the coins is ignored
- amounts of zero or less are ignored

All inputs are valid integers.

## Example

```python
bank = PiggyBank("Ada", 1000)

print(bank.owner)
print(bank.get_coins())

bank.add_coins(500)
print(bank.get_coins())

bank.take_coins(300)
print(bank.get_coins())
```

Output

```text
Ada
1000
1500
1200
```

## Explanation

The piggy bank starts with `1000` coins. After adding `500`, the coins are
`1500`. After taking `300`, the coins are `1200`. The coins are protected:
they only change through `add_coins` and `take_coins`, so they can never
become negative.

## Hint

Protect the coins with a leading underscore (`_coins`). Read it with
`get_coins`, and change it only inside `add_coins` and `take_coins`.

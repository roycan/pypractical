# Bank Account

## Story

A bank must keep every account safe. A bank account must never go below zero and
must ignore invalid deposits or withdrawals.

The balance is protected inside the object. It is read with `get_balance` and
changed only through `deposit` and `withdraw`.

## Task

Complete the `BankAccount` class so an account protects its own balance.

## Class Specification

### BankAccount

A `BankAccount` object represents one bank account.

Each account stores:

- the owner's name (`owner`)
- a protected balance (`_balance`)

## Required Methods

### BankAccount.__init__(owner, starting_balance)

Store the owner's name as `owner`. Store the starting balance as a protected
attribute `_balance`.

### BankAccount.get_balance()

Return the protected `_balance`.

### BankAccount.deposit(amount)

If `amount` is greater than `0`, add `amount` to `_balance`. Otherwise do
nothing.

### BankAccount.withdraw(amount)

If `amount` is greater than `0` and less than or equal to `_balance`, subtract
`amount` from `_balance`. Otherwise do nothing.

## Constraints

- owner is a non-empty string
- starting_balance is a non-negative integer
- deposit and withdraw amounts are integers
- a withdrawal that exceeds the balance is ignored
- amounts of zero or less are ignored

All inputs are valid integers.

## Example

```python
account = BankAccount("Ada", 1000)

print(account.owner)
print(account.get_balance())

account.deposit(500)
print(account.get_balance())

account.withdraw(300)
print(account.get_balance())
```

Output

```text
Ada
1000
1500
1200
```

## Explanation

The account starts with a balance of `1000`. After depositing `500`, the
balance is `1500`. After withdrawing `300`, the balance is `1200`. The balance
is protected: it only changes through `deposit` and `withdraw`, so it can
never become negative.

## Hint

Protect the balance with a leading underscore (`_balance`). Read it with
`get_balance`, and change it only inside `deposit` and `withdraw`.

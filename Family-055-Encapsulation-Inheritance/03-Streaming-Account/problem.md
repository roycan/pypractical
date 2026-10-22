# Streaming Account

## Story

A streaming service keeps track of its accounts. Every account has an email and
an owner. A premium account also has a maximum number of screens, and the
service must never record an account with zero or negative screens — that would
be garbage data.

## Task

The `Account` class is provided and complete. Do **not** modify it.

Complete the `PremiumAccount` class so a premium account inherits the account's
email and owner and protects its own screen limit.

## Class Specification

### Account (provided, do not modify)

An `Account` object represents one streaming account.

Each account stores:

- the account's email (`email`)
- the account's owner (`owner`)

### PremiumAccount

A `PremiumAccount` object represents one premium account. A premium account
IS-A account.

Each premium account should remember:

- the inherited account's email and owner
- a protected screen limit (`_max_screens`)

## Required Methods

### PremiumAccount.\_\_init\_\_(email, owner, max_screens)

Call `super().__init__(email, owner)` so the premium account inherits the email
and owner. Then assign the screen limit to `self.max_screens` so the setter
below validates and stores it.

### PremiumAccount.max_screens (property)

Use the `@property` decorator so callers read the limit as
`premium.max_screens` — no parentheses. Return the protected `_max_screens`.

### PremiumAccount.max_screens (setter)

Use the `@max_screens.setter` decorator. Validate the screen limit:

- if the value is zero or negative, print
  `"The number of screens must be positive"` and store `0` as the placeholder
  meaning "not recorded"
- otherwise store the value in the protected attribute `_max_screens`

## Constraints

- email is a non-empty string
- owner is a non-empty string
- max_screens is an integer (it may be zero or negative — the constructor must
  handle that case)

## Example

```python
account = Account("ada@mail.com", "Ada")
print(account.display_info())

premium = PremiumAccount("ben@mail.com", "Ben", 4)
print(premium.display_info())
print(premium.max_screens)

bad_premium = PremiumAccount("cy@mail.com", "Cy", -1)
print(bad_premium.max_screens)
```

Output

```text
Email: ada@mail.com, Owner: Ada
Email: ben@mail.com, Owner: Ben
4
The number of screens must be positive
0
```

## Explanation

`account` is a plain `Account`. The `premium` is a `PremiumAccount`, so it is
also an account: its `email` and `owner` come from the parent through
`super().__init__(email, owner)`, and its `display_info()` is the parent's
method, reused unchanged. The screen limit is protected: `premium.max_screens`
reads it through the `@property` getter, and the `@max_screens.setter` validates
every value before it is stored. `bad_premium` is given a negative screen limit,
so the setter prints a warning and stores the placeholder `0` — its data is
rejected, not silently kept.

## Hint

Write `class PremiumAccount(Account):` so the premium account inherits from the
parent. In `__init__`, call `super().__init__(email, owner)` first, then assign
`self.max_screens = max_screens` so the setter runs. Decorate the getter with
`@property` and the setter with `@max_screens.setter`. In the setter, check the
value with `<= 0` before storing it in `self._max_screens` — zero screens is
garbage data too.

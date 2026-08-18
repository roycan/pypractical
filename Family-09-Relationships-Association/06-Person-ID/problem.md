# Person ID

## Story

A person carries exactly one ID card. A person and their ID card are linked
one-to-one — each person has one card, and each card belongs to one person.

## Task

The `IDCard` class is provided and complete. Do **not** modify it.

Complete the `Person` class so a person can set an ID card, return the card
itself, and report the card's number.

## Class Specification

### IDCard (provided, do not modify)

An `IDCard` object represents one identification card.

It stores:

- the ID number (`id_number`)

It provides `get_number` (returns the ID number).

### Person

A `Person` object represents one person.

It stores:

- the person's name (`name`)
- an ID card (`id_card`)

Initially the person has no ID card (`None`).

## Required Methods

### Person.__init__(name)

Store the person's name and set `id_card` to `None`.

### Person.set_id_card(card)

Store the given `IDCard` object.

### Person.get_id_card()

Return the stored `IDCard`, or `None` if there is none.

### Person.get_id_number()

If the person has an ID card, return its number. Otherwise return the string
`"No ID"`.

## Constraints

- name is a non-empty string
- id_number is a non-empty string
- All inputs are valid

## Example

```python
person = Person("Ada")
print(person.get_id_number())

person.set_id_card(IDCard("A-1001"))
print(person.get_id_number())
print(person.get_id_card().get_number())
```

Output

```text
No ID
A-1001
A-1001
```

## Explanation

A new `Person` has no card, so `get_id_number` returns `"No ID"`. After
`set_id_card`, the person holds one `IDCard`, so `get_id_number` returns
`"A-1001"` and `get_id_card().get_number()` returns the same value. One person,
one card: that is a one-to-one association. If a card is set again, it replaces
the previous one.

## Hint

In `get_id_number`, check whether `self.id_card` is `None`. If it is, return the
string `"No ID"`. Otherwise return `self.id_card.get_number()`.
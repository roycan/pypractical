# Animal Bird

## Story

Every bird is an animal. The `Animal` class stores a name and species. A bird
inherits everything an animal has and adds a wingspan — the distance from
wingtip to wingtip in centimeters.

## Task

The `Animal` class is provided and complete. Do **not** modify it.

Complete the `Bird` class so a bird inherits `get_name` and `get_species` from
`Animal` and also stores a `wingspan`.

## Class Specification

### Animal (provided, do not modify)

An `Animal` object represents one animal.

Each animal stores:

- the animal's name (`name`)
- the animal's species (`species`)

### Bird

A `Bird` object represents one bird.

Each bird should remember:

- the inherited animal's name and species
- a wingspan (`wingspan`)

## Required Methods

### Bird.__init__(name, species, wingspan)

Call `super().__init__(name, species)` to reuse the parent, then store the
bird's `wingspan`.

### Bird.get_wingspan()

Return the bird's `wingspan`.

### Bird.describe()

Return a string in the format `"name is a species with a wingspan cm wingspan"`.

For example, `"Tweety is a canary with a 25 cm wingspan"`.

## Constraints

- name is a non-empty string
- species is a non-empty string
- wingspan is a positive integer

All inputs are valid.

## Example

```python
bird = Bird("Tweety", "canary", 25)
print(bird.get_name())
print(bird.get_species())
print(bird.get_wingspan())
print(bird.describe())
```

Output

```text
Tweety
canary
25
Tweety is a canary with a 25 cm wingspan
```

## Explanation

A `Bird` inherits `get_name` and `get_species` from `Animal`, so
`bird.get_name()` returns `"Tweety"` and `bird.get_species()` returns `"canary"`
even though `Bird` does not define those methods. `Bird` adds its own
`wingspan`, returned by `get_wingspan`. The `describe` method builds a sentence
using all three values. That is inheritance: the child reuses the parent and
adds something new.

## Hint

In the child `__init__`, call `super().__init__(name, species)` to reuse the
parent, then set the new attribute with `self.wingspan = wingspan`. In
`describe`, build the string using f-strings or concatenation.
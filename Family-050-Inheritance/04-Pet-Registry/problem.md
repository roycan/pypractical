# Pet Registry

## Story

Every pet is also an animal. The `Animal` class has already been written and
stores an animal's species and age.

A pet inherits the animal's species and age, and adds an owner.

## Task

The `Animal` class is provided and complete. Do **not** modify it.

Complete the `Pet` class so a pet inherits `get_species` and `get_age` from
`Animal` and also stores an `owner`.

## Class Specification

### Animal (provided, do not modify)

An `Animal` object represents one basic animal.

Each animal stores:

- the animal's species (`species`)
- the animal's age (`age`)

### Pet

A `Pet` object represents one animal that has an owner.

Each pet should remember:

- the inherited animal's species and age
- an owner (`owner`)

## Required Methods

### Pet.__init__(species, age, owner)

Call `super().__init__(species, age)` to reuse the parent, then store the
pet's `owner`.

### Pet.get_owner()

Return the pet's `owner`.

## Constraints

- species is a non-empty string
- age is a positive integer
- owner is a non-empty string

All inputs are valid.

## Example

```python
animal = Animal("Dog", 3)
print(animal.get_species())
print(animal.get_age())

pet = Pet("Cat", 2, "Ada")
print(pet.get_species())
print(pet.get_age())
print(pet.get_owner())
```

Output

```text
Dog
3
Cat
2
Ada
```

## Explanation

A `Pet` inherits `get_species` and `get_age` from `Animal`, so
`pet.get_species()` returns `"Cat"` and `pet.get_age()` returns `2` even though
`Pet` does not define those methods. `Pet` adds its own `owner`, returned by
`get_owner`. That is inheritance: the child reuses the parent and adds
something new.

## Hint

In the child `__init__`, call `super().__init__(species, age)` to reuse the
parent, then set the new attribute with `self.owner = owner`.

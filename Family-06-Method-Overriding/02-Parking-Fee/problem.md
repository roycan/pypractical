# Parking Fee

## Story

A truck pays a higher parking fee than a standard vehicle. The `Vehicle` class
has already been written and stores a vehicle's name and the number of hours
parked.

A standard vehicle pays `5` per hour. A truck pays `8` per hour.

## Task

The `Vehicle` class is provided and complete. Do **not** modify it.

Complete the `Truck` class so it inherits the vehicle's data and OVERRIDES the
`fee` method with the truck rate.

## Class Specification

### Vehicle (provided, do not modify)

A `Vehicle` object represents one standard vehicle.

Each vehicle stores:

- the vehicle's name (`name`)
- the number of hours parked (`hours`)

### Truck

A `Truck` object represents one vehicle that pays a higher parking fee.

A truck inherits the vehicle's name and hours.

## Required Methods

### Truck.__init__(name, hours)

Call `super().__init__(name, hours)` to reuse the parent's data.

### Truck.fee()

Return the truck parking fee: `self.hours * 8`. This method OVERRIDES the
parent's `fee` method.

## Constraints

- name is a non-empty string
- hours is a positive integer

All inputs are valid.

## Example

```python
vehicle = Vehicle("Sedan", 4)
print(vehicle.get_name())
print(vehicle.fee())

truck = Truck("Lorry", 4)
print(truck.get_name())
print(truck.fee())
```

Output

```text
Sedan
20
Lorry
32
```

## Explanation

Both vehicles park for `4` hours. A standard vehicle pays `4 * 5 = 20`. A truck
OVERRIDES the `fee` method, so `truck.fee()` uses the truck rate `4 * 8 = 32`
instead. Same method name, different behavior in the child — that is method
overriding.

## Hint

In the child, call `super().__init__(name, hours)` to reuse the parent's data,
then write a `fee` method with the truck rate `self.hours * 8` to override the
parent's version.

# Rental Cost

## Story

A power tool costs more to rent per day than a standard hand tool. The `Tool`
class has already been written and stores a tool's name and the number of days
rented.

A standard tool costs `10` per day. A power tool costs `15` per day.

## Task

The `Tool` class is provided and complete. Do **not** modify it.

Complete the `PowerTool` class so it inherits the tool's data and OVERRIDES the
`cost` method with the power-tool rate.

## Class Specification

### Tool (provided, do not modify)

A `Tool` object represents one standard tool.

Each tool stores:

- the tool's name (`name`)
- the number of days rented (`days`)

### PowerTool

A `PowerTool` object represents one tool rented at the power-tool rate.

A power tool inherits the tool's name and days.

## Required Methods

### PowerTool.__init__(name, days)

Call `super().__init__(name, days)` to reuse the parent's data.

### PowerTool.cost()

Return the power-tool rental cost: `self.days * 15`. This method OVERRIDES the
parent's `cost` method.

## Constraints

- name is a non-empty string
- days is a positive integer

All inputs are valid.

## Example

```python
tool = Tool("Hammer", 3)
print(tool.get_name())
print(tool.cost())

power = PowerTool("Hammer", 3)
print(power.get_name())
print(power.cost())
```

Output

```text
Hammer
30
Hammer
45
```

## Explanation

Both tools are rented for `3` days. A standard tool costs `3 * 10 = 30`. A power
tool OVERRIDES the `cost` method, so `power.cost()` uses the power-tool rate
`3 * 15 = 45` instead. Same method name, different behavior in the child — that
is method overriding.

## Hint

In the child, call `super().__init__(name, days)` to reuse the parent's data,
then write a `cost` method with the power-tool rate `self.days * 15` to override
the parent's version.

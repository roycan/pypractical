# Internet Cafe Daily Report

## Story

An internet cafe offers two payment plans.

- **Hourly Plan:** The customer pays **R × H** pesos, where:
  - `R` is the cost per hour.
  - `H` is the number of hours used.
- **Day Pass:** The customer pays **P** pesos regardless of how many hours they
  use a computer.

At the end of the day, the cafe manager wants to know the **total revenue**
collected from all customers.

For each customer, charge the smaller of the hourly fee and the day pass fee.

## Task

Write a function named `calculate_daily_revenue(usage_hours, hourly_rate, day_pass_fee)`.

The function should calculate the total amount collected from all customers.

## Function Specification

### Parameters

- `usage_hours` (list of integers)
  - The number of hours each customer used a computer.
- `hourly_rate` (int)
  - The cost per hour.
- `day_pass_fee` (int)
  - The unlimited-use day pass fee.

### Returns

- Returns one integer: the total revenue collected.

## Constraints

- 1 ≤ number of customers ≤ 100
- 1 ≤ hours used ≤ 24
- 1 ≤ hourly rate ≤ 100
- 1 ≤ day pass fee ≤ 2000

All input values are integers.

## Example

```python
usage_hours = [2, 6, 4, 8]

print(calculate_daily_revenue(usage_hours, 60, 300))
```

Output

```text
960
```

## Explanation

For each customer, the cafe charges the smaller of the hourly fee and the
day pass fee.

| Hours | Hourly Fee | Day Pass | Charged |
|------:|-----------:|---------:|--------:|
| 2     | 120        | 300      | 120     |
| 6     | 360        | 300      | 300     |
| 4     | 240        | 300      | 240     |
| 8     | 480        | 300      | 300     |

Total revenue:

```text
120 + 300 + 240 + 300 = 960
```

## Hint

Repeat the following steps for every customer:

1. Compute the hourly fee.
2. Compare it with the day pass fee.
3. Add the cheaper fee to the total.

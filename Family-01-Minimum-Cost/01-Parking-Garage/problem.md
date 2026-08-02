# Parking Garage Daily Report

## Story

A parking garage offers two payment plans.

- **Hourly Plan:** The customer pays **A × T** yen, where:
  - `A` is the hourly parking rate.
  - `T` is the number of hours parked.
- **Fixed Plan:** The customer pays **B** yen regardless of how many hours they parked.

At the end of the day, the parking manager wants to know the **total revenue**
collected from all customers.

For each customer, charge the smaller of the hourly fee and the fixed fee.

## Task

Write a function named `calculate_total_revenue(customers, hourly_rate, fixed_rate)`.

The function should calculate the total amount collected from all customers.

## Function Specification

### Parameters

- `customers` (list of integers)
  - The number of hours each customer parked.
- `hourly_rate` (int)
  - The cost per hour.
- `fixed_rate` (int)
  - The fixed parking fee.

### Returns

- Returns one integer: the total revenue collected.

## Constraints

- 1 ≤ number of customers ≤ 100
- 1 ≤ hours parked ≤ 20
- 1 ≤ hourly rate ≤ 100
- 1 ≤ fixed fee ≤ 2000

All input values are integers.

## Example

```python
customers = [5, 3, 8, 2, 10]

print(calculate_total_revenue(customers, 100, 450))
```

Output

```text
1850
```

## Explanation

For each customer, the garage charges the smaller of the hourly fee and the
fixed fee.

| Hours | Hourly Fee | Fixed Fee | Charged |
|------:|-----------:|----------:|--------:|
| 5     | 500        | 450       | 450     |
| 3     | 300        | 450       | 300     |
| 8     | 800        | 450       | 450     |
| 2     | 200        | 450       | 200     |
| 10    | 1000       | 450       | 450     |

Total revenue:

```text
450 + 300 + 450 + 200 + 450 = 1850
```

## Hint

Repeat the following steps for every customer:

1. Compute the hourly fee.
2. Compare it with the fixed fee.
3. Add the cheaper fee to the total.

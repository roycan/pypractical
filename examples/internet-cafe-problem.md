# Internet Café Daily Report

An Internet café offers two payment plans.

- **Hourly Plan:** A customer pays **hourly_rate × hours_used** pesos.
- **Day Pass:** A customer pays **day_pass_fee** pesos regardless of how many hours they use the computer.

At the end of the day, the café manager wants to know the **total revenue** collected from all customers.

For each customer, always charge the **cheaper** of the two payment plans.

---

## Task

Write a function named

```python
calculate_daily_revenue(usage_hours, hourly_rate, day_pass_fee)
```

that calculates the total amount collected from all customers.

---

## Parameters

### usage_hours

A list of integers representing the number of hours each customer used a computer.

### hourly_rate

The cost per hour.

### day_pass_fee

The fixed fee for unlimited computer use for one day.

---

## Returns

Return one integer:

- the total revenue collected for the day.

---

## Example

```python
usage_hours = [2, 6, 4, 8]

print(
    calculate_daily_revenue(
        usage_hours,
        60,
        300
    )
)
```

Output

```
960
```

### Explanation

| Hours | Hourly Cost | Day Pass | Charged |
|-------:|------------:|---------:|--------:|
|2|120|300|120|
|6|360|300|300|
|4|240|300|240|
|8|480|300|300|

Total Revenue

```
120 + 300 + 240 + 300 = 960
```

---

## Hint

For every customer:

1. Compute the hourly cost.
2. Compare it with the day pass fee.
3. Add the cheaper amount to the total revenue.

---

## Constraints

- 1 ≤ number of customers ≤ 100
- 1 ≤ hours used ≤ 24
- 1 ≤ hourly rate ≤ 100
- 1 ≤ day pass fee ≤ 2000

All values are integers.
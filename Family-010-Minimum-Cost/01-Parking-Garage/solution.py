"""Parking Garage Daily Report -- Family 01, Assessment 01 (teacher solution)."""


def calculate_total_revenue(customers, hourly_rate, fixed_rate):
    """Calculate the total parking revenue for all customers.

    Args:
        customers (list[int]): Number of hours parked for each customer.
        hourly_rate (int): Hourly parking fee.
        fixed_rate (int): Fixed parking fee.

    Returns:
        int: Total revenue collected.
    """
    total = 0

    for hours in customers:
        hourly_fee = hours * hourly_rate

        # Charge the smaller of the hourly fee and the fixed fee.
        if hourly_fee < fixed_rate:
            total = total + hourly_fee
        else:
            total = total + fixed_rate

    return total


if __name__ == "__main__":
    customers = [5, 3, 8, 2, 10]
    revenue = calculate_total_revenue(customers, 100, 450)
    print(revenue)

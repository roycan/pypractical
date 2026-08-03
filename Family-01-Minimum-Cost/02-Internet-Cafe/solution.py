"""Internet Cafe Daily Report -- Family 01, Assessment 02 (teacher solution)."""


def calculate_daily_revenue(usage_hours, hourly_rate, day_pass_fee):
    """Calculate the total revenue earned by the internet cafe.

    Args:
        usage_hours (list[int]): Hours used by each customer.
        hourly_rate (int): Cost per hour.
        day_pass_fee (int): Unlimited-use day pass fee.

    Returns:
        int: Total revenue collected.
    """
    total = 0

    for hours in usage_hours:
        hourly_fee = hours * hourly_rate

        # Charge the smaller of the hourly fee and the day pass fee.
        if hourly_fee < day_pass_fee:
            total = total + hourly_fee
        else:
            total = total + day_pass_fee

    return total


if __name__ == "__main__":
    usage_hours = [2, 6, 4, 8]
    revenue = calculate_daily_revenue(usage_hours, 60, 300)
    print(revenue)

"""
Program: Nested if statement - Module 4
Author: Ryan Blankenship
Last date modified: 09/18/2019
The purpose of this program is to
calculate the price of an item after
deducting coupons, then adding tax
and shipping costs.
"""


def calculate_price(price, cash_coupon, percent_coupon):
    TAX = 0.06
    TEN_OR_LESS_SHIPPING = 5.95
    TEN_UP_TO_THIRTY_SHIPPING = 7.95
    THIRTY_UP_TO_FIFTY = 11.95
    FIFTY_OR_OVER = 0.00

    total_after_cash_coupon = price - cash_coupon
    total_after_percent_coupon = total_after_cash_coupon * percent_coupon
    total_after_percent_coupon = total_after_cash_coupon - total_after_percent_coupon
    total_to_add_to_tax = total_after_percent_coupon * TAX
    total_after_tax = total_after_percent_coupon + total_to_add_to_tax
    if total_after_tax < 10.00:
        total = total_after_tax + TEN_OR_LESS_SHIPPING
    elif total_after_tax >= 10.00 or total_after_tax < 30.00:
        total = total_after_tax + TEN_UP_TO_THIRTY_SHIPPING
    # elif total_after_tax >= 30.00 or total_after_tax < 50.00:
    #     total = total_after_tax + THIRTY_UP_TO_FIFTY
    # else:
    #     total = total_after_tax + FIFTY_OR_OVER
    return round(total, 2)


if __name__ == '__main__':
    price_of_item = 35.00
    cash_pon = 10.00
    percent_pon = .10
    net_total = calculate_price(price_of_item, cash_pon, percent_pon)
    print(net_total)

import unittest
from store import coupon_calculations


class MyTestCase(unittest.TestCase):
    # Test Set1

    def test_ten_or_less_shipping_test1(self):
        self.assertEqual(coupon_calculations.calculate_price(8.50, 5.00, .10), 9.29)

    def test_ten_or_less_shipping_test2(self):
        self.assertEqual(coupon_calculations.calculate_price(7.50, 5.00, .15), 8.2)

    def test_ten_or_less_shipping_test3(self):
        self.assertEqual(coupon_calculations.calculate_price(6.50, 5.00, .20), 7.22)

    def test_ten_or_less_shipping_test4(self):
        self.assertEqual(coupon_calculations.calculate_price(8.50, 10.00, .10), 4.52)

    def test_ten_or_less_shipping_test5(self):
        self.assertEqual(coupon_calculations.calculate_price(7.50, 10.00, .15), 3.7)

    def test_ten_or_less_shipping_test6(self):
        self.assertEqual(coupon_calculations.calculate_price(6.50, 10.00, .20), 2.98)

    # Test Set2

    def test_ten_up_to_thirty_test1(self):
        self.assertEqual(coupon_calculations.calculate_price(27.50, 5.00, .10), 29.41)

    def test_ten_up_to_thirty_test2(self):
        self.assertEqual(coupon_calculations.calculate_price(26.50, 5.00, .15), 27.32)

    def test_ten_up_to_thirty_test3(self):
        self.assertEqual(coupon_calculations.calculate_price(25.50, 5.00, .20), 25.33)

    def test_ten_up_to_thirty_test4(self):
        self.assertEqual(coupon_calculations.calculate_price(27.50, 10.00, .10), 24.64)

    def test_ten_up_to_thirty_test5(self):
        self.assertEqual(coupon_calculations.calculate_price(26.50, 10.00, .15), 22.82)

    def test_ten_up_to_thirty_test6(self):
        self.assertEqual(coupon_calculations.calculate_price(25.50, 10.00, .20), 21.09)

    # # Test Set3
    #
    # def test_thirty_up_to_fifty_test1(self):
    #     self.assertEqual(coupon_calculations.calculate_price(42.50, 5.00, .10), 43.73)
    #
    # def test_thirty_up_to_fifty_test2(self):
    #     self.assertEqual(coupon_calculations.calculate_price(40.50, 5.00, .15), 39.94)
    #
    # def test_thirty_up_to_fifty_test3(self):
    #     self.assertEqual(coupon_calculations.calculate_price(38.50, 5.00, .20), 36.36)
    #
    # def test_thirty_up_to_fifty_test4(self):
    #     self.assertEqual(coupon_calculations.calculate_price(42.50, 10.00, .10), 38.95)
    #
    # def test_thirty_up_to_fifty_test5(self):
    #     self.assertEqual(coupon_calculations.calculate_price(40.50, 10.00, .15), 35.43)
    #
    # def test_thirty_up_to_fifty_test6(self):
    #     self.assertEqual(coupon_calculations.calculate_price(38.50, 10.00, .20), 32.12)
    #
    # # Test Set4
    #
    # def test_fifty_or_over_test1(self):
    #     self.assertEqual(coupon_calculations.calculate_price(75.00, 5.00, .10), 74.73)
    #
    # def test_fifty_or_over_test2(self):
    #     self.assertEqual(coupon_calculations.calculate_price(75.00, 5.00, .15), 71.02)
    #
    # def test_fifty_or_over_test3(self):
    #     self.assertEqual(coupon_calculations.calculate_price(75.00, 5.00, .20), 67.31)
    #
    # def test_fifty_or_over_test4(self):
    #     self.assertEqual(coupon_calculations.calculate_price(75.00, 10.00, .10), 69.96)
    #
    # def test_fifty_or_over_test5(self):
    #     self.assertEqual(coupon_calculations.calculate_price(75.00, 10.00, .15), 66.52)
    #
    # def test_fifty_or_over_test6(self):
    #     self.assertEqual(coupon_calculations.calculate_price(75.00, 10.00, .20), 63.07)


if __name__ == '__main__':
    unittest.main()

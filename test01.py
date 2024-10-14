import unittest
from dz_test01 import calculate_remainder


class TestCalculateRemainder(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_remainder(10, 3), 1)

    def test_negative_numbers(self):
        self.assertEqual(calculate_remainder(-10, 3), -1)

    def test_division_by_zero(self):
        self.assertEqual(calculate_remainder(10, 0), "Ошибка: Делить на ноль нельзя")

    def test_zero_dividend(self):
        self.assertEqual(calculate_remainder(0, 3), 0)

    def test_equal_dividend_and_divisor(self):
        self.assertEqual(calculate_remainder(5, 5), 0)

if __name__ == "__main__":
    unittest.main()

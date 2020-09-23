import unittest
import random
import datetime
from simple_calculator import Calculator, fun

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(random.randint(1,100))

    def test_add(self):
        calc_value = self.calculator.value + 1 + 2 + 3
        self.assertEqual(calc_value, self.calculator.add(1, 2, 3).value)

    def test_mul(self):
        calc_value = self.calculator.value * 5 * 2 * 90
        self.assertEqual(calc_value, self.calculator.multiply(5, 2, 90).value)

    def test_divide(self):
        calc_value = self.calculator.value / 2 / 3
        self.assertEquals(calc_value, self.calculator.divide(2, 3).value)

    def kek(self):
        self.assertEqual(1, 2)


if __name__ == '__main__':
    print("Start of the test",datetime.datetime.now())
    unittest.main()
    print("End of the test", datetime.datetime.now())



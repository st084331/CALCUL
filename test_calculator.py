import unittest
import random
import datetime
from math import sqrt
from simple_calculator import Calculator, fun

class TestCalculator(unittest.TestCase):
    print("Start of the test", datetime.datetime.now())
    def setUp(self):
        self.calculator = Calculator(random.randint(1,100))

    def test_add(self):
        calc_value = self.calculator.value + 6
        self.assertEqual(calc_value, self.calculator.add(1, 2, 3).value)

    def test_subtract(self):
        calc_value = self.calculator.value - 2
        self.assertEqual(calc_value, self.calculator.subtract(1, 1).value)

    def test_mul(self):
        calc_value = self.calculator.value * 900
        self.assertEqual(calc_value, self.calculator.multiply(5, 2, 90).value)

    def test_divide(self):
        calc_value = self.calculator.value/6
        self.assertEquals(calc_value, self.calculator.divide(6).value)

    def test_pow_and_root(self):
        calc_value = sqrt(self.calculator.value ** 4)
        self.assertEqual(calc_value, self.calculator.power(4).root().value)

    def test_chain(self):
        calc_value = (((sqrt(self.calculator.value**2)) + 12 - 33)*10)/2
        self.assertEqual(calc_value, self.calculator.power(2).root().add(4,8).subtract(11,22).multiply(5,2).divide(2).value)

    def kek(self):
        self.assertEqual(1, 2)
    print("End of the test", datetime.datetime.now())


if __name__ == '__main__':
    unittest.main()




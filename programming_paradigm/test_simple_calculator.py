import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calculator.add(5, 5), 10)
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(7,3),4)
    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(3,5),15)
    def test_division(self):
        self.assertEqual(self.calculator.divide(10,5),2)
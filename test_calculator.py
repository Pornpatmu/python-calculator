import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1),0)
        self.assertEqual(self.calc.add(-1, -1), -2)


    # Add the following test methods to the TestCalculator class:

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 1),4)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(3, 3), 0)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, -5), -5)


        

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 1),5)
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5),2)
        self.assertEqual(self.calc.divide(15, 5),3)
        self.assertEqual(self.calc.divide(10, 0), 'Cannot divide by zero')

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(0, 3), 0)
        self.assertEqual(self.calc.modulo(10, 0), 'Division by 0 is undefined') 

if __name__ == '__main__':
    unittest.main()
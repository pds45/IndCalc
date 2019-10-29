import unittest
from Calc import Calc


class MyTestCase(unittest.TestCase):

    def test_instantiate_calc(self):
        calc = Calc()
        self.assertIsInstance(calc, Calc)

    def test_results_property_calc(self):
        calc = Calc()
        self.assertEqual(calc.result, 0)

    def test_add_method_calc(self):
        calc = Calc()
        self.assertEqual(calc.add(2, 2), 4)
        self.assertEqual(calc.result, 4)

    def test_subtract_method_calc(self):
        calc = Calc()
        self.assertEqual(calc.subtract(2, 2), 0)
        self.assertEqual(calc.result, 0)

if __name__ == '__main__':
    unittest.main()
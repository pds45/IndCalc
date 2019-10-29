import unittest
from Calc import Calc


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calc()

    def test_instantiate_calc(self):
        self.assertIsInstance(self.calc, Calc)

    def test_results_property_calc(self):
        self.assertEqual(self.calc.result, 0)

    def test_add_method_calc(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.result, 4)

    def test_subtract_method_calc(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.result, 0)

    def test_mul_method_calc(self):
        self.assertEqual(self.calc.mul(2, 2), 4)
        self.assertEqual(self.calc.result, 4)

if __name__ == '__main__':
    unittest.main()

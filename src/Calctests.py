import unittest
from Calc import Calc


class MyTestCase(unittest.TestCase):

    def test_instantiate_calc(self):
        calc = Calc()
        self.assertIsInstance(calc, Calc)

    def test_results_property_calc(self):
        calc = Calc()
        self.assertEqual(calc.result, 4)


if __name__ == '__main__':
    unittest.main()

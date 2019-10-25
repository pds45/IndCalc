import unittest
from calc import calc

class MyTestCase(unittest.TestCase):

    def test_instantiate_Calc(self):
        Calc = calc()
        self.assertIsInstance(Calc,calc)


if __name__ == '__main__':
    unittest.main()
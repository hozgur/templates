import unittest
from math_ops_cpp import add, mul

class TestMathOps(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)

if __name__ == '__main__':
    unittest.main() 
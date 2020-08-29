import unittest

from calc import *

fun = Calc()

class MyTest(unittest.TestCase):
    def testMin(self):
        self.assertEqual(fun.minimum([1, 2, 3]), 1)
        self.assertEqual(fun.minimum([2, 3, 4]), 2)
        self.assertEqual(fun.minimum([-1, 3, 7, 9999]), -1)

    def testMax(self):
        self.assertEqual(fun.maximum([1, 2, 3]), 3)
        self.assertEqual(fun.maximum([2, 3, 4]), 4)
        self.assertEqual(fun.maximum([-1, 3, 7, 9999]), 9999)

    def testNumElements(self):
        self.assertEqual(fun.numElements([1, 2, 3]), 3)
        self.assertEqual(fun.numElements([1, 2]), 2)
        self.assertEqual(fun.numElements([]), 0)

    def testAvr(self):
        self.assertEqual(fun.average([1, 2, 3]), 2)
        self.assertEqual(fun.average([1, 2, 3, 4]), 2.5)
        self.assertEqual(fun.average([]), 0)


if __name__ == "__main__":
    unittest.main()
# 1("vvs20", true)
# 2("v", true)
# 3("vvs202", true)
# 4("20vvs", false)
# 5("vvs_20", false)
# 6("vvs2020", false)
# 7("", false)
# 8(null, false)

import unittest

from silly import *

fun = Silly()

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertTrue(fun.checkSilly("vvs20"))

    def test2(self):
        self.assertTrue(fun.checkSilly("v"))

    def test3(self):
        self.assertTrue(fun.checkSilly("vvs202"))

    def test4(self):
        self.assertFalse(fun.checkSilly("20vvs"))
    
    def test5(self):
        self.assertFalse(fun.checkSilly("vvs-20"))

    def test6(self):
        self.assertFalse(fun.checkSilly("vvs2020"))
    
    def test7(self):
        self.assertFalse(fun.checkSilly(""))
    
    def test8(self):
        self.assertFalse(fun.checkSilly(None))


if __name__ == "__main__":
    unittest.main()
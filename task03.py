import unittest
import base


class TestIsYearLeap(unittest.TestCase):

    def testZeroValue(self):
        res = base.is_year_leap(0)
        self.assertEqual(res, True)

    def testStrIn(self):
        res = base.is_year_leap("abc")
        self.assertIsNone(res)

    def testListIn(self):
        res = base.is_year_leap([1, 2])
        self.assertIsNone(res)

    def testNumInStr(self):
        res = base.is_year_leap("2000")
        self.assertEqual(res, True)

    def testMinus2000(self):
        res = base.is_year_leap(-2000)
        self.assertEqual(res, True)

    def testMinus999(self):
        res = base.is_year_leap(-999)
        self.assertEqual(res, False)

    def testFloat(self):
        res = base.is_year_leap(3.7)
        self.assertEqual(res, False)

    def test100(self):
        res = base.is_year_leap(100)
        self.assertEqual(res, False)

    def test400(self):
        res = base.is_year_leap(400)
        self.assertEqual(res, True)

    def test4(self):
        res = base.is_year_leap(4)
        self.assertEqual(res, True)

    def test3(self):
        res = base.is_year_leap(3)
        self.assertEqual(res, False)


class TestTriangle(unittest.TestCase):

    def testZeroValue(self):
        res = base.triangle(0, 0, 0)
        self.assertEqual(res, False)

    def testStrIn(self):
        res = base.triangle("abc", 7, 4)
        self.assertIsNone(res)

    def testListIn(self):
        res = base.triangle([1, 2], 11, 3)
        self.assertIsNone(res)

    def testMinusValue(self):
        res = base.triangle(-1, -2, -2.5)
        self.assertEqual(res, False)

    def testTrueValue(self):
        res = base.triangle(1, 2, 2.5)
        self.assertEqual(res, True)


class TestTrianglePlus(unittest.TestCase):

    def testZeroValue(self):
        res = base.triangle_plus(0, 0, 0)
        self.assertEqual(res, 'Not a triangle')

    def testStrIn(self):
        res = base.triangle_plus("abc", 7, 4)
        self.assertIsNone(res)

    def testListIn(self):
        res = base.triangle_plus([1, 2], 11, 3)
        self.assertIsNone(res)

    def testMinusValue(self):
        res = base.triangle_plus(-1, -2, -2.5)
        self.assertEqual(res, 'Not a triangle')

    def testVersatileValue(self):
        res = base.triangle_plus(1, 2, 2.5)
        self.assertEqual(res, 'Versatile triangle')

    def testIsoscelesValue(self):
        res = base.triangle_plus(1, 1, 1.5)
        self.assertEqual(res, 'Isosceles triangle')

    def testEquilateralValue(self):
        res = base.triangle_plus(7, 7, 7)
        self.assertEqual(res, 'Equilateral triangle')


if __name__ == '__main__':
    unittest.main()

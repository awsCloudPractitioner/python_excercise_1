import unittest
from ClassifyTriangle import ClassifyTriangle


class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral(tc):
        tc.assertTrue(ClassifyTriangle(sidelist=[10, 10, 10]).equilateral)
        tc.assertTrue(ClassifyTriangle(sidelist=[2.2, 2.2, 2.2]).equilateral)
        tc.assertFalse(ClassifyTriangle(sidelist=[20, 10, 10]).equilateral)
        tc.assertFalse(ClassifyTriangle(sidelist=[1.1, 2.2, 3.3]).equilateral)

    def test_isosceles(tc):
        tc.assertTrue(ClassifyTriangle(sidelist=[10, 20, 20]).isosceles)
        tc.assertTrue(ClassifyTriangle(sidelist=[3.5, 1.1, 3.5]).isosceles)
        tc.assertFalse(ClassifyTriangle(sidelist=[10, 20, 30]).isosceles)
        tc.assertFalse(ClassifyTriangle(sidelist=[2.5, 1, 1.2]).isosceles)

    def test_scalene(tc):
        tc.assertTrue(ClassifyTriangle(sidelist=[10, 20, 30]).scalene)
        tc.assertTrue(ClassifyTriangle(sidelist=[1.1, 2.2, 3.3]).scalene)
        tc.assertFalse(ClassifyTriangle(sidelist=[10, 20, 20]).scalene)
        tc.assertFalse(ClassifyTriangle(sidelist=[1.1, 2.2, 2.2]).scalene)

    def test_error(self):
        with self.assertRaises(Exception): ClassifyTriangle(sidelist=[-10, 20, 30]).equilateral
        with self.assertRaises(Exception): ClassifyTriangle(sidelist=[a, 20, 30]).equilateral


if __name__ == '__main__':
    unittest.main()

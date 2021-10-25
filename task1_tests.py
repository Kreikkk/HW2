from task1 import CoolList
import unittest


class AlgebraTest(unittest.TestCase):
    def setUp(self):
        self.l1 = CoolList([1, 2, 3, 4])
        self.l2 = CoolList([])
        self.l3 = [10, 20, 30]
        self.l4 = []
        self.l5 = [1, 2, 3, 4]

    def test_result(self):
        self.assertEqual(self.l1 - self.l2, CoolList([1, 2, 3, 4]))
        self.assertEqual(self.l3 - self.l1, CoolList([9, 18, 27, -4]))
        self.assertEqual(self.l1 - self.l3, CoolList([-9, -18, -27, 4]))
        self.assertEqual(self.l4 - self.l2, CoolList([]))
        self.assertEqual(self.l1 + self.l1, CoolList([2, 4, 6, 8]))
        self.assertEqual(self.l3 + self.l1, CoolList([11, 22, 33, 4]))
        self.assertEqual(self.l5 - self.l1, CoolList([0, 0, 0, 0]))


class CompareTrueTest(unittest.TestCase):
    def setUp(self):
        self.l1 = CoolList([1, 2, 3, 4])
        self.l2 = CoolList([0,])
        self.l3 = [10, 20, 30]
        self.l4 = []
        self.l5 = [2, -10, 18]

    def test_result(self):
        self.assertTrue(self.l1 == self.l5)
        self.assertTrue(self.l1 >= self.l5)
        self.assertTrue(self.l3 > self.l1)
        self.assertTrue(self.l4 <= self.l2)
        self.assertTrue(self.l2 < self.l3)
        self.assertTrue(self.l2 != self.l5)

class CompareFalseTest(unittest.TestCase):
    def setUp(self):
        self.l1 = CoolList([1, 2, 3, 4])
        self.l2 = CoolList([0])
        self.l3 = [10, 20, 30]
        self.l4 = []
        self.l5 = [2, -10, 18]

    def test_result(self):
        self.assertFalse(self.l2 > self.l1)
        self.assertFalse(self.l2 != self.l4)
        self.assertFalse(self.l3 < self.l1)
        self.assertFalse(self.l1 == self.l2)
        self.assertFalse(self.l1 <= self.l4)
        self.assertFalse(self.l5 < self.l1)



if __name__ == "__main__":
    unittest.main()

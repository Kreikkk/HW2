from task2 import CustomMeta
import unittest

class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

        def Foo():
            return True
        self.func = Foo

    def __add__(self, other):
        return 1

    def line(self):
        return 100


class AttributesTest(unittest.TestCase):
    def setUp(self):
        self.obj_1 = CustomClass()

    def test_result(self):
        self.assertFalse(hasattr(self.obj_1, "x"))
        self.assertFalse(hasattr(self.obj_1, "val"))
        self.assertFalse(hasattr(self.obj_1, "line"))

        self.assertTrue(hasattr(self.obj_1, "custom_x"))
        self.assertTrue(hasattr(self.obj_1, "custom_val"))
        self.assertTrue(hasattr(self.obj_1, "custom_line"))


if __name__ == "__main__":
    unittest.main()

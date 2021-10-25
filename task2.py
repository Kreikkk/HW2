from re import match
from types import FunctionType


class CustomMeta(type):
    def __call__(self, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)

        new = {}
        for key in dir(obj):
            if not match(r'^__\w(\w|\d)+__$', key):
                new[key] = getattr(obj, key)

        for key, val in new.items():
            try:
                delattr(self, key)
            except AttributeError:
                delattr(obj, key)

            setattr(obj, "custom_" + key, val)

        return obj


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
        

if __name__ == "__main__":

    inst = CustomClass(val=10)
    inst.custom_x
    inst.custom_val
    inst.custom_line()

    print(dir(inst))

    # inst.x  # ошибка
    # inst.val  # ошибка
    # inst.line() # ошибка
class CoolList(list):
    def __init__(self, values):
        self.extend(values)

    def __add__(self, other):
        ret = CoolList([])

        minlen = min((len(self), len(other)))

        for i, j in zip(self[:minlen], other[:minlen]):
            ret.append(i + j)

        ret.extend(self[minlen:])
        ret.extend(other[minlen:])

        return ret

    def __radd__(self, other):
        ret = CoolList([])

        minlen = min((len(self), len(other)))

        for i, j in zip(self[:minlen], other[:minlen]):
            ret.append(j + i)

        ret.extend(self[minlen:])
        ret.extend(other[minlen:])

        return ret

    def __sub__(self, other):
        ret = CoolList([])

        minlen = min((len(self), len(other)))

        for i, j in zip(self[:minlen], other[:minlen]):
            ret.append(i - j)

        ret.extend(self[minlen:])
        ret.extend([-item for item in other[minlen:]])

        return ret

    def __rsub__(self, other):
        ret = CoolList([])

        minlen = min((len(self), len(other)))

        for i, j in zip(self[:minlen], other[:minlen]):
            ret.append(j - i)

        ret.extend([-item for item in self[minlen:]])
        ret.extend(other[minlen:])

        return ret

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)


if __name__ == "__main__":
    l1 = CoolList([])
    l2 = CoolList([])

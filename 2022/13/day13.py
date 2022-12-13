import unittest
from functools import cmp_to_key
from numpy import sign


def read(filename):
    with open(filename) as f:
        return [(eval(l1), eval(l2)) for pair in f.read().split('\n\n') for l1, l2 in [pair.splitlines()]]

def log(param):
    # print(param)
    pass


def compare(left, right):
    match(left, right):
        case int(l), int(r):
            return sign(r - l)

        case [*l], int(r):
            return compare(l, [r])

        case int(l), [*r]:
            return compare([l], r)

        case [*l], [*r] if len(l) == 0 or len(r) == 0:
            return sign(len(r) - len(l))

        case [l, *lr], [r, *rr]:
            cmp = compare(l, r)
            return cmp if cmp != 0 else compare(lr, rr)

        case _:
            raise Exception("Unkonwn {} {}".format(left, right))

def part1(filename):
    pairs = read(filename)
    return sum(i+1 for i, (left, right) in enumerate(pairs) if compare(left, right) >= 0)

def part2(filename):
    pairs = read(filename)
    packets = [p for pair in pairs for p in pair]
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
    idx2 = sorted_packets.index([[2]])
    idx6 = sorted_packets.index([[6]])
    return (idx2+1) * (idx6+1)


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(13, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(5506, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(140, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(21756, part2('input.txt'))

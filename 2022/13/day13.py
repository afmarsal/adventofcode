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
    for i in range(len(left)):
        if i >= len(right):
            return -1

        if type(left[i]) == int and type(right[i]) == int:
            if left[i] != right[i]:
                return sign(right[i] - left[i])
            else:
                continue

        new_left = left[i]
        new_right = right[i]
        if type(left[i]) == int:
            new_left = [left[i]]
        if type(right[i]) == int:
            new_right = [right[i]]

        result = compare(new_left, new_right)
        if result != 0:
            return result

    # All elements equal: check length
    return 0 if len(left) == len(right) else 1

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

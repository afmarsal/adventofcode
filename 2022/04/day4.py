import unittest
import itertools as it

def read_ranges(filename):
    with open(filename) as f:
        return it.chain([line.split(",") for line in f.read().splitlines()])


def day1(filename):
    res = 0
    for rng1, rng2 in read_ranges(filename):
        start1, end1 = rng1.split("-")
        start2, end2 = rng2.split("-")
        new_range1 = set(range(int(start1), int(end1)+1))
        new_range2 = set(range(int(start2), int(end2)+1))
        if new_range1.issubset(new_range2) or new_range2.issubset(new_range1):
            res += 1
    return res

def day2(filename):
    res = 0
    for rng1, rng2 in read_ranges(filename):
        start1, end1 = rng1.split("-")
        start2, end2 = rng2.split("-")
        new_range1 = set(range(int(start1), int(end1)+1))
        new_range2 = set(range(int(start2), int(end2)+1))
        res += 1 if len(new_range1.intersection(new_range2)) > 0 else 0
    return res


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(2, day1('sample.txt'))

    def test_input(self):
        self.assertEqual(471, day1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(4, day2('sample.txt'))

    def test_input(self):
        self.assertEqual(888, day2('input.txt'))

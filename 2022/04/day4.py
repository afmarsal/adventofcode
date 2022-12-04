import unittest
import itertools as it


def read_ranges(filename):
    with open(filename) as f:
        return [(list(map(int, r1.split('-'))), list(map(int, r2.split('-'))))
                for r1, r2 in it.chain([line.split(",") for line in f.read().splitlines()])]

def day1(filename):
    return sum([int(p1[0] <= p2[0] <= p2[1] <= p1[1] or p2[0] <= p1[0] <= p1[1] <= p2[1])
                for p1, p2 in read_ranges(filename)])

def day2(filename):
    return sum([int(max(p1[0], p2[0]) <= min(p1[1], p2[1]))
                for p1, p2 in read_ranges(filename)])


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

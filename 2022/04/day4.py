import unittest
import itertools as it


def read_ranges(filename):
    with open(filename) as f:
        return [(list(map(int, r1.split('-'))), list(map(int, r2.split('-'))))
                for r1, r2 in it.chain([line.split(",") for line in f.read().splitlines()])]

def count_trues(filename, f):
    return [f(p1, p2) for p1, p2 in read_ranges(filename)].count(True)

def part1(filename):
    return count_trues(filename,
                       lambda p1, p2: p1[0] <= p2[0] <= p2[1] <= p1[1] or p2[0] <= p1[0] <= p1[1] <= p2[1])

def part2(filename):
    return count_trues(filename,
                       lambda p1, p2: max(p1[0], p2[0]) <= min(p1[1], p2[1]))


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(2, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(471, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(4, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(888, part2('input.txt'))

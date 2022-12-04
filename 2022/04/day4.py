import unittest
import itertools as it


def read_ranges(filename):
    to_set = lambda p: set(range(int(p[0]), int(p[1]) + 1))
    with open(filename) as f:
        return [(to_set(r1.split('-')), to_set(r2.split('-')))
                for r1, r2 in it.chain([line.split(",") for line in f.read().splitlines()])]

def day1(filename):
    return sum([int(rng1 >= rng2 or rng2 >= rng1) for rng1, rng2 in read_ranges(filename)])

def day2(filename):
    return sum([int(not rng1.isdisjoint(rng2)) for rng1, rng2 in read_ranges(filename)])


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(2, day1('sample.txt'))

    def test_input(self):
        self.assertEqual(471, day1('input.txt'))
        z


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(4, day2('sample.txt'))

    def test_input(self):
        self.assertEqual(888, day2('input.txt'))

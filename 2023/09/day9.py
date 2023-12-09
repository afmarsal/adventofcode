import unittest
import operator
import re
import functools
import operator as op
from collections import defaultdict
from pprint import pprint


def get_lines(filename):
    with open(filename) as f:
        return [[int(n) for n in l.strip().split()] for l in f.readlines()]


def log(param='', end='\n'):
    # print(param, end=end)
    pass


def log_nolf(param):
    log(param, end='')


def next_value(line):
    pyramid = [line]
    while any(pyramid[-1]):
        # Build next pyramid row
        pyramid.append([n2 - n1 for n1, n2 in zip(pyramid[-1], pyramid[-1][1:])])
    pyramid.reverse()
    # Add last value of each row in pyramid
    return functools.reduce(lambda x, y: x + y[-1], pyramid, 0)


def part1(filename):
    scan = get_lines(filename)
    return sum(next_value(line) for line in scan)


def part2(filename):
    scan = get_lines(filename)
    scan = [list(reversed(line)) for line in scan]
    return sum(next_value(line) for line in scan)


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(114, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(1938731307, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(948, part2('input.txt'))

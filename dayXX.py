import unittest
import operator
import re
import functools
import operator as op
from collections import defaultdict

def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')

def part1(filename):
    scan = get_lines(filename)
    return -1

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

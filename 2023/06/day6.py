import unittest
import operator
import re
import functools
import operator as op
from collections import defaultdict
from pprint import pprint

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
    times = [int(n.strip()) for n in scan[0].split(':')[1].split()]
    distances = [int(n.strip()) for n in scan[1].split(':')[1].split()]
    pprint(distances)
    res = 1
    for i in range(len(times)):
        ways = 0
        for m in range(times[i]):
            cur_dist = m * (times[i] - m)
            ways += 1 if cur_dist > distances[i] else 0
            log(f'Cur dist: {m} * {times[i] - m} = {cur_dist}. Res: {ways}')
        res *= ways

    return res

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(288, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(512295, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

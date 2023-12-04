import re
import unittest
import functools
import operator as op
from collections import defaultdict


def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


def part1(filename):
    lines = get_lines(filename)
    res = 0
    for line in lines:
        cards = line.split(':')[1]
        winners, numbers = cards.split('|')
        winners = {s.strip() for s in winners.split()}
        numbers = {s.strip() for s in numbers.split()}
        print(f'w: {winners}, n: {numbers}')
        combo = len(winners.intersection(numbers))
        print(f'c: {combo}')
        if combo > 0:
            res += pow(2, combo - 1)
    return res


def part2(filename):
    lines = get_lines(filename)



class TestAll(unittest.TestCase):
    def test_part1(self):
        f = 'sample.txt'
        self.assertEqual(13, part1(f))
        f = 'input.txt'
        self.assertEqual(19135, part1(f))

    def test_part2(self):
        f = 'sample.txt'
        self.assertEqual(467835, part2(f))
        f = 'input.txt'
        self.assertEqual(89471771, part2(f))


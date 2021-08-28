import itertools
import math
import operator
import unittest
import re
from collections import namedtuple, Counter

# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
regex = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'

to_find = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

def parse_input(lines):
    result = []
    for line in lines:
        m = re.match(r'Sue (\d+): (.*)', line)
        with_quotes = re.sub(r'([a-z]+)', r'"\1"', m[2])
        d = eval('{' + with_quotes + '}')
        result.append(d)
    return result


def solve(lines, match_func):
    sues = parse_input(lines)
    for i, sue in enumerate(sues):
        if all([match_func(sue, prop) for prop in sue]):
            return i + 1
    raise -1


def part1(lines):
    res = solve(lines, lambda sue, prop: sue[prop] == to_find[prop])
    return res


def part2(lines):
    def matches(sue, prop):
        if prop in {'cats', 'trees'}:
            return sue[prop] > to_find[prop]
        elif prop in {'pomeranians', 'goldfish'}:
            return sue[prop] < to_find[prop]
        else:
            return sue[prop] == to_find[prop]
    res = solve(lines, matches)
    return res


class TestPart1(unittest.TestCase):
    def test1(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part1(lines), 40)


class TestPart2(unittest.TestCase):
    def test2(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part2(lines), 241)


if __name__ == '__main__':
    unittest.main()

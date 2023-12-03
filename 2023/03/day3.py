import re
import unittest
import functools
import operator as op
from collections import defaultdict


def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


around = [(-1,-1), (-1, 0),(-1,1),
          (0,-1,),(0,1),
          (1,-1),(1,0),(1,1)]

def is_symbol(c):
    return c != '.' and not c.isdigit()

def has_adjacent_symbol(j, i, lines):
    for a in around:
        coord = list(map(op.add, a, (j, i)))
        if 0 <= coord[0] < len(lines) and 0 <= coord[1] < len(lines[i]):
            if is_symbol(lines[coord[0]][coord[1]]):
                return True
    return False


def part1(filename):
    lines = get_lines(filename)
    numbers = []
    for j, line in enumerate(lines):
        symbol_found = False
        cur_number = 0
        for i, c in enumerate(line):
            if c.isdigit():
                cur_number = cur_number * 10 + int(c)
                if not symbol_found and has_adjacent_symbol(j, i, lines):
                    print(f'Found symbol for {j},{i}. Cur num: {cur_number}')
                    symbol_found = True
            else:
                if symbol_found and cur_number > 0:
                    print(f'Adding number: {cur_number}')
                    numbers.append(cur_number)
                cur_number = 0
                symbol_found = False

        if symbol_found:
            print(f'Adding number: {cur_number}')
            numbers.append(cur_number)

    return sum(numbers)


def find_star(j, i, lines):
    for a in around:
        coord = tuple(map(op.add, a, (j, i)))
        if 0 <= coord[0] < len(lines) and 0 <= coord[1] < len(lines[i]):
            if lines[coord[0]][coord[1]] == '*':
                return coord
    return None


def part2(filename):
    lines = get_lines(filename)
    numbers_and_stars = defaultdict(list)
    for j, line in enumerate(lines):
        cur_number = 0
        cur_star = None
        for i, c in enumerate(line):
            if c.isdigit():
                cur_number = cur_number * 10 + int(c)
                if not cur_star:
                    coord = find_star(j, i, lines)
                    if coord:
                        print(f'Found star for {j},{i}. Cur num: {cur_number}')
                        cur_star = coord
            else:
                if cur_star and cur_number > 0:
                    print(f'Adding number for star: {cur_star} -> {cur_number}')
                    numbers_and_stars[cur_star].append(cur_number)
                cur_number = 0
                cur_star = None

        if cur_star and cur_number > 0:
            print(f'Adding number for star: {cur_star} -> {cur_number}')
            numbers_and_stars[cur_star].append(cur_number)

    print(numbers_and_stars)
    return sum([v[0]*v[1] for v in numbers_and_stars.values() if len(v) == 2])


class TestAll(unittest.TestCase):
    def test_part1(self):
        f = 'sample.txt'
        # self.assertEqual(4361, part1(f))
        f = 'input.txt'
        self.assertEqual(556367, part1(f))

    def test_part2(self):
        f = 'sample.txt'
        self.assertEqual(467835, part2(f))
        f = 'input.txt'
        self.assertEqual(89471771, part2(f))


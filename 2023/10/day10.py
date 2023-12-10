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

class Pipe:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, x, y):
        return Pipe(self.x + x, self.y + y)

VALID_PIPES = {
    (-1, 0): {'-', 'L', 'F'},
    (0, -1): {'|', '7', 'F'},
    (1, 0): {'-', 'J', '7'},
    (0, 1): {'|', 'L', 'J'},
}
DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
NEXT_DIRECTIONS = {
    ('-', (0, 1)): (0, 1),
    ('-', (0, -1)): (0, -1),
    ('L', (0, -1)): (-1, 0),
    ('L', (1, 0)): (0, 1),
    ('F', (-1, 0)): (0, 1),
    ('F', (0, -1)): (1, 0),
    ('|', (-1, 0)): (-1, 0),
    ('|', (1, 0)): (1, 0),
    ('7', (0, 1)): (1, 0),
    ('7', (-1, 0)): (0, -1),
    ('J', (1, 0)): (0, -1),
    ('J', (0, 1)): (-1, 0)}


def add(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]

def parse_grid(filename):
    scan = get_lines(filename)
    grid = dict()
    start = None
    for y, l in enumerate(scan):
        for x, c in enumerate(l):
            if c not in 'S-|F7JL':
                continue
            grid[(y, x)] = c
            if c == 'S':
                start = (y, x)
    return grid, start, len(scan), len(scan[0])


def part1(filename):
    grid, start, max_y, max_x = parse_grid(filename)
    for dir in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        if add(start, dir) not in grid:
            continue
        log(f'Start path at: {start} with dir {dir}')
        curr_pos = add(start, dir)
        curr_dir = dir
        if (grid[curr_pos], curr_dir) not in NEXT_DIRECTIONS:
            continue
        path = [start]
        while curr_pos != start:
            path += [curr_pos]
            nxt_dir = NEXT_DIRECTIONS[grid[curr_pos], curr_dir]
            nxt_pos = add(curr_pos, nxt_dir)
            log(f'curr_pos: {curr_pos}, curr_dir: {curr_dir}, pipe: {grid[curr_pos]} -> nxt_dir: {nxt_pos}, next_pos: {nxt_pos}')
            curr_dir, curr_pos = nxt_dir, nxt_pos
        log(path)
        return len(path) // 2
    return -1


def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(4, part1('sample.txt'))
        self.assertEqual(8, part1('sample2.txt'))

    def test_input(self):
        self.assertEqual(6815, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

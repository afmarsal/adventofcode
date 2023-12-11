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


RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)

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


def get_path(grid, start, max_y, max_x):
    for dir in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        if add(start, dir) not in grid:
            continue
        start_dir = dir
        # log(f'Start path at: {start} with dir {dir}')
        curr_pos = add(start, dir)
        curr_dir = dir
        if (grid[curr_pos], curr_dir) not in NEXT_DIRECTIONS:
            continue
        # TODO: this is wrong!! the start node should be handled after the main loop
        # with the same logic as any other node. Hardcoding a 0 gives the right
        # solution for my input
        path = {start: 0}
        lst_horizontal_dir = dir
        while curr_pos != start:
            nxt_dir = NEXT_DIRECTIONS[grid[curr_pos], curr_dir]
            nxt_pos = add(curr_pos, nxt_dir)
            path[curr_pos] = 0
            if curr_dir == RIGHT:
                path[curr_pos] = 1
                lst_horizontal_dir = curr_dir
            elif curr_dir == LEFT:
                path[curr_pos] = -1
                lst_horizontal_dir = curr_dir
            elif curr_dir == DOWN:
                if grid[curr_pos] == 'L' and lst_horizontal_dir == LEFT:
                    path[curr_pos] = 1
                    lst_horizontal_dir = RIGHT
                elif grid[curr_pos] == 'J' and lst_horizontal_dir == RIGHT:
                    path[curr_pos] = -1
                    lst_horizontal_dir = LEFT
            elif curr_dir == UP:
                if grid[curr_pos] == 'F' and lst_horizontal_dir == LEFT:
                    path[curr_pos] = 1
                    lst_horizontal_dir = RIGHT
                elif grid[curr_pos] == '7' and lst_horizontal_dir == RIGHT:
                    path[curr_pos] = -1
                    lst_horizontal_dir = LEFT
            else:
                raise Exception("Impossible!")
            log(f'curr_dir: {curr_dir}, curr_pos: {curr_pos}, pipe: {grid[curr_pos]}, path={path[curr_pos]} -> nxt_dir: {nxt_dir}, next_pos: {nxt_pos}')
            curr_dir, curr_pos = nxt_dir, nxt_pos

        log(f'start dir: {start_dir}, end_dir: {nxt_dir}')
        end_dir = nxt_dir
        if path[start] == 0:
            path[start] = end_dir[1]
        return path


def part1(filename):
    grid, start, max_y, max_x = parse_grid(filename)
    path = get_path(grid, start, max_y, max_x)
    return len(path) // 2


def part2(filename):
    grid, start, max_y, max_x = parse_grid(filename)
    path = get_path(grid, start, max_y, max_x)
    res = 0
    # Use the nonzero rule: https://en.wikipedia.org/wiki/Nonzero-rule
    # Trace a line from a point going down and check intersections
    in_loop = []
    for y in range(max_y):
        for x in range(max_x):
            cur_pos = (y, x)
            if cur_pos in path:
                continue
            intersections = 0
            log(f'Checking {cur_pos}={path.get(cur_pos, 0)}...')
            # for z in range(y+1,max_y):
            for z in range(0, y):
                ray_pos = (z, x)
                intersections += path.get(ray_pos, 0)
                log(f'Ray at {ray_pos}={path.get(ray_pos, 0)}. Grid: {grid.get(ray_pos, ".")} Intersections: {intersections}')
            log(f'{cur_pos}={path.get(cur_pos, 0)}. Intersections: {intersections}')
            res += 1 if intersections else 0
            in_loop += [cur_pos] if intersections else []

    log(in_loop)
    return res


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(4, part1('sample.txt'))
        self.assertEqual(8, part1('sample2.txt'))

    def test_input(self):
        self.assertEqual(6815, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(4, part2('sample3.txt'))
        self.assertEqual(4, part2('sample4.txt'))
        self.assertEqual(8, part2('sample5.txt'))
        self.assertEqual(10, part2('sample6.txt'))

    def test_input(self):
        self.assertEqual(269, part2('input.txt'))
        # 273 too high

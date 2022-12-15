import re
import unittest
from dataclasses import dataclass
import itertools


def read(filename):
    with open(filename) as f:
        return [Sensor(x1, y1, x2, y2) for line in f.read().splitlines() for x1, y1, x2, y2 in [list(map(int, re.findall(r'-?\d+', line)))]]

def log(param='', end='\n'):
    # print(param, end=end)
    pass

def log_nolf(param):
    # print(param, end='')
    pass

@dataclass
class Point:
    x: int
    y: int

    def __repr__(self) -> str:
        return f'{self.x},{self.y}'


class Sensor:

    def __init__(self, sx, sy, bx, by) -> None:
        self.pos = Point(sx, sy)
        self.beacon = Point(bx, by)

    def manhattan(self, p):
        return abs(self.pos.x - p.x) + abs(self.pos.y - p.y)

    def in_x(self, x):
        return self.min_x() <= x <= self.max_x()

    def min_x(self):
        return self.pos.x - self.manhattan(self.beacon)

    def max_x(self):
        return self.pos.x + self.manhattan(self.beacon)

    def radius(self):
        return self.manhattan(self.beacon)

    def range_of_points_at(self, y):
        result = None
        busy = []
        offset = self.radius() - abs(self.pos.y - y)
        if offset >= 0:
            edge_min = self.pos.x - offset
            edge_max = self.pos.x + offset
            result = (edge_min, edge_max)
            # Print
            # for i in range(-5, 30):
            #     log_nolf(f'{i%10}')
            # log()
            # for i in range(-5, 30):
            #     char = '#' if edge_min <= i <= edge_max else '.'
            #     if self.pos.x == i and self.pos.y == y:
            #         char = 'S'
            #     if self.beacon.x == i and self.beacon.y == y:
            #         char = 'B'
            #     log_nolf(char)
            # log()
            # # End print
            # if self.pos.y == y:
            #     # log(f'Found sensor!!')
            #     pass

        if self.beacon.y == y:
            # log_nolf(f'Found beacon at {self.beacon.x}. Converting {result} to -> ')
            busy.append((self.beacon.x, self.beacon.x))
            # log(f'{result}')
        if self.pos.y == y:
            # log_nolf(f'Found sensor at {self.pos.x}. Converting {result} to...\n')
            busy.append((self.pos.x, self.pos.x))
            # log(f'{result}')
        log(f'Range at {y}: s: {self}, offset: {offset}. Result: {result}, busy: {busy}')
        return result, busy

    def __repr__(self) -> str:
        return f'(s:{self.pos}, b:{self.beacon}, r:{self.radius()})'


def range_diff(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    endpoints = sorted((s1, s2-1, e1, e2+1))
    result = []
    if endpoints[0] == s1:
        result.append((endpoints[0], endpoints[1]))
    if endpoints[3] == e1:
        result.append((endpoints[2], endpoints[3]))
    return result

def multirange_diff(r1_list, r2_list):
    for r2 in r2_list:
        r1_list = list(itertools.chain(*[range_diff(r1, r2) for r1 in r1_list]))
    return r1_list


def get_row_data(grid, row):
    ranges = []
    total_busy = set()
    for s in grid:
        r, busy = s.range_of_points_at(row)
        if r:
            ranges.append(r)
        total_busy.update(busy)
    return ranges, total_busy

def count_busy_in_row(grid, row):
    ranges, busy = get_row_data(grid, row)
    result = 0
    counted_ranges = []
    for r in ranges:
        if not r:
            continue
        sub_ranges = multirange_diff([r], counted_ranges)
        sub_ranges = multirange_diff(sub_ranges, busy)
        partial = 0
        for sr in sub_ranges:
            partial += sr[1] - sr[0] + 1
        result += partial

        counted_ranges.extend(sub_ranges)
    return result

def part1(filename, row):
    grid = read(filename)
    return count_busy_in_row(grid, row)

def part2(filename, max_row):
    # Asuming the "single" beacon should be at distance of max dist + 1 of any sensor
    grid = read(filename)
    checked_rows = set()
    for sensor in grid:
        min_y = max(0, sensor.pos.y - sensor.radius() - 1)
        max_y = min(max_row, sensor.pos.y + sensor.radius() + 1)
        for y in range(min_y, max_y):
            if y in checked_rows:
                continue
            ranges, busy = get_row_data(grid, y)
            free_range = multirange_diff([(0, max_row)], ranges)
            free_range = multirange_diff(free_range, busy)
            if free_range:
                x = free_range[0][1]
                log(f'Free range non empty: {free_range}. x={x}, y={y}')
                return x * 4000000 + y
            checked_rows.add(y)

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(26, part1('sample.txt', 10))

    def test_input(self):
        self.assertEqual(5832528, part1('input.txt', 2000000))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(56000011, part2('sample.txt', 20))

    def test_input(self):
        self.assertEqual(13360899249595, part2('input.txt', 4000000))
        pass

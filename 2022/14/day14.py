import sys
import time
import unittest
from dataclasses import dataclass


def read(filename):
    with open(filename) as f:
        underground = set()
        max_x = 0
        min_x = sys.maxsize
        max_y = 0
        min_y = sys.maxsize
        for line in f.read().splitlines():
            prev_x, prev_y = None, None
            for pair in line.split(' -> '):
                new_x, new_y = tuple(map(int, pair.split(',')))
                if prev_x:
                    x1, x2 = min(prev_x, new_x), max(prev_x, new_x)
                    y1, y2 = min(prev_y, new_y), max(prev_y, new_y)
                    for x in range(x1, x2 + 1):
                        for y in range(y1, y2 + 1):
                            underground.add((x, y))
                min_x, max_x = min(min_x, new_x), max(max_x, new_x)
                min_y, max_y = min(min_y, new_y), max(max_y, new_y)
                prev_x = new_x
                prev_y = new_y
    return Underground(min_x, min_y, max_x, max_y, underground, set())

@dataclass
class Underground:
    min_x: int
    min_y: int
    max_x: int
    max_y: int
    rocks: set
    sand: set

    def free(self, x, y):
        return (x, y) not in self.rocks and (x, y) not in self.sand and y < self.floor_y()

    def floor_y(self):
        return self.max_y + 2

    def pour1(self, x_pos):
        total_units = 0
        while True:
            sand_x, sand_y = x_pos, 0
            pouring = True
            total_units += 1
            while pouring:
                sand_y += 1
                if sand_y > self.max_y:
                    return total_units - 1
                if self.free(sand_x, sand_y + 1):
                    continue
                if self.free(sand_x - 1, sand_y + 1):
                    sand_x -= 1
                    continue
                if self.free(sand_x + 1, sand_y + 1):
                    sand_x += 1
                    continue
                # Settle
                self.sand.add((sand_x, sand_y))
                break

    def pour2(self, x_pos):
        total_units = 0
        while True:
            sand_x, sand_y = x_pos, -1
            pouring = True
            total_units += 1
            while pouring:
                sand_y += 1
                if self.free(sand_x, sand_y + 1):
                    continue
                if self.free(sand_x - 1, sand_y + 1):
                    sand_x -= 1
                    continue
                if self.free(sand_x + 1, sand_y + 1):
                    sand_x += 1
                    continue
                # Settle
                self.sand.add((sand_x, sand_y))
                if (sand_x, sand_y) == (x_pos, 0):
                    return total_units
                # self.print(total_units, sand_x, sand_y)
                # time.sleep(1/10)
                break

    def print(self, units, sand_x, sand_y):
        print('units: {}'.format(units))
        for y in range(0, self.max_y + 4):
            for x in range(self.min_x - 4, self.max_x+4):
                if (x, y) == (sand_x, sand_y):
                    char = 'x'
                elif (x, y) in self.rocks or y == self.floor_y():
                    char = '#'
                else:
                    char = 'o' if (x, y) in self.sand else '.'
                print(char, end='')
            print()

def log(param):
    print(param)
    pass


def part1(filename):
    underground = read(filename)
    return underground.pour1(500)


def part2(filename):
    underground = read(filename)
    return underground.pour2(500)


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(24, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(825, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(93, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

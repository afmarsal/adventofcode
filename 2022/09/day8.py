import itertools
import operator
import unittest
from numpy import sign


def read(filename):
    with open(filename) as f:
        return [l.split() for l in f.read().splitlines()]

def log(param):
    print(param)
    pass


STEPS = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def move(s, step):
    return s[0] + step[0], s[1] + step[1]

def dist(t, s):
    return max(abs(s[0]-t[0]), abs(s[1]-t[1]))

def follow(t, s):
    if dist(t, s) <= 1:
        return t
    move_x = sign(s[0] - t[0])
    move_y = sign(s[1] - t[1])
    return move(t, (move_x, move_y))

def rope(filename, tail_size):
    knots = [(0, 0)] * tail_size  # list of knot positions [(0,0), (0,0)...]
    visited = set()
    for direction, num_steps in read(filename):
        for i in range(int(num_steps)):
            knots[0] = move(knots[0], STEPS[direction])
            for prev, knot in itertools.pairwise(range(len(knots))):
                knots[knot] = follow(knots[knot], knots[prev])
            visited.add(knots[len(knots)-1])
    return len(visited)

def part1(filename):
    return rope(filename, 2)

def part2(filename):
    return rope(filename, 10)

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(13, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(6026, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1, part2('sample.txt'))
        self.assertEqual(36, part2('sample2.txt'))

    def test_input(self):
        self.assertEqual(2273, part2('input.txt'))

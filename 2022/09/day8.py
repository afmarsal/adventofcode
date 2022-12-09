import itertools as it
import operator
import unittest
import numpy as np
from numpy import sign


def read(filename):
    with open(filename) as f:
        return [l.split() for l in f.read().splitlines()]

def log(param):
    print(param)
    pass


def move(s, step_x, step_y):
    return tuple(map(operator.add, s, (step_x, step_y)))


def dist(t, s):
    return max(abs(s[0]-t[0]), abs(s[1]-t[1]))


def follow(t, s):
    if dist(t, s) <= 1:
        return t
    move_x = sign(s[0] - t[0])
    move_y = sign(s[1] - t[1])
    t = move(t, move_x, move_y)
    return t

def part1(filename):
    s = t = (0, 0)
    visited = {t}
    for direction, steps in read(filename):
        for i in range(int(steps)):
            match direction:
                case 'R':
                    s = move(s, 1, 0)
                case 'L':
                    s = move(s, -1, 0)
                case 'U':
                    s = move(s, 0, 1)
                case 'D':
                    s = move(s, 0, -1)
            t = follow(t, s)
            visited.add(t)
    return len(visited)

def part2(filename):
    s = (0, 0)
    knots = [s] * 9
    visited = {s}
    for direction, steps in read(filename):
        for i in range(int(steps)):
            match direction:
                case 'R':
                    s = move(s, 1, 0)
                case 'L':
                    s = move(s, -1, 0)
                case 'U':
                    s = move(s, 0, 1)
                case 'D':
                    s = move(s, 0, -1)
            prev_knot = s
            for j in range(len(knots)):
                knots[j] = follow(knots[j], prev_knot)
                prev_knot = knots[j]
            visited.add(knots[len(knots)-1])
    return len(visited)

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

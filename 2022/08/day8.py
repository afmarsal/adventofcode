import itertools as it
import unittest
import numpy as np

def read(filename):
    with open(filename) as f:
        return [[int(c) for c in l] for l in f.read().splitlines()]

def log(param):
    print(param)
    pass


def is_visible(forest, y, x):
    vis_left  = all(forest[y, x] > t for t in forest[y, :x])
    vis_right = all(forest[y, x] > t for t in forest[y, x+1:])
    vis_up    = all(forest[y, x] > t for t in forest[:y, x])
    vis_down  = all(forest[y, x] > t for t in forest[y+1:, x])
    return vis_left or vis_right or vis_up or vis_down


def part1(filename):
    forest = np.array(read(filename))
    edges = (len(forest)-1) * 2 + (len(forest[0])-1) * 2
    return edges + sum([int(is_visible(forest, y, x))
                        for y in range(1, len(forest) - 1)
                        for x in range(1, len(forest[y]) - 1)])

def view(line, tree):
    # Adding + 1 to count for the blocking tree. If no blocking, then it accounts for the edge.
    return len(list(it.takewhile(lambda v: v < tree, line))) + 1

def scenic_score(forest, y, x):
    dist_left  = view(forest[y, x-1:0:-1], forest[y, x])
    dist_right = view(forest[y, x+1:-1], forest[y, x])
    dist_up    = view(forest[y-1:0:-1, x], forest[y, x])
    dist_down  = view(forest[y+1:-1, x], forest[y, x])
    return dist_left * dist_right * dist_up * dist_down

def part2(filename):
    forest = np.array(read(filename))
    return max(scenic_score(forest, y, x)
               for y in range(1, len(forest) - 1)
               for x in range(1, len(forest[y]) - 1))

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(21, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(1785, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(8, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(345168, part2('input.txt'))

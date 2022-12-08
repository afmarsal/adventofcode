import unittest
import re


def read(filename):
    with open(filename) as f:
        return [[int(c) for c in l] for l in f.read().splitlines()]

def log(param):
    # print(param)
    pass

def part1(filename):
    result = 0
    forest = read(filename)
    for y in range(len(forest)):
        visible = False
        for x in range(len(forest[y])):
            tree = forest[y][x]
            log("Tree: {},{} -> {}".format(x, y, tree))
            visible = all(tree > forest[y][i] for i in range(x))
            log("1: {},{} -> {}".format(x, y, visible))
            visible = visible or all(tree > forest[y][i] for i in range(x + 1, len(forest[y])))
            log("2: {},{} -> {}".format(x, y, visible))
            visible = visible or all(tree > forest[i][x] for i in range(y))
            log("3: {},{} -> {}".format(x, y, visible))
            visible = visible or all(tree > forest[i][x] for i in range(y + 1, len(forest)))
            log("4: {},{} -> {}".format(x, y, visible))
            result += int(visible)
            log("Result: {}".format(result))
    return result

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(21, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(1785, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(24933642, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(3979145, part2('input.txt'))

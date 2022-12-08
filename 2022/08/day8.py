import unittest
import itertools as it

def read(filename):
    with open(filename) as f:
        return [[int(c) for c in l] for l in f.read().splitlines()]

def log(param):
    print(param)
    pass

def part1(filename):
    result = 0
    forest = read(filename)
    for y in range(len(forest)):
        for x in range(len(forest[y])):
            tree = forest[y][x]
            visible = all(tree > forest[y][i] for i in range(x))
            visible = visible or all(tree > forest[y][i] for i in range(x + 1, len(forest[y])))
            visible = visible or all(tree > forest[i][x] for i in range(y))
            visible = visible or all(tree > forest[i][x] for i in range(y + 1, len(forest)))
            result += int(visible)
    return result

def dist(forest, x, y, ry, rx):
    result = 1
    for j in ry:
        for i in rx:
            if forest[y][x] <= forest[j][i]:
                break
            result += 1
        else:
            continue
        break
    return result

def score(forest, y, x):
    dist_left = dist(forest, x, y, [y], range(x - 1, 0, -1))
    dist_right = dist(forest, x, y, [y], range(x + 1, len(forest[y]) - 1))
    dist_up = dist(forest, x, y, range(y - 1, 0, -1), [x])
    dist_down = dist(forest, x, y, range(y + 1, len(forest) - 1), [x])
    result = dist_left * dist_right * dist_up * dist_down
    # log("{}, {}: {} -> {}, {}, {}, {} => {}".format(x, y, forest[y][x], dist_up, dist_left, dist_down,
    # dist_right, result))
    return result


def part2(filename):
    forest = read(filename)
    return max(score(forest, y, x) for y in range(1, len(forest) - 1) for x in range(1, len(forest[y]) - 1))

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(21, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(1785, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(8, part2('sample.txt'))

    def test_input(self):
        # 20, 72, 120, 216 not!
        self.assertEqual(345168, part2('input.txt'))

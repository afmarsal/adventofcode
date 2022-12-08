import unittest

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


def score(forest, y, x):
    if y == 0 or x == 0 or y == len(forest) - 1 or x == len(forest[y]) - 1:
        return 0
    tree = forest[y][x]
    dist_left = 1
    for i in range(x-1, 0, -1):
        if tree <= forest[y][i]:
            break
        dist_left += 1
    dist_right = 1
    for i in range(x+1, len(forest[y])-1):
        if tree <= forest[y][i]:
            break
        dist_right += 1
    dist_up = 1
    for i in range(y-1, 0, -1):
        if tree <= forest[i][x]:
            break
        dist_up += 1
    dist_down = 1
    for i in range(y+1, len(forest)-1):
        if tree <= forest[i][x]:
            break
        dist_down += 1
    result = dist_left * dist_right * dist_up * dist_down
    log("{}, {}: {} -> {}, {}, {}, {} => {}".format(x, y, forest[y][x], dist_up, dist_left, dist_down, dist_right, result))
    return result


def part2(filename):
    forest = read(filename)
    return max(score(forest, y, x) for y in range(len(forest)) for x in range(len(forest[y])))

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

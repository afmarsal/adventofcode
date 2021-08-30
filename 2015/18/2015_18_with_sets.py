import operator
import unittest
import cProfile

all_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def parse_input(lines):
    return {(i, j) for i, line in enumerate(lines) for j, square in enumerate(line) if square == '#'}


def get_num_ON_neighbour(lights, i, j):
    return sum((x, y) in lights for x in (i - 1, i, i + 1) for y in (j - 1, j, j + 1) if (i, j) != (x, y))


def print_grid(step, lights):
    return
    print()
    print(f'Step: {step}')
    print(lights)
    size = 6
    for i in range(size):
        line = ''
        for j in range(size):
            line += '#' if (i, j) in lights else '.'
        print(line)


def solve(lines, steps, keep_corners=False):
    lights = parse_input(lines)
    size = len(lines)
    print_grid(0, lights)
    corners = {(0, 0), (0, len(lines) - 1), (len(lines) - 1, 0), (len(lines) - 1, len(lines) - 1)} \
        if keep_corners else set()
    for step in range(steps):
        lights = corners | {(x, y) for x in range(size) for y in range(size)
                            if (x, y) in lights and 2 <= get_num_ON_neighbour(lights, x, y) <= 3
                            or (x, y) not in lights and get_num_ON_neighbour(lights, x, y) == 3}
        print_grid(0, lights)
    return len(lights)


def part1(lines, steps):
    return solve(lines, steps)


def part2(lines, steps):
    return solve(lines, steps, True)


class TestPart1(unittest.TestCase):
    def test_sample(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part1(lines, 4), 4)

    def test_input1(self):
        with open('input_part1.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part1(lines, 100), 1061)


class TestPart2(unittest.TestCase):
    def test_sample(self):
        with open('input2.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part2(lines, 5), 17)

    def test_input1(self):
        with open('input_part1.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part2(lines, 100), 1006)


if __name__ == '__main__':
    cProfile.run('unittest.main()')

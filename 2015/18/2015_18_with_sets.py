import operator
import unittest
import cProfile

all_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def parse_input(lines):
    return {(i, j) for i, line in enumerate(lines) for j, square in enumerate(line) if square == '#'}


def get_num_ON_neighbour(lights, i, j):
    result = 0
    for neighbour in all_neighbours:
        result += 1 if (neighbour[0] + i, neighbour[1] + j) in lights else 0
    return result


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
    print_grid(0, lights)
    for step in range(steps):
        new_lights = set()
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                num_neighbours = get_num_ON_neighbour(lights, i, j)
                if (i, j) in lights and 2 <= num_neighbours <= 3:
                    new_lights.add((i, j))
                elif (i, j) not in lights and num_neighbours == 3:
                    new_lights.add((i, j))
        if keep_corners:
            new_lights.update(
                {(0, 0), (0, len(lines) - 1), (len(lines) - 1, 0), (len(lines) - 1, len(lines) - 1)})
        lights = new_lights
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

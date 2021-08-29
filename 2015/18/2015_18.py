import operator
import unittest
import cProfile

all_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def parse_input(lines):
    result = []
    for line in lines:
        result.append([ch for ch in line])
    return result


def get_neighbor_squares(grid, i, j):
    return [grid[i + neighbour[0]][j + neighbour[1]] for neighbour in all_neighbours
            if 0 <= i + neighbour[0] < len(grid) and 0 <= j + neighbour[1] < len(grid[i])]


def print_grid(step, grid):
    return
    print(f'Step {step}:')
    for line in grid:
        print(line)


def solve(lines, steps, keep_corners=False):
    grid = parse_input(lines)
    print_grid(0, grid)
    for step in range(steps):
        next_grid = [['.' for col in range(len(grid[0]))] for row in range(len(grid))]
        for i, line in enumerate(grid):
            # print(f'Step, i: {step}, {i}')
            for j, square in enumerate(grid[i]):
                if keep_corners and (i in (0, len(grid) - 1) and j in (0, len(grid[i]) - 1)):
                    next_grid[i][j] = '#'
                    continue
                neighbor_squares = get_neighbor_squares(grid, i, j)
                if square == '#' and neighbor_squares.count('#') in (2, 3):
                    next_grid[i][j] = '#'
                elif square == '.' and neighbor_squares.count('#') == 3:
                    next_grid[i][j] = '#'
                else:
                    next_grid[i][j] = '.'
        grid = next_grid[:]
        print_grid(step, grid)
    return [square for line in grid for square in line].count('#')


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

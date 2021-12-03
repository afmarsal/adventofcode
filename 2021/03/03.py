import functools
import unittest
import numpy as np


def read_lines(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return np.array([list(l) for l in lines])


def part1(file_name):
    lines = read_lines(file_name).transpose()
    # for each column, shift and accumulate 1 or 0 depending on count of 1's or 0's
    gamma = functools.reduce(lambda accum, line: (accum << 1) + (line[line == '1'].size > len(line)/2), lines, 0)
    # epsilon is the "negated" value of gamma, but needs to be masked to the length of the number
    mask = ~(~0 << len(lines))
    epsilon = ~gamma & mask
    print(f'Gamma: {gamma}, Epsilon: {epsilon}')
    return gamma * epsilon


def part2(file_name):
    return calc_oxygen(file_name) * calc_co2(file_name)


def calc_oxygen(file_name):
    all_lines = read_lines(file_name)
    col = 0
    while len(all_lines) > 1:
        line = all_lines[:, col]
        ones = line[line == '1'].size
        zeroes = line[line == '0'].size
        if ones >= zeroes:
            all_lines = all_lines[all_lines[:, col] == '1']
        else:
            all_lines = all_lines[all_lines[:, col] == '0']
        col += 1
    res = ''.join(all_lines[0])
    print(f'num: {res}')
    return int(res, 2)


def calc_co2(file_name):
    all_lines = read_lines(file_name)
    col = 0
    while len(all_lines) > 1:
        line = all_lines[:, col]
        ones = line[line == '1'].size
        zeroes = line[line == '0'].size
        if zeroes <= ones:
            all_lines = all_lines[all_lines[:, col] == '0']
        else:
            all_lines = all_lines[all_lines[:, col] == '1']
        col += 1
    res = ''.join(all_lines[0])
    print(f'num: {res}')
    return int(res, 2)


class TestPart1(unittest.TestCase):
    def test10(self):
        self.assertEqual(198, part1('input0.txt'))

    def test1(self):
        self.assertEqual(3429254, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test20(self):
        self.assertEqual(230, part2('input0.txt'))

    def test21(self):
        self.assertEqual(5410338, part2('input.txt'))

import unittest
import numpy as np


def read_lines(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return np.array([list(l) for l in lines])


def part1(file_name):
    lines = read_lines(file_name)
    lines = lines.transpose()
    res = 0
    for line in lines:
        ones, zeroes = 0, 0
        for j in line:
            if j == '0':
                zeroes += 1
            else:
                ones += 1
        res = (res << 1) + (ones > zeroes)
    mask = ~(~0 << len(lines))
    res2 = ~res & mask
    print(f'Gamma: {res}, Epsilon: {res2}')
    return res * res2


def part1_calc(lines):
    res = 0
    for line in lines:
        ones, zeroes = 0, 0
        for j in line:
            if j == '0':
                zeroes += 1
            else:
                ones += 1
        res = (res << 1) + (ones > zeroes)
    mask = ~(~0 << len(lines))
    res2 = ~res ^ mask
    print(f'Gamma: {res}, Epsilon: {res2}')
    return res * res2


def part2(lines):
    return 0


class TestPart1(unittest.TestCase):
    def test10(self):
        self.assertEqual(198, part1('input0.txt'))

    def test1(self):
        self.assertEqual(3429254, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test20(self):
        self.assertEqual(198, part2('input0.txt'))

    def test21(self):
        self.assertEqual(198, part1('input.txt'))

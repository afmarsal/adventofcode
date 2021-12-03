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

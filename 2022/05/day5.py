import re
import unittest
import numpy as np


def read_crates(filename):
    columns = []
    with open(filename) as f:
        for line in f.read().splitlines():
            row = line[1::4]
            columns.append(np.array(list(row)))
        arr = np.array(columns).transpose()
        return [list(''.join(col).strip()) for col in arr.tolist()]

def read_moves(moves_file):
    moves = []
    with open(moves_file) as f:
        for line in f.read().splitlines():
            moves.append(list(map(int, re.findall(r"\d+", line))))
    return moves


def day1(crates_file, moves_file):
    crates = read_crates(crates_file)
    moves = read_moves(moves_file)
    for move in moves:
        for i in range(int(move[0])):
            crates[move[2]-1].insert(0, crates[move[1]-1].pop(0))
    return ''.join([c[0] for c in crates])


def day2(crates_file, moves_file):
    crates = read_crates(crates_file)
    moves = read_moves(moves_file)
    for move in moves:
        crates[move[2] - 1][:0] = crates[move[1] - 1][:move[0]]
        crates[move[1] - 1][0:move[0]] = []
    return ''.join([c[0] for c in crates])


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual('CMZ', day1('sample_0.txt', 'sample_1.txt'))

    def test_input(self):
        self.assertEqual('QNNTGTPFN', day1('input_0.txt', 'input_1.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual('MCD', day2('sample_0.txt', 'sample_1.txt'))

    def test_input(self):
        self.assertEqual('GGNPJBTTR', day2('input_0.txt', 'input_1.txt'))

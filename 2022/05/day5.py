import re
import unittest
import numpy as np


def chunks(l, n):
    """Yield n number of striped chunks from l."""
    for i in range(0, n):
        yield l[i::n]


def read_crates(filename):
    columns = []
    with open(filename) as f:
        for l in f.read().splitlines():
            row = l[1::4]
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
    print(crates)
    print(moves)
    print()
    for move in moves:
        for i in range(int(move[0])):
            crates[move[2]-1].insert(0, crates[move[1]-1].pop(0))
    return ''.join([c[0] for c in crates])


def day2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual('CMZ', day1('sample_0.txt', 'sample_1.txt'))

    def test_input(self):
        self.assertEqual('QNNTGTPFN', day1('input_0.txt', 'input_1.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(4, day2('sample.txt'))

    def test_input(self):
        self.assertEqual(888, day2('input.txt'))

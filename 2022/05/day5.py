import re
import unittest


def read(crates_file, moves_file):
    with open(crates_file) as f:
        rows = [list(line[1::4]) for line in f.read().splitlines()]
        columns = list(map(list, zip(*rows)))  # transpose
        # This leaves top crate in position 0
        crates = [[c for c in col if c != ' '] for col in columns]  # filter out ' '
    with open(moves_file) as f:
        moves = [list(map(int, re.findall(r"\d+", line))) for line in f.read().splitlines()]
    return crates, moves

def day1(crates_file, moves_file):
    crates, moves = read(crates_file, moves_file)
    for move in moves:
        for i in range(int(move[0])):
            crates[move[2]-1].insert(0, crates[move[1]-1].pop(0))
    return ''.join([c[0] for c in crates])


def day2(crates_file, moves_file):
    crates, moves = read(crates_file, moves_file)
    for move in moves:
        crates[move[2]-1][:0] = crates[move[1]-1][:move[0]]
        crates[move[1]-1][0:move[0]] = []
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

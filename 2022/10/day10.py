import itertools
import operator
import unittest
from numpy import sign


def read(filename):
    with open(filename) as f:
        return [l.split() for l in f.read().splitlines()]


def log(param):
    print(param)
    pass


def part1(filename):
    cycle = 1
    rx = 1
    special_cycles = {20, 60, 100, 140, 180, 220}
    signal_strengths = []
    for instr in read(filename):
        cycles_left = 1
        cycling = False
        while cycles_left > 0:
            match instr:
                case ['addx', _]:
                    if not cycling:
                        cycles_left = 2
                        cycling = True
            if cycle in special_cycles:
                signal_strength = cycle * rx
                signal_strengths.append(signal_strength)
            cycles_left -= 1
            cycle += 1
        match instr:
            case ['addx', delta]:
                rx += int(delta)

    return sum(s for s in signal_strengths)


def part2(filename):
    cycle = 1
    rx = 1
    crt = [['.' for i in range(40)] for j in range(6)]
    for instr in read(filename):
        cycles_left = 1
        cycling = False
        while cycles_left > 0:
            match instr:
                case ['addx', _]:
                    if not cycling:
                        cycles_left = 2
                        cycling = True
            crt_y, crt_x = divmod(cycle - 1, 40)
            if crt_x in {rx - 1, rx, rx + 1}:
                crt[crt_y][crt_x] = '▮'
            cycles_left -= 1
            cycle += 1
        match instr:
            case ['addx', delta]:
                rx += int(delta)

    for line in crt:
        print(''.join(line))
    return 'EJBZLRJR'


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(13140, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(12640, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1, part2('sample.txt'))

    def test_input(self):
        self.assertEqual("EJBZLRJR", part2('input.txt'))

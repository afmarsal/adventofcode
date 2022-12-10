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
    # for instr, delta in read(filename):
    for instr in read(filename):
        # log('cycle: {}, instr: {}, rx: {}'.format(cycle, instr, rx))
        cycles_left = 1
        cycling = False
        while cycles_left > 0:
            match instr:
                case ['addx', _]:
                    if not cycling:
                        cycles_left = 2
                        cycling = True
                case ['noop']:
                    pass
                case _:
                    raise Exception('Invalid instruction: {}'.format(instr))
            if cycle in special_cycles:
                signal_strength = cycle * rx
                signal_strengths.append(signal_strength)
                log('Adding signal strength cycle: {}, rx: {}, strength: {}'.format(cycle, rx, signal_strength))
            cycles_left -= 1
            cycle += 1
            # log('cycle: {}, instr: {}, left: {}, rx: {}'.format(cycle, instr, cycles_left, rx))
        match instr:
            case ['addx', delta]:
                rx += int(delta)

    return sum(s for s in signal_strengths)

def part2(filename):
    return rope(filename, 10)

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(13140, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(12640, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(2273, part2('input.txt'))

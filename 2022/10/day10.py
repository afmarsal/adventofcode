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
    cycle = 1
    rx = 1
    signal_strengths = []
    crt = [['.' for i in range(40)] for j in range(6)]
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

            crt_y, crt_x = divmod(cycle - 1, 40)
            sprite_pos = {rx-1, rx, rx+1}
            line = crt[crt_y][:]
            line[rx-1:rx+2] = '###'
            line[crt_x] = 'X'
            log('cycle: {}, line: {}'.format(cycle, ''.join(line)))
            if crt_x in sprite_pos:
                crt[crt_y][crt_x] = '◼'
                log('cycle: {}, lit {},{}'.format(cycle+1, crt_y, crt_x))
            cycles_left -= 1
            cycle += 1
        match instr:
            case ['addx', delta]:
                rx += int(delta)

    for line in crt:
        print(''.join(line))
    return sum(s for s in signal_strengths)



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

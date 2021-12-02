import unittest


def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def part1(lines):
    x, y = 0, 0
    for l in lines:
        instr, param = l.split()
        if instr == 'forward':
            x += int(param)
        elif instr == 'down':
            y += int(param)
        elif instr == 'up':
            y -= int(param)
        else:
            raise RuntimeError(f'Invalid instruction {instr}')

    return x * y


def part2(lines):
    x, y, aim = 0, 0, 0
    for l in lines:
        instr, param = l.split()
        if instr == 'forward':
            x += int(param)
            y += aim * int(param)
        elif instr == 'down':
            aim += int(param)
        elif instr == 'up':
            aim -= int(param)
        else:
            raise RuntimeError(f'Invalid instruction {instr}')

    return x * y


class TestPart1(unittest.TestCase):
    def test10(self):
        lines = read_lines('input0.txt')
        self.assertEqual(part1(lines), 150)

    def test1(self):
        lines = read_lines('input.txt')
        self.assertEqual(part1(lines), 2150351)


class TestPart2(unittest.TestCase):
    def test20(self):
        lines = read_lines('input0.txt')
        self.assertEqual(900, part2(lines))

    def test21(self):
        lines = read_lines('input.txt')
        self.assertEqual(1842742223, part2(lines))
# 2150351 too low

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


def part2(nums):
    return sum([1 if v1+v2+v3 > v0+v1+v2 else 0 for v0, v1, v2, v3 in zip(nums, nums[1:], nums[2:], nums[3:])])


class TestPart1(unittest.TestCase):
    def test10(self):
        lines = read_lines('input0.txt')
        self.assertEqual(part1(lines), 150)

    def test1(self):
        lines = read_lines('input.txt')
        self.assertEqual(part1(lines), 150)


class TestPart2(unittest.TestCase):
    def test20(self):
        lines = read_lines('input0.txt')
        self.assertEqual(part2(lines), 150)

    def test21(self):
        lines = read_lines('input.txt')
        self.assertEqual(part1(lines), 150)

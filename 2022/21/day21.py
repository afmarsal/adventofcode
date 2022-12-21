import unittest

def read(filename):
    with open(filename) as f:
        return {k: v.strip() for line in f.read().splitlines() for k, v in [line.split(':')]}

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')


def calc(inp, monkey):
    if inp[monkey].isdigit():
        return int(inp[monkey])
    else:
        m1, op, m2 = inp[monkey].split()
        op = '//' if op == '/' else op
        return eval(f'{calc(inp, m1)} {op} {calc(inp, m2)} ')


def part1(filename):
    inp = read(filename)
    return calc(inp, 'root')

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(152, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(75147370123646, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(301, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

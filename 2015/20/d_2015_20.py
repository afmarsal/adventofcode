import unittest
from sympy import divisors

def read(filename):
    with open(filename) as f:
        return f.read().splitlines()

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')

def part1(num):
    num = num // 10
    s, house = 0, 0
    while s < num:
        house += 1
        s = sum(d for d in divisors(house))
        # log(f'House: {house}, sum: {s}')
    return house


def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1, part1(10))
        self.assertEqual(2, part1(30))
        self.assertEqual(3, part1(40))
        self.assertEqual(4, part1(70))
        self.assertEqual(6, part1(120))
        self.assertEqual(8, part1(150))

    def test_input(self):
        self.assertEqual(786240, part1(34000000))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

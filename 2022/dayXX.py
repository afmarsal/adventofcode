import unittest

def read(filename):
    with open(filename) as f:
        return f.read().splitlines()

def log(param):
    print(param)
    pass


def part1(filename):
    return -1

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

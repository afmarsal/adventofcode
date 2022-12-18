import unittest

def read(filename):
    with open(filename) as f:
        return [eval(f'({line})') for line in f.read().splitlines()]

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')

def dist(cube1, cube2):
    return sum(abs(c1 - c2) for c1, c2 in zip(cube1, cube2))

def part1(filename):
    inp = read(filename)
    connected = 0
    for i, cube1 in enumerate(inp):
        for cube2 in inp[i+1:]:
            if dist(cube1, cube2) == 1:
                connected += 2
    return len(inp) * 6 - connected

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(64, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

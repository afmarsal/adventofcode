import unittest
import numpy as np

def read(filename):
    with open(filename) as f:
        return f.read().splitlines()


first = lambda it: next(iter(it))
priority = lambda c: ord(c) + 1 - (ord('a') if c.islower() else ord('A') - 26)

def part1(filename):
    common_char = lambda l: first(set(l[:len(l) // 2]).intersection(l[len(l) // 2:]))
    return sum([priority(common_char(line)) for line in read(filename)])

def part2(filename):
    lines = read(filename)
    chunks = np.array_split(lines, len(lines) // 3)
    common_char = lambda chunk: first(set.intersection(*[set(l) for l in chunk]))
    return sum([priority(common_char(chunk)) for chunk in chunks])


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(157, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(8072, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(70, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(2567, part2('input.txt'))

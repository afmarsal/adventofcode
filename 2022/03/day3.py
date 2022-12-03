import unittest
import numpy as np

def read(filename):
    with open(filename) as f:
        return f.read().splitlines()

def day1(filename):
    res = 0
    for l in read(filename):
        common = set(l[:len(l) // 2]).intersection(l[len(l) // 2:])
        c = next(iter(common))
        prio = ord(c) + 1 - (ord('a') if c.islower() else ord('A') - 26)
        # print('{} {} {}'.format(common, c, prio))
        res += prio
    return res

def day2(filename):
    lines = read(filename)
    chunks = np.array_split(lines, len(lines) // 3)
    res = 0
    for chunk in chunks:
        common = set.intersection(*[set(l) for l in chunk])
        print(common)
        c = next(iter(common))
        prio = ord(c) + 1 - (ord('a') if c.islower() else ord('A') - 26)
        res += prio
    return res


class TestPart1(unittest.TestCase):
    def test_sample(self):
        f = 'sample.txt'
        self.assertEqual(157, day1(f))
        self.assertEqual(70, day2(f))

    def test_input(self):
        f = 'input.txt'
        self.assertEqual(8072, day1(f))
        self.assertEqual(2567, day2(f))

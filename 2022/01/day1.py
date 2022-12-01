import unittest


def get_nums(filename):
    with open(filename) as f:
        return [[int(n) for n in l.splitlines()] for l in f.read().split('\n\n')]


def day1(chunks):
    return max([sum(chunk) for chunk in chunks])


def day2(chunks):
    return sum(sorted([sum(chunk) for chunk in chunks])[-3:])


class TestPart1(unittest.TestCase):
    def test0(self):
        nums = get_nums('sample.txt')
        self.assertEqual(day1(nums), 24000)
        self.assertEqual(day2(nums), 45000)

    def test1(self):
        nums = get_nums('input.txt')
        self.assertEqual(day1(nums), 69281)
        self.assertEqual(day2(nums), 201524)

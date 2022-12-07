import unittest


# def get_nums(filename):
#     with open(filename) as f:
#         return [[int(n) for n in l.splitlines()] for l in f.read().split('\n\n')]


def get_sums(filename):
    with open(filename) as f:
        return [sum([int(n) for n in l.splitlines()]) for l in f.read().split('\n\n')]


def part1(filename):
    return max(get_sums(filename))


def part2(filename):
    print(get_sums(filename))
    return sum(sorted(get_sums(filename))[-3:])


class TestPart1(unittest.TestCase):
    def test_sample(self):
        f = 'sample.txt'
        self.assertEqual(24000, part1(f))
        self.assertEqual(45000, part2(f))

    def test_input(self):
        f = 'input.txt'
        self.assertEqual(69281, part1(f))
        self.assertEqual(201524, part2(f))

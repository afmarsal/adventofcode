import unittest


# def get_nums(filename):
#     with open(filename) as f:
#         return [[int(n) for n in l.splitlines()] for l in f.read().split('\n\n')]


def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


def part1(filename):
    lines = get_lines(filename)
    res = 0
    for line in lines:
        only_digits = [d for d in line if d.isdigit()]
        line_val = int(only_digits[0]) * 10 + int(only_digits[-1])
        print(line_val)
        res += line_val
    return res


def part2(filename):
    print(get_lines(filename))
    return sum(sorted(get_lines(filename))[-3:])


class TestPart1(unittest.TestCase):
    def test_sample(self):
        f = 'sample.txt'
        self.assertEqual(142, part1(f))
        # self.assertEqual(45000, part2(f))

    def test_input(self):
        f = 'input.txt'
        self.assertEqual(53080, part1(f))
        # self.assertEqual(201524, part2(f))

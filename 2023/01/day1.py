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
        res += line_val
    return res

repl = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def part2(filename):
    lines = get_lines(filename)
    res = 0
    for line in lines:
        p = int(find_first_digit(line, False)) * 10
        p += int(find_first_digit(line[::-1], True))
        res += p
    return res


def find_first_digit(line, reversed):
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]
        for old, new in repl.items():
            old = old[::-1] if reversed else old
            if line[i:].startswith(old):
                return new
    return -1


class TestPart1(unittest.TestCase):
    def test_part1(self):
        f = 'sample.txt'
        self.assertEqual(142, part1(f))
        f = 'input.txt'
        self.assertEqual(53080, part1(f))

    def test_input(self):
        f = 'sample2.txt'
        self.assertEqual(281, part2(f))
        f = 'input.txt'
        self.assertEqual(53268, part2(f))
        # self.assertEqual(45000, part2(f))

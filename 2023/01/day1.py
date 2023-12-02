import re
import unittest


def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


def part1(filename):
    with open(filename) as f:
        text = f.read()
    return sum(int(nt[0] + nt[-1]) for nt in re.sub(r"[A-z]", "", text).split("\n"))
    # lines = get_lines(filename)
    # res = 0
    # for line in lines:
    #     re.sub(r'[A-z]', '', line)
    #     only_digits = [d for d in line if d.isdigit()]
    #     res += int(only_digits[0] + only_digits[-1])
    # return res


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
        first = find_first_digit(line, False)
        last = find_first_digit(line, True)
        res += int(first + last)
    return res


def find_first_digit(line, reverse):
    line = line[::-1] if reverse else line
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]
        for old, new in repl.items():
            old = old[::-1] if reverse else old
            if line[i:].startswith(old):
                return new
    return -1


class TestAll(unittest.TestCase):
    def test_part1(self):
        f = 'sample.txt'
        self.assertEqual(142, part1(f))
        f = 'input.txt'
        self.assertEqual(53080, part1(f))

    def test_part2(self):
        f = 'sample2.txt'
        self.assertEqual(281, part2(f))
        f = 'input.txt'
        self.assertEqual(53268, part2(f))

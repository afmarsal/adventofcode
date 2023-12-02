import re
import unittest


def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


load = {
    'red': 12,
    'green': 13,
    'blue': 14
}
def part1(filename):
    lines = get_lines(filename)
    res = 0
    for line in lines:
        invalid = False
        game_part, bags_part = line.split(':')
        game_id = int(game_part[len('Game '):])
        for hand in bags_part.split(';'):
            for draw in hand.split(','):
                n, c = draw.strip().split(' ')
                if load[c] < int(n):
                    invalid = True
                    break
            if invalid:
                break
        else:
            res += game_id

    return res


def part2(filename):

    return res

class TestAll(unittest.TestCase):
    def test_part1(self):
        f = 'sample.txt'
        self.assertEqual(8, part1(f))
        f = 'input.txt'
        self.assertEqual(53080, part1(f))

    def test_part2(self):
        f = 'sample2.txt'
        self.assertEqual(281, part2(f))
        f = 'input.txt'
        self.assertEqual(53268, part2(f))


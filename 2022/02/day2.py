import unittest

MAPPINGS = {
    'A': {'X': 3, 'Y': 6, 'Z': 0, 3: 'X', 6: 'Y', 0: 'Z'},
    'B': {'X': 0, 'Y': 3, 'Z': 6, 0: 'X', 3: 'Y', 6: 'Z'},
    'C': {'X': 6, 'Y': 0, 'Z': 3, 6: 'X', 0: 'Y', 3: 'Z'}
}

def read(filename):
    with open(filename) as f:
        return [tuple(n for n in l.split()) for l in f.read().splitlines()]

def play(m):
    # ord(g[1]) - ord('X') + 1 gives the score of the chosen shape
    return sum([MAPPINGS[g[0]][g[1]] + ord(g[1]) - ord('X') + 1 for g in m])

def part1(filename):
    return play(read(filename))

def part2(filename):
    # 3 * ord(g[1]) - ord('X') gives the required score
    required_shapes = [(g[0], MAPPINGS[g[0]][(3 * (ord(g[1]) - ord('X')))]) for g in read(filename)]
    return play(required_shapes)


class TestPart1(unittest.TestCase):
    def test_sample(self):
        f = 'sample.txt'
        self.assertEqual(15, part1(f))
        self.assertEqual(12, part2(f))

    def test_input(self):
        f = 'input.txt'
        self.assertEqual(14531, part1(f))
        self.assertEqual(11258, part2(f))

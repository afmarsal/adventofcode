import unittest

RESULTS = {
    'A': {'X': 3, 'Y': 6, 'Z': 0, 3: 'X', 6: 'Y', 0: 'Z'},
    'B': {'X': 0, 'Y': 3, 'Z': 6, 0: 'X', 3: 'Y', 6: 'Z'},
    'C': {'X': 6, 'Y': 0, 'Z': 3, 6: 'X', 0: 'Y', 3: 'Z'}
}

def read(filename):
    with open(filename) as f:
        return [tuple(n for n in l.split()) for l in f.read().splitlines()]


def day1(filename):
    # results = []
    # for g in read(filename):
    #     results.append(RESULTS[g[0]][g[1]] + ord(g[1]) - ord('X') + 1)
    # print(results)
    m = read(filename)
    return play(m)


def play(m):
    return sum([RESULTS[g[0]][g[1]] + ord(g[1]) - ord('X') + 1 for g in m])


def day2(filename):
    new_input = []
    for g in read(filename):
        expected_res = 3 * (ord(g[1]) - ord('X'))
        my_move = list(RESULTS[g[0]].keys())[list(RESULTS[g[0]].values()).index(expected_res)]
        new_input.append([g[0], my_move])
    print(new_input)
    return play(new_input)


class TestPart1(unittest.TestCase):
    def test_sample(self):
        f = 'sample.txt'
        self.assertEqual(15, day1(f))
        self.assertEqual(12, day2(f))

    def test_input(self):
        f = 'input.txt'
        self.assertEqual(14531, day1(f))
        self.assertEqual(11258, day2(f))

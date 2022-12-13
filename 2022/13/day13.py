import unittest

from numpy import sign


def read(filename):
    res = []
    with open(filename) as f:
        for pair in f.read().split('\n\n'):
            # print(pair)
            # print()
            # print('#{}#'.format(pair))
            # print('#{}#'.format(pair.splitlines()))
            l1, l2 = pair.splitlines()
            res.append((eval(l1), eval(l2)))
        return res
        return [(eval(l1), eval(l2)) for pair in f.read().split('\n\n') for l1, l2 in pair.splitlines()]

def log(param):
    print(param)
    pass


def compare(left, right):
    result = -1
    try:
        for i in range(len(left)):
            if i >= len(right):
                return -1

            if type(left[i]) == int and type(right[i]) == int:
                if left[i] == right[i]:
                    continue
                else:
                    result = sign(right[i] - left[i])
                    return result

            if type(left[i]) == list and type(right[i]) == list:
                result = compare(left[i], right[i])
                if result != 0:
                    return result
                continue

            if type(left[i]) == int and type(right[i]) == list:
                result = compare([left[i]], right[i])
                if result != 0:
                    return result
                continue

            if type(left[i]) == list and type(right[i]) == int:
                result = compare(left[i], [right[i]])
                if result != 0:
                    return result
                continue

        # All elements equal: left is shorter
        result = 0 if len(left) == len(right) else 1
        return result
    finally:
        log('Comparing {} vs {}. Result: {}'.format(left, right, result))

def part1(filename):
    pairs = read(filename)
    result = 0
    for i, (left, right) in enumerate(pairs):
        if compare(left, right) >= 0:
            log('{}: {}\n{}\n{}\n'.format(i, True, left, right))
            result += (i+1)
        else:
            log('{}: {}\n{}\n{}\n'.format(i, False, left, right))

    return result

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(13, part1('sample.txt'))

    def test_input(self):
        # 820 NO!
        self.assertEqual(-2, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

import unittest
from functools import cmp_to_key
from numpy import sign


def read(filename):
    with open(filename) as f:
        return [(eval(pair.splitlines()[0]), eval(pair.splitlines()[1])) for pair in f.read().split('\n\n')]

def log(param):
    # print(param)
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
    pairs = read(filename)
    packets = [p for pair in pairs for p in pair]
    packets.append([[2]])
    packets.append([[6]])
    # print('\n'.join(packets))
    sorted_packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
    # print('\n'.join(sorted_packets))
    idx2 = sorted_packets.index([[2]])
    idx6 = sorted_packets.index([[6]])
    return (idx2+1) * (idx6+1)


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(13, part1('sample.txt'))

    def test_input(self):
        # 820 NO!
        self.assertEqual(-2, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(140, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(21756, part2('input.txt'))

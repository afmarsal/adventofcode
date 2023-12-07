import unittest
import operator
import re
import functools
import operator as op
from collections import defaultdict
from pprint import pprint
from collections import Counter

def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


def log(param='', end='\n'):
    print(param, end=end)
    pass


def log_nolf(param):
    log(param, end='')


def compute_hand1(hand):
    d = sorted(Counter(hand).values())
    match d:
        case[_]:
            return 7
        case[1, 4]:
            return 6
        case[2, 3]:
            return 5
        case[1, 1, 3]:
            return 4
        case[1, 2, 2]:
            return 3
        case[1, 1, 1, 2]:
            return 2
        case _:
            return 1


def compute_hand2(hand):
    pprint(hand)
    counter = Counter(hand)
    most_used_card = counter.most_common(1)[0]
    if most_used_card[0] == 'J' and most_used_card[1] < 5:
        most_used_card = counter.most_common(2)[1]
    hand = hand.replace('J', most_used_card[0])
    counter = Counter(hand)
    d = sorted(counter.values())
    match d:
        case[_]:
            return 7
        case[1, 4]:
            return 6
        case[2, 3]:
            return 5
        case[1, 1, 3]:
            return 4
        case[1, 2, 2]:
            return 3
        case[1, 1, 1, 2]:
            return 2
        case _:
            return 1


def hand_value(hand, trans):
    trans = str.maketrans(trans)
    return int(hand.translate(trans), 16)


def calc(filename, hand_type, trans):
    scan = get_lines(filename)
    hands = [l.split() for l in scan]
    sorted_hands = sorted(hands, key=lambda x: hand_value(x[0], trans))
    sorted_hands = sorted(sorted_hands, key=lambda x: hand_type(x[0]))
    return sum((i + 1) * int(p[1]) for i, p in enumerate(sorted_hands))


def part1(filename):
    return calc(filename, compute_hand1,{'A': 'F', 'K': 'E', 'Q': 'D', 'J': 'C', 'T': 'B'})


def part2(filename):
    return calc(filename, compute_hand2, {'A': 'F', 'K': 'E', 'Q': 'D', 'J': '1', 'T': 'B'})


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(6440, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(254024898, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(5905, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(254115617, part2('input.txt'))

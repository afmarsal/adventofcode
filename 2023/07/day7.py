import unittest
import operator
import re
import functools
import operator as op
from collections import defaultdict
from pprint import pprint
from collections import Counter

TYPE_WEIGHT = 10000000000000
HAND_VALUES = {
    '5k': 7,
    '4k': 6,
    'fh': 5,
    '3k': 4,
    '2p': 3,
    '2k': 2,
    '1k': 1
}


def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


def log(param='', end='\n'):
    print(param, end=end)
    pass


def log_nolf(param):
    log(param, end='')


def group_hand(hand):
    dict1 = Counter(hand)
    res = defaultdict(set)
    for key, value in dict1.items():
        res[value].add(key)
    return res


def compute_hand1(p):
    hand, grouped_hand, bid = p
    if 5 in grouped_hand:
        type = '5k'
    elif 4 in grouped_hand:
        type = '4k'
    elif 3 in grouped_hand and 2 in grouped_hand:
        type = 'fh'
    elif 3 in grouped_hand:
        type = '3k'
    elif 2 in grouped_hand and len(grouped_hand[2]) == 2:
        type = '2p'
    elif 2 in grouped_hand:
        type = '2k'
    else:
        type = '1k'
    return HAND_VALUES[type] * TYPE_WEIGHT + hand_value(hand, "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2")


def compute_hand2(p):
    hand, grouped_hand, bid = p
    if 5 in grouped_hand:
        type = '5k'
    elif 4 in grouped_hand:
        if 'J' in hand:
            type = '5k'
        else:
            type = '4k'
    elif 3 in grouped_hand and 2 in grouped_hand:
        if 'J' in hand:
            type = '5k'
        else:
            type = 'fh'
    elif 3 in grouped_hand:
        if 'J' in grouped_hand[3] or 'J' in hand:
            # 3J or 1J
            type = '4k'
        else:
            type = '3k'
    elif 2 in grouped_hand and len(grouped_hand[2]) == 2:
        if 'J' in grouped_hand[2]:
            type = '4k'
        elif 'J' in hand:
            type = 'fh'
        else:
            type = '2p'
    elif 2 in grouped_hand:
        if 'J' in grouped_hand[2] or 'J' in hand:
            type = '3k'
        else:
            type = '2k'
    else:
        if 'J' in hand:
            type = '2k'
        else:
            type = '1k'
    return HAND_VALUES[type] * TYPE_WEIGHT + hand_value(hand, "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J")


def hand_value(hand, order):
    card_values = {c: i for i, c in enumerate(reversed(order.split(", ")))}
    hand_value = sum(pow(100, len(hand) - i) * card_values[c] for i, c in enumerate(hand))
    return hand_value


def calc(filename, compute_hand_func):
    scan = get_lines(filename)
    hands = []
    for i, line in enumerate(scan):
        hand, bid = line.split()
        hands.append((hand, group_hand(hand), int(bid)))
    sorted_hands = sorted(hands, key=lambda x: compute_hand_func(x))
    return sum((i + 1) * p[2] for i, p in enumerate(sorted_hands))


def part1(filename):
    return calc(filename, compute_hand1)

def part2(filename):
    return calc(filename, compute_hand2)


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

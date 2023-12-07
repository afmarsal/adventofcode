import unittest
import operator
import re
import functools
import operator as op
from collections import defaultdict
from pprint import pprint
from collections import Counter

TYPE_WEIGHT = 10000000000000


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


def hand_cards_values1(hand):
    card_values = {c: i for i, c in enumerate(reversed("A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")))}
    return sum(pow(100, len(hand)-i)*card_values[c] for i, c in enumerate(hand))

def hand_cards_values2(hand):
    card_values = {c: i for i, c in enumerate(reversed("A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")))}
    return sum(pow(100, len(hand)-i)*card_values[c] for i, c in enumerate(hand))


def compute_hand1(p):
    hand, grouped_hand, bid = p
    if 5 in grouped_hand:
        res = 7 * TYPE_WEIGHT + hand_cards_values1(hand)
    elif 4 in grouped_hand:
        res = 6 * TYPE_WEIGHT + hand_cards_values1(hand)
    elif 3 in grouped_hand and 2 in grouped_hand:
        res = 5 * TYPE_WEIGHT + hand_cards_values1(hand)
    elif 3 in grouped_hand:
        res = 4 * TYPE_WEIGHT + hand_cards_values1(hand)
    elif 2 in grouped_hand and len(grouped_hand[2]) == 2:
        res = 3 * TYPE_WEIGHT + hand_cards_values1(hand)
    elif 2 in grouped_hand:
        res = 2 * TYPE_WEIGHT + hand_cards_values1(hand)
    else:
        res = hand_cards_values1(hand)
    log(f'Evaluated {hand}: {res}')
    return res

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
    if type == '5k':
        res = 7 * TYPE_WEIGHT + hand_cards_values2(hand)
    elif type == '4k':
        res = 6 * TYPE_WEIGHT + hand_cards_values2(hand)
    elif type == 'fh':
        res = 5 * TYPE_WEIGHT + hand_cards_values2(hand)
    elif type == '3k':
        res = 4 * TYPE_WEIGHT + hand_cards_values2(hand)
    elif type == '2p':
        res = 3 * TYPE_WEIGHT + hand_cards_values2(hand)
    elif type == '2k':
        res = 2 * TYPE_WEIGHT + hand_cards_values2(hand)
    else:
        res = hand_cards_values2(hand)
    log(f'Evaluated {hand}: {res}')
    return res

def part1(filename):
    scan = get_lines(filename)
    hands = []
    for i, line in enumerate(scan):
        hand, bid = line.split()
        hands.append((hand, group_hand(hand), int(bid)))
    sorted_hands = sorted(hands, key=lambda x: compute_hand1(x))
    return sum((i+1)*p[2] for i, p in enumerate(sorted_hands))

def part2(filename):
    scan = get_lines(filename)
    hands = []
    for i, line in enumerate(scan):
        hand, bid = line.split()
        hands.append((hand, group_hand(hand), int(bid)))
    sorted_hands = sorted(hands, key=lambda x: compute_hand2(x))
    return sum((i+1)*p[2] for i, p in enumerate(sorted_hands))

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(6440, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(254024898, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(5905, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

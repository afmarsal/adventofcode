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
    res = defaultdict(list)
    for key, value in dict1.items():
        res[value].append(key)
    return res


def hand_cards_values1(hand):
    card_values = {c: i for i, c in enumerate(reversed("A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")))}
    l = [pow(100, len(hand)-i-1)*card_values[c] for i, c in enumerate(hand)]
    log(f'{hand}: {l}')
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

def part1(filename):
    scan = get_lines(filename)
    hands = []
    for i, line in enumerate(scan):
        hand, bid = line.split()
        hands.append((hand, group_hand(hand), int(bid)))
    sorted_hands = sorted(hands, key=lambda x: compute_hand1(x))
    return sum((i+1)*p[2] for i, p in enumerate(sorted_hands))

def part2(filename):
    return -1


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

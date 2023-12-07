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


def compute_value(hand, jokers):
    j_val = '1' if jokers else 'C'
    trans = {'A': 'F', 'K': 'E', 'Q': 'D', 'J': j_val, 'T': 'B'}
    trans = str.maketrans(trans)
    return int(hand.translate(trans), 16)


# def compute_type(hand, jokers):
#     counter = Counter(hand)
#     if jokers:
#         most_used_card = counter.most_common(1)[0]
#         if most_used_card[0] == 'J' and most_used_card[1] < 5:
#             most_used_card = counter.most_common(2)[1]
#         hand = hand.replace('J', most_used_card[0])
#         counter = Counter(hand)
#     d = sorted(counter.values())
#     match d:
#         case[_]:
#             return 7
#         case[1, 4]:
#             return 6
#         case[2, 3]:
#             return 5
#         case[1, 1, 3]:
#             return 4
#         case[1, 2, 2]:
#             return 3
#         case[1, 1, 1, 2]:
#             return 2
#         case _:
#             return 1

def compute_type2(hand, jokers):
    counter = Counter(hand)
    if jokers:
        most_used_card = counter.most_common(1)[0]
        if most_used_card[0] == 'J' and most_used_card[1] < 5:
            most_used_card = counter.most_common(2)[1]
        hand = hand.replace('J', most_used_card[0])
        counter = Counter(hand)
    # Sequences are sorted lexicographically
    # This generates lists like [5], [2, 2, 1], etc with freq of cards
    return list(reversed(sorted(counter.values())))

def calc(filename, jokers):
    scan = get_lines(filename)
    hands = [line.split() for line in scan]
    sorted_hands = sorted(hands, key=lambda x: compute_value(x[0], jokers))
    sorted_hands = sorted(sorted_hands, key=lambda x: compute_type2(x[0], jokers))
    return sum((i + 1) * int(p[1]) for i, p in enumerate(sorted_hands))


def part1(filename):
    return calc(filename, False)


def part2(filename):
    return calc(filename, True)


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

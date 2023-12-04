import operator
import re
import unittest
import functools
import operator as op
from collections import defaultdict


def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


def part1(filename):
    lines = get_lines(filename)
    res = 0
    for line in lines:
        cards = line.split(':')[1]
        winners, numbers = cards.split('|')
        winners = {s.strip() for s in winners.split()}
        numbers = {s.strip() for s in numbers.split()}
        print(f'w: {winners}, n: {numbers}')
        combo = len(winners.intersection(numbers))
        print(f'c: {combo}')
        if combo > 0:
            res += pow(2, combo - 1)
    return res


def part2(filename):
    lines = get_lines(filename)
    res = 1
    total_cards = [1] * len(lines)
    for i, line in enumerate(lines):
        cards = line.split(':')[1]
        winners, numbers = cards.split('|')
        winners = {s.strip() for s in winners.split()}
        numbers = {s.strip() for s in numbers.split()}
        combo = len(winners.intersection(numbers))
        print(f'i: {i+1}, w: {winners}, n: {numbers}, c:{combo}')
        for j in range(i+1, i+1+combo):
            total_cards[j] += total_cards[i]
        print(f'tc: {total_cards}')
    return sum(total_cards)


class TestAll(unittest.TestCase):
    def test_part1(self):
        f = 'sample.txt'
        self.assertEqual(13, part1(f))
        f = 'input.txt'
        self.assertEqual(19135, part1(f))

    def test_part2(self):
        f = 'sample.txt'
        self.assertEqual(30, part2(f))
        f = 'input.txt'
        self.assertEqual(5704953, part2(f))


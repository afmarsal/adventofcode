import itertools
import math
import operator
import unittest
import re
from collections import namedtuple, Counter


def parse_input(lines):
    result = [int(i) for i in lines]
    return sorted(result, reverse=True)


def solve(lines, top):
    capacities = parse_input(lines)
    print(f'Capacities: {capacities}')
    combos = 0
    stack = []
    idx = 0
    accum = 0
    while True:
        partial = accum + capacities[idx]
        # print(f'Partial: {partial}, accum: {accum}, capacity: {capacities[idx]}, combos: {combos}, Stack: {[capacities[idx] for idx in stack]}')
        if partial == top:
            combos += 1
        elif partial < top:
            stack.append(idx)
            accum = partial
        idx += 1
        if idx >= len(capacities):
            idx = stack.pop()
            accum -= capacities[idx]
            idx += 1
            if idx >= len(capacities):
                if len(stack) == 0:
                    return combos
                idx = stack.pop()
                accum -= capacities[idx]
                idx += 1


def part1(lines, top):
    return solve(lines, top)


def part2(lines, top):
    pass


class TestPart1(unittest.TestCase):
    def test_sample(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part1(lines, 25), 4)

    def test_input1(self):
        with open('input_part1.txt') as f:
            lines = f.read().splitlines()
            # Not 5
            self.assertEqual(part1(lines, 150), 4372)


class TestPart2(unittest.TestCase):
    def test2(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part2(lines), 241)


if __name__ == '__main__':
    unittest.main()

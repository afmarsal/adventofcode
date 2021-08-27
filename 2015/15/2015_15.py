import itertools
import math
import operator
import unittest
import re
from collections import namedtuple, Counter

# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
regex = r'(\w+): capacity (-{0,1}\d+), durability (-{0,1}\d+), flavor (-{0,1}\d+), texture (-{0,1}\d+), calories (' \
        r'-{0,1}\d+)'


class TeaspoonInfo(namedtuple('TeaspoonInfo', ['capacity', 'durability', 'flavour', 'texture', 'calories'])):
    __slots__ = ()

    def __add__(self, other):
        return TeaspoonInfo._make(map(operator.add, tuple(self), tuple(other)))

    def __mul__(self, other):
        return TeaspoonInfo._make([f*other for f in tuple(self)])

    def score(self):
        # Remove "calories" for now
        fields = list(self)[:-1]
        if all(v > 0 for v in fields):
            return math.prod(fields)
        else:
            return 0


def parse_input(lines):
    result = dict()
    for line in lines:
        m = re.fullmatch(regex, line)
        if not m:
            raise RuntimeError(f'line "{line}" does not match')
        result[m[1]] = TeaspoonInfo(*tuple(map(int, m.groups()[1:])))
    return result


def solve(lines, total_spoons, matching_calories=None):
    teaspoons = parse_input(lines)
    results = []
    for combo in itertools.combinations_with_replacement(teaspoons.keys(), total_spoons):
        teaspoon_total = TeaspoonInfo(*([0] * 5))
        counter = Counter(combo)
        for ingredient, reps in counter.items():
            teaspoon_total = teaspoon_total + (teaspoons[ingredient] * reps)
        if matching_calories is None or teaspoon_total.calories == matching_calories:
            results.append(teaspoon_total.score())

    # print(results)
    return max(results)


def part1(lines, total_spoons):
    res = solve(lines, total_spoons)
    return res


def part2(lines, elapsed_sec):
    res = solve(lines, elapsed_sec, 500)
    return res


class TestPart1(unittest.TestCase):
    def test10(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part1(lines, 100), 62842880)

    def test1(self):
        with open('input_part1.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part1(lines, 100), 13882464)


class TestPart2(unittest.TestCase):
    def test20(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part2(lines, 100), 57600000)

    def test2(self):
        with open('input_part1.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part2(lines, 100), 11171160)


if __name__ == '__main__':
    unittest.main()

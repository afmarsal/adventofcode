import unittest
import re
import itertools as it
from collections import deque

regex = r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\.'


def sort_permutation(p):
    first = min(p)
    dq = deque(p)
    while dq[0] != first:
        dq.rotate()
    return dq, ','.join(dq)


def calc_score(dq, rules):
    def prev(i):
        return dq[i - 1] if i > 0 else dq[len(dq) - 1]

    def next(i):
        return dq[i + 1] if i < len(dq) - 1 else dq[0]

    print(f'Processing combo: {",".join(dq)}')
    total_score = 0
    for i, character in enumerate(dq):
        score1 = rules[(character, prev(i))]
        score2 = rules[(character, next(i))]
        # print(f'Processing {i} -> {character}. Prev: {prev(i)} Score: {score1}')
        # print(f'Processing {i} -> {character}. Next: {next(i)} Score: {score2}')
        total_score += score1 + score2
    # print(f'Combo score: {",".join(dq)} -> {total_score}')
    return total_score


def part1(lines):
    characters, rules = make_rules(lines)
    seen = set()
    combos = {}
    for p in it.permutations(characters, len(characters)):
        dq, dq_str = sort_permutation(p)
        if dq_str not in seen:
            combos[dq_str] = dq
            seen.add(dq_str)

    scores = {}
    for dq_str, dq in combos.items():
        scores[dq_str] = calc_score(dq, rules)

    return max(scores.values())


def make_rules(lines):
    def f(w):
        return 1 if w == 'gain' else -1

    rules = dict()
    characters = set()
    for line in lines:
        m = re.fullmatch(regex, line)
        if not m:
            raise RuntimeError(f'Invalid line {line}')
        rules[(m[1], m[4])] = f(m[2]) * int(m[3])
        characters.add(m[1])
    return characters, rules


class TestPart1(unittest.TestCase):
    def test10(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part1(lines), 330)

    def test1(self):
        with open('input.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part1(lines), 664)


if __name__ == '__main__':
    unittest.main()

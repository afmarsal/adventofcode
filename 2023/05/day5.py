import itertools
import unittest
import operator
import re
import functools
import operator as op
from collections import defaultdict

def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')

def part1(filename):
    scan = get_lines(filename)
    seeds = [int(n.strip()) for n in scan[0].split(':')[1].split()]
    chunks = defaultdict(list)
    scan = scan[2:]
    start = True
    for i in range(len(scan)):
        if scan[i].strip() == '':
            start = True
            continue
        if start:
            nl = re.match(r'([^-]+)-to-([^ ]+)', scan[i])
            if not nl:
                raise Exception(f'{scan[i]} not matched')
            c1, c2 = nl[1], nl[2]
            start = False
            continue
        numbers = [int(n.strip()) for n in scan[i].split()]
        chunks[c1].append((c2, numbers))

    locations = seeds[:]
    for i, seed in enumerate(seeds):
        log(f'Seed {seed}')
        next_map = 'seed'
        while next_map != 'location':
            curr_map = next_map
            for rng in chunks[curr_map]:
                next_map, (dst, src, l) = rng
                # log(f'Processing {seed} in {curr_map} -> {dst}, {src}, {l}')
                offset = locations[i] - src
                if 0 <= offset < l:
                    locations[i] = dst + offset
                    log(f'Found location {i}: {seed}, nxt map:{next_map}, new location:{locations[i]}')
                    break
            else:
                log(f'Not Found location {i}: {seed}, nxt map:{next_map}, keep location:{locations[i]}')
    print(locations)
    return min(locations)

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(35, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(579439039, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

import unittest
import operator
import re
import functools
import operator as op
from collections import defaultdict
from pprint import pprint

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
    instructions = scan[0]
    nodes = dict()
    for line in scan[2:]:
        match = re.match(r'(\w{3}) = \((\w{3}), (\w{3})\)', line)
        nodes[match[1]] = {'L': match[2], 'R': match[3]}

    steps = 0
    cur_node = 'AAA'
    while cur_node != 'ZZZ':
        lr = instructions[steps % len(instructions)]
        cur_node = nodes[cur_node][lr]
        steps += 1
    return steps

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(2, part1('sample1.txt'))

    def test_input(self):
        self.assertEqual(-2, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

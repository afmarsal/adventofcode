import unittest
import operator
import re
import functools
import operator as op
from collections import defaultdict
from pprint import pprint
import math

def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')

def get_nodes(filename):
    scan = get_lines(filename)
    instructions = scan[0]
    nodes = dict()
    for i, line in enumerate(scan[2:]):
        match = re.match(r'(\w{3}) = \((\w{3}), (\w{3})\)', line)
        nodes[match[1]] = {'L': match[2], 'R': match[3]}
    return instructions, nodes


def part1(filename):
    instructions, nodes = get_nodes(filename)

    steps = 0
    cur_node = 'AAA'
    while cur_node != 'ZZZ':
        lr = instructions[steps % len(instructions)]
        cur_node = nodes[cur_node][lr]
        steps += 1
    return steps


def find_cycle(instructions, nodes, cur_node):
    steps = 0
    # Store list of visited node + direction
    visited = []
    while True:
        lr = instructions[steps % len(instructions)]
        if cur_node.endswith('Z') and (cur_node, 'lr') in visited:
            idx = visited.index((cur_node, 'lr'))
            log(f'Found final node {cur_node}[{lr}] at {idx} cycle: {len(visited)-idx}')
            return idx, len(visited) - idx
        # log(f'Visited {cur_node}[{lr}] -> {nodes[cur_node][lr]}. Past: {visited}')
        visited.append((cur_node, 'lr'))
        cur_node = nodes[cur_node][lr]
        steps += 1
    pass

def part2(filename):
    instructions, nodes = get_nodes(filename)
    a_nodes = [node for node in nodes.keys() if node.endswith('A')]
    cycles = [find_cycle(instructions, nodes, a_node) for a_node in a_nodes]
    lcm = math.lcm(*[p2 for _, p2 in cycles])

    return lcm


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(2, part1('sample1.txt'))

    def test_input(self):
        self.assertEqual(15989, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(6, part2('sample3.txt'))

    def test_input(self):
        self.assertEqual(13830919117339, part2('input.txt'))

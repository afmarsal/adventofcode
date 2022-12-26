import functools
import itertools as iter
import unittest
import re
import dataclasses

import networkx as nx

def read(filename):
    with open(filename) as f:
        reg = re.compile(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)')
        scan = {}
        for line in f.read().splitlines():
            m = reg.match(line)
            scan[m[1]] = Node(int(m[2]), list(map(str.strip, m[3].split(','))))
        return scan

@dataclasses.dataclass
class Node:
    rate: int
    children: list

def log(param='', end='\n'):
    # print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')

TOTAL_MINUTES = 30

def build_graph(scan):
    graph = nx.DiGraph()
    for node in scan:
        graph.add_node(node, rate=scan[node].rate)
        for child in scan[node].children:
            graph.add_edge(node, child)
    return graph


@functools.cache
def best_path(graph, valve1, valve2):
    return len(nx.shortest_path(graph, valve1, valve2)) - 1

def best_path_cost(graph, remaining_minutes, curr_node, remaning_nodes, curr_path):
    if len(remaning_nodes) == 0:
        return 0
    else:
        costs = []
        for node in remaning_nodes:
            c = best_path(graph, curr_node, node)
            next_remaining_minutes = remaining_minutes - (c + 1)
            if next_remaining_minutes <= 0:
                continue
            release = next_remaining_minutes * graph.nodes[node]['rate']
            next_remaning_nodes = tuple(set(remaning_nodes) - {node})
            next_path = curr_path + [node]
            log(f'Cost from {curr_node} to {node}. Release: {release} = {remaining_minutes} * '
                f'{graph.nodes[node]["rate"]}. Recursing: {node} -> {next_remaning_nodes}')
            cost = release + best_path_cost(graph, next_remaining_minutes, node, next_remaning_nodes, next_path)
            costs.append((remaning_nodes, cost))
            log(f'Cost from {curr_node} to {node}. Release: {release}, cost: {cost}')
        if len(costs) == 0:
            return 0
        return max(c for p, c in costs)

def part1(filename):
    scan = read(filename)
    graph = build_graph(scan)
    valves = {k for k, v in scan.items() if v.rate > 0}
    return best_path_cost(graph, TOTAL_MINUTES, 'AA', tuple(valves), ['AA'])

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1651, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(1820, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

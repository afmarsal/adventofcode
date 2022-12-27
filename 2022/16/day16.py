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

def best_path_cost1(graph, remaining_minutes, curr_node, remaning_nodes, curr_path):
    if len(remaning_nodes) == 0:
        return 0
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
        cost = release + best_path_cost1(graph, next_remaining_minutes, node, next_remaning_nodes, next_path)
        costs.append((remaning_nodes, cost))
        log(f'Cost from {curr_node} to {node}. Release: {release}, cost: {cost}')
    if len(costs) == 0:
        return 0
    return max(c for p, c in costs)

def part1(filename):
    scan = read(filename)
    graph = build_graph(scan)
    valves = {k for k, v in scan.items() if v.rate > 0}
    return best_path_cost1(graph, 30, 'AA', tuple(valves), ['AA'])

def best_path_cost2(graph, min1, min2, curr_node1, curr_node2, remaning_nodes, curr_path1, curr_path2):
    if len(remaning_nodes) == 0:
        return 0
    costs = []
    if min1 >= min2:
        remaining_minutes = min1
        curr_node = curr_node1
        advance1 = True
    else:
        remaining_minutes = min2
        curr_node = curr_node2
        advance1 = False
    log(f'Advancing1: {advance1}. min1: {min1}, min2: {min2}, node1: {curr_node1}, node2: {curr_node2}')
    for node in remaning_nodes:
        c = best_path(graph, curr_node, node)
        next_remaining_minutes = remaining_minutes - (c + 1)
        if next_remaining_minutes <= 0:
            continue
        if advance1:
            next_min1 = next_remaining_minutes
            next_min2 = min2
            next_node1 = node
            next_node2 = curr_node2
            next_path1 = curr_path1 + [node]
            next_path2 = curr_path2
        else:
            next_min1 = min1
            next_min2 = next_remaining_minutes
            next_node1 = curr_node1
            next_node2 = node
            next_path1 = curr_path1
            next_path2 = curr_path2 + [node]
        release = next_remaining_minutes * graph.nodes[node]['rate']
        next_remaning_nodes = tuple(set(remaning_nodes) - {node})
        log(f'Cost from {curr_node} to {node}. Release: {release} = {remaining_minutes} * '
            f'{graph.nodes[node]["rate"]}. Recursing: {node} -> {next_remaning_nodes}')
        cost = release + best_path_cost2(graph, next_min1, next_min2, next_node1, next_node2, next_remaning_nodes, next_path1, next_path2)
        costs.append((remaning_nodes, cost))
        log(f'Cost from {curr_node} to {node}. Release: {release}, cost: {cost}')
    if len(costs) == 0:
        return 0
    return max(c for p, c in costs)

def part2(filename):
    scan = read(filename)
    graph = build_graph(scan)
    valves = {k for k, v in scan.items() if v.rate > 0}
    return best_path_cost2(graph, 26, 26, 'AA', 'AA', tuple(valves), ['AA'], ['AA'])


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1651, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(1820, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1707, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(2602, part2('input.txt'))

import re
import itertools as it


def make_key(node1, node2):
    return f'{node1}-{node2}' if node1 > node2 else f'{node2}-{node1}'


def calc_dist(paths, route):
    return sum(paths[make_key(route[i], route[i + 1])] for i in range(len(route) - 1))


def parse_routes_and_paths(lines):
    paths = dict()
    nodes = set()
    for line in lines:
        node1, node2, dist = re.fullmatch(r'(\w+) to (\w+) = (\d+)', line).groups()
        nodes.update({node1, node2})
        paths[make_key(node1, node2)] = int(dist)
    return nodes, paths


def calc_route(lines, f):
    nodes, paths = parse_routes_and_paths(lines)
    return f(calc_dist(paths, route) for route in it.permutations(nodes, len(nodes)))


def part1(lines):
    return calc_route(lines, min)

def part2(lines):
    return calc_route(lines, max)


sample = '''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
'''
assert part1(sample.splitlines()) == 605

lines = open('input.txt').read().splitlines()
assert part1(lines) == 207
print(f'# Part 1: {part1(lines)}')

assert part2(sample.splitlines()) == 982
assert part2(lines) == 804
print(f'# Part 2: {part2(lines)}')

# Part 1: 207
# Part 2: 804

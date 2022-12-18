import sys
import unittest
import networkx

def read(filename):
    with open(filename) as f:
        return [eval(f'({line})') for line in f.read().splitlines()]

def log(param='', end='\n'):
    # print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')

def dist(cube1, cube2):
    return sum(abs(c1 - c2) for c1, c2 in zip(cube1, cube2))

def part1(filename):
    inp = read(filename)
    # for each pair of connected cube, sum 2 sides that are connected
    connected = sum(2 for i, cube1 in enumerate(inp) for cube2 in inp[i+1:] if dist(cube1, cube2) == 1)
    return len(inp) * 6 - connected

def add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2]

def neighbors(cube):
    offsets = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    result = []
    for offset in offsets:
        neighbor = add(cube, offset)
        result.append(neighbor)
    return result


def part2(filename):
    # Idea
    # Build a graph of connected free cells with surrounding box a bit "bigger"
    # than provided cubes
    # Then for each cube check if neighbor has a path to a "known free cube" (asssumed 1,1,1)
    inp = read(filename)
    all_cubes = set(inp)
    min_x, min_y, min_z = sys.maxsize, sys.maxsize, sys.maxsize
    max_x, max_y, max_z = 0, 0, 0
    for x, y, z in inp:
        min_x, max_x = min(x, min_x), max(x, max_x)
        min_y, max_y = min(y, min_y), max(y, max_y)
        min_z, max_z = min(z, min_z), max(z, max_z)
    g = networkx.Graph()
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                cube = (x, y, z)
                if cube in all_cubes:
                    continue
                g.add_node(cube)
                for neighbor in neighbors(cube):
                    if neighbor not in all_cubes:
                        g.add_edge(cube, neighbor)
    connected = 0
    free_node = (1, 1, 1)
    for cube in inp:
        log()
        for neighbor in neighbors(cube):
            log(f'Cube: {cube} -> {neighbor}')
            if neighbor in all_cubes:
                continue
            # connected += 1  # Uncomment for part 1
            if networkx.has_path(g, neighbor, free_node):
                # neighbor not in nodes means it was blocked by the cube, but on the outside
                if neighbor not in g.nodes:
                    log(f'node outside: {neighbor}')
                connected += 1
            else:
                log(f'No path {cube} -> {neighbor}')

    return connected

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(64, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(4332, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(58, part2('sample.txt'))

    def test_input(self):
        # 2519 too low
        self.assertEqual(2524, part2('input.txt'))

import unittest
import networkx as nx

def log(param):
    print(param)
    pass


def read(filename):
    with open(filename) as f:
        grid = [list(l) for l in f.read().splitlines()]
        return {(j, i): grid[j][i] for j in range(len(grid)) for i in range(len(grid[j]))}


UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

def find(grid, char):
    return find_all(grid, char)[0]

def find_all(grid, char):
    return [k for k, v in grid.items() if v == char]

def find_neighbors1(grid, node):
    result = set()
    for n in [UP, DOWN, LEFT, RIGHT]:
        nxt = (node[0] + n[0], node[1] + n[1])
        if nxt in grid \
                and ((grid[node] == 'S' and grid[nxt] in {'a', 'b'})
                     or (grid[nxt] == 'E' and grid[node] in {'z', 'y'})
                     or (grid[nxt] not in {'S', 'E'} and ord(grid[nxt]) <= ord(grid[node]) + 1)):
            result.add(nxt)
    return result

def find_neighbors2(grid, node):
    result = set()
    for n in [UP, DOWN, LEFT, RIGHT]:
        nxt = (node[0] + n[0], node[1] + n[1])
        if nxt in grid \
                and ((grid[node] == 'E' and grid[nxt] in {'z', 'y'})
                     or (grid[nxt] == 'S' and grid[node] in {'a', 'b'})
                     or (grid[node] not in {'S', 'E'} and ord(grid[nxt]) >= ord(grid[node]) - 1)):
            result.add(nxt)
    return result

def part1(filename):
    grid = read(filename)
    graph = nx.DiGraph()
    s_pos = find(grid, 'S')
    e_pos = find(grid, 'E')
    for curr in grid:
        neighbors = find_neighbors1(grid, curr)
        for n in neighbors:
            graph.add_edge(curr, n)
    path = nx.algorithms.shortest_path(graph, s_pos, e_pos)
    return len(path) - 1

def part2(filename):
    grid = read(filename)
    graph = nx.DiGraph()
    e_pos = find(grid, 'E')
    for curr in grid:
        neighbors = find_neighbors2(grid, curr)
        for n in neighbors:
            graph.add_edge(curr, n)
    paths = []
    for a in find_all(grid, 'a'):
        try:
            shortest_path = nx.algorithms.shortest_path(graph, e_pos, a)
        except Exception as e:
            log('Exception with node {}: {}'.format(a, e))

        paths.append(shortest_path)
    return min(len(path) for path in paths) - 1

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(31, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(420, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(29, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(414, part2('input.txt'))

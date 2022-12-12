import unittest
import networkx.algorithms
import networkx as nx

def log(param):
    print(param)
    pass


MAX_J = -1
MAX_I = -1
def read(filename):
    global MAX_J
    global MAX_I
    with open(filename) as f:
        grid = [list(l) for l in f.read().splitlines()]
        MAX_J = len(grid)
        MAX_I = len(grid[0])
        return {(j, i): grid[j][i] for j in range(len(grid)) for i in range(len(grid[j]))}


UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)


def find(grid, char):
    for k, v in grid.items():
        if v == char:
            return k

def find_all(grid, char):
    return [k for k, v in grid.items() if v == char]


def find_next(grid, visited, node):
    result = set()
    for n in [UP, DOWN, LEFT, RIGHT]:
        nxt = (node[0] + n[0], node[1] + n[1])
        if nxt in grid \
                and nxt not in visited \
                and ((grid[node] == 'S' and grid[nxt] == 'a')
                     or (grid[nxt] == 'E' and grid[node] == 'z')
                     or (grid[nxt] != 'E' and ord(grid[nxt]) <= ord(grid[node]) + 1)):
            result.add(nxt)
    log('{} -> {}, next:'.format(node, grid[node]))
    print_pending('   ', result, grid)
    return result

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

def print_pending(steps, pending, grid):
    log('{}: {} '.format(steps, ', '.join(['{}:{}'.format(p, grid[p]) for p in pending])))


# def part1(filename):
#     grid = read(filename)
#     s_pos = find(grid, 'S')
#     e_pos = find(grid, 'E')
#     log('Route {} -> {}\n'.format(s_pos, e_pos))
#     curr_pos = s_pos
#     visited = {curr_pos}
#     pending = find_next(grid, visited, curr_pos)
#     steps = 0
#     while True:
#         nxt_pending = set()
#         steps += 1
#         print_pending(steps, pending, grid)
#         print()
#         for p in pending:
#             visited.add(p)
#             if grid[p] == 'E':
#                 return steps
#             else:
#                 nxt_pending.update(find_next(grid, visited, p))
#         pending = nxt_pending


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
        shortest_path = nx.algorithms.shortest_path(graph, e_pos, a)
        log('Route {} -> {}\nPath {}: {}'.format(e_pos, a, len(shortest_path), shortest_path))
        paths.append(shortest_path)
    return min(len(path) for path in paths) - 1

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(31, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(420, part1('input.txt'))
        self.assertEqual(339, part1('input2.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(29, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

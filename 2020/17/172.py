import itertools
import operator


DELTAS = [c for c in itertools.product((0, 1, -1), repeat=4) if c != (0, 0, 0, 0)]


def neighbours(coord):
    return (tuple(map(operator.add, delta, coord)) for delta in DELTAS)


def calc_next(grid):
    next_coord = {neighbour for coord in grid for neighbour in neighbours(coord)}
    next_grid = {}
    # print(next_coord)
    for coord in next_coord:
        active = sum(grid.get(n, '.') == '#' for n in neighbours(coord))
        if grid.get(coord, '.') == '#':
            if 2 <= active <= 3:
                next_grid[coord] = '#'
            else:
                next_grid[coord] = '.'
        else:
            next_grid[coord] = '#' if active == 3 else '.'
    # print(next_grid)
    return next_grid


def do_it(filename, times):
    with open(filename) as f:
        lines = list(map(str.strip, f.readlines()))

    grid = {(i, j, 0, 0): c for i, line in enumerate(lines) for j, c in enumerate(line)}
    for i in range(times):
        next_grid = calc_next(grid)
        grid = next_grid
    return sum(c == '#' for c in grid.values())


if __name__ == '__main__':
    output = do_it('input1.txt', 6)
    print(f'Result: {output}')

# Result: 2240

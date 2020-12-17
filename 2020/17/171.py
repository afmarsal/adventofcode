import itertools
import operator
import util


def neighbours(coord, deltas):
    return (tuple(map(operator.add, delta, coord)) for delta in deltas)


def calc_next(grid, deltas):
    next_coord = {n for coord in grid for n in neighbours(coord, deltas)}
    next_grid = {}
    for coord in next_coord:
        active = sum(grid.get(n, '.') == '#' for n in neighbours(coord, deltas))
        if grid.get(coord, '.') == '#':
            next_grid[coord] = '#' if 2 <= active <= 3 else '.'
        else:
            next_grid[coord] = '#' if active == 3 else '.'
    return next_grid


def do_it(grid, deltas):
    for i in range(6):
        grid = calc_next(grid, deltas)
    return sum(c == '#' for c in grid.values())


if __name__ == '__main__':
    filelines = util.lines('input1.txt')

    deltas3d = [c for c in itertools.product((0, 1, -1), repeat=3) if c != (0, 0, 0)]
    grid3d = {(i, j, 0): c for i, line in enumerate(filelines) for j, c in enumerate(line)}
    output = do_it(grid3d, deltas3d)
    print(f'Part 1: {output}')

    deltas4d = [c for c in itertools.product((0, 1, -1), repeat=4) if c != (0, 0, 0, 0)]
    grid4d = {(i, j, 0, 0): c for i, line in enumerate(filelines) for j, c in enumerate(line)}
    output = do_it(grid4d, deltas4d)
    print(f'Part 2: {output}')

# Part 1: 284
# Part 2: 2240


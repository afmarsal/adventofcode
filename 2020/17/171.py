import itertools
import operator


def neighbours(coord, deltas):
    return (tuple(map(operator.add, delta, coord)) for delta in deltas)


def calc_next(grid, deltas):
    next_coord = {n for coord in grid for n in neighbours(coord, deltas)}
    next_grid = set()
    for coord in next_coord:
        active = sum(n in grid for n in neighbours(coord, deltas))
        if coord in grid and 2 <= active <= 3:
            next_grid.add(coord)
        elif coord not in grid and active == 3:
            next_grid.add(coord)
    return next_grid


def do_it(grid, deltas):
    for i in range(6):
        grid = calc_next(grid, deltas)
    return len(grid)


if __name__ == '__main__':
    with open('input1.txt') as f:
        filelines = list(map(str.strip, f))

    # grid is a set of active coordinates
    deltas3d = [c for c in itertools.product((0, 1, -1), repeat=3) if c != (0, 0, 0)]
    grid3d = {(i, j, 0) for i, line in enumerate(filelines) for j, c in enumerate(line) if c == '#'}
    output = do_it(grid3d, deltas3d)
    print(f'Part 1: {output}')

    deltas4d = [c for c in itertools.product((0, 1, -1), repeat=4) if c != (0, 0, 0, 0)]
    grid4d = {(i, j, 0, 0) for i, line in enumerate(filelines) for j, c in enumerate(line) if c == '#'}
    output = do_it(grid4d, deltas4d)
    print(f'Part 2: {output}')

# Part 1: 284
# Part 2: 2240


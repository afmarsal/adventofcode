import sys
from operator import add


def parse_instructions(line):
    idx = 0
    instructions = []
    while idx < len(line):
        if line[idx] in {'e', 'w'}:
            instructions.append(line[idx])
            idx += 1
        else:
            instructions.append(line[idx] + line[idx + 1])
            idx += 2
    return instructions


DELTAS = {
    'e': lambda x: tuple(map(add, (2, 0), x)),
    'w': lambda x: tuple(map(add, (-2, 0), x)),
    'ne': lambda x: tuple(map(add, (1, 1), x)),
    'se': lambda x: tuple(map(add, (1, -1), x)),
    'nw': lambda x: tuple(map(add, (-1, 1), x)),
    'sw': lambda x: tuple(map(add, (-1, -1), x)),
}


def starting_grid(lines):
    grid = set()
    for line in lines:
        instructions = parse_instructions(line)
        curr = (0, 0)
        for op in instructions:
            curr = DELTAS[op](curr)
        if curr in grid:
            grid.remove(curr)
        else:
            grid.add(curr)
    return grid


def adjacent(tile):
    return {d(tile) for d in DELTAS.values()}


def do_it(lines):
    grid = starting_grid(lines)
    print(f'--- Day 0: {len(grid)}')
    print(f'--- Day 0: {grid}')
    for i in range(100):
        new_grid = set()
        to_check = {tile: 'black' for tile in grid}
        to_check.update({a: 'white' for tile in grid for a in adjacent(tile) if a not in to_check})
        for tile, color in to_check.items():
            black_adj = sum(a in grid for a in (adjacent(tile)))
            # print(f'Adjacent to {tile}: {black_adj}')
            # for a in adjacent(tile):
            #     if a in grid:
            #         print(f'{tile} adj to {a}')
            if color == 'black':
                # print(f'Black {tile} -> black adj: {black_adj} adj: {adj}, grid: {grid}')
                if 1 <= black_adj <= 2:
                    # print(f'Black {tile}')
                    new_grid.add(tile)
                    # print(f'{tile} will be black')

            else:  # color white
                # print(f'White check {tile} -> black adj: {black_adj} -> adj: {adj}, grid: {grid}')
                if black_adj == 2:
                    # print(f'Black {tile}')
                    new_grid.add(tile)
                    # print(f'{tile} will be black')
        grid = new_grid
        # print()
        # print(f'--- Day {i + 1}: {len(grid)}')
        # print(f'--- Day {i + 1}: {grid}')

    return len(grid)


if __name__ == '__main__':
    with open('input1.txt') as f:
        lines = list(map(str.strip, f))
    print(f'Part 1: {do_it(lines)}')

# Part 1:
# too high: 987423651

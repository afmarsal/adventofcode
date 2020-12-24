import functools
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


def do_it(lines):
    grid = set()
    for line in lines:
        instructions = parse_instructions(line)
        curr = functools.reduce(lambda coord, op: DELTAS[op](coord), instructions, (0, 0))
        if curr in grid:
            grid.remove(curr)
        else:
            grid.add(curr)
    return len(grid)


if __name__ == '__main__':
    with open('input1.txt') as f:
        lines = list(map(str.strip, f))
    print(f'Part 1: {do_it(lines)}')

# Part 1: 263

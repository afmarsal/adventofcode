import numpy as np
import re

WIDTH = 1000
HEIGHT = WIDTH


def part1(instructions):
    grid = np.zeros(shape=(WIDTH, HEIGHT), dtype=np.bool)
    operations = {'turn on': lambda n: True,
                  'turn off': lambda n: False,
                  'toggle': lambda n: not n}
    for instruction in instructions:
        m = re.match(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', instruction)
        op = operations[m[1]]
        for i in range(int(m[3]), int(m[5]) + 1):
            for j in range(int(m[2]), int(m[4]) + 1):
                grid[i, j] = op(grid[i, j])
    return np.sum(grid)


# assert part1(['turn on 0,0 through 9,9']) == WIDTH * HEIGHT
# assert part1(['toggle 0,0 through 9,0']) == WIDTH
lines = open('input.txt').read().splitlines()
print(f'# Part 1: {part1(lines)}')

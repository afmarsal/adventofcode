import numpy as np
import re


def part1(instructions, size):
    grid = np.zeros(shape=(size, size), dtype=np.bool)
    operations = {'turn on': lambda n: True,
                  'turn off': lambda n: False,
                  'toggle': lambda n: not n}
    return do_lights(grid, instructions, operations)


def part2(instructions, size):
    grid = np.zeros(shape=(size, size), dtype=np.int)
    operations = {'turn on': lambda n: n + 1,
                  'turn off': lambda n: max(0, n - 1),
                  'toggle': lambda n: n + 2}
    return do_lights(grid, instructions, operations)


def do_lights(grid, instructions, operations):
    for instruction in instructions:
        m = re.match(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', instruction)
        op = operations[m[1]]
        for i in range(int(m[3]), int(m[5]) + 1):
            for j in range(int(m[2]), int(m[4]) + 1):
                grid[i, j] = op(grid[i, j])
    return np.sum(grid)


lines = open('input.txt').read().splitlines()

assert part1(['turn on 0,0 through 9,9'], 10) == 100
assert part1(['toggle 0,0 through 9,0'], 10) == 10
res1 = part1(lines, 1000)
print(f'# Part 1: {res1}')
assert res1 == 569999

assert part2(['turn on 0,0 through 0,0'], 1000) == 1
assert part2(['toggle 0,0 through 999,999'], 1000) == 2000000
res2 = part2(lines, 1000)
print(f'# Part 2: {res2}')
assert res2 == 17836115

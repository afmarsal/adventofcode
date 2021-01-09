from itertools import combinations
from math import prod

lines = open('input.txt').read().splitlines()
dimensions = [list(map(int, line.split('x'))) for line in lines]


def part1(dimensions):
    result = 0
    for dim in dimensions:
        dim_combo = [prod(lwh) for lwh in list(combinations(dim, 2))]
        result += 2 * sum(dim_combo) + min(dim_combo)

    return result


# lines = ['2x3x4']
# assert part1(lines) == 58

def part2(dimensions):
    return sum(prod(dim) + (sum(dim) - max(dim)) * 2 for dim in dimensions)


# lines = ['2x3x4']
# assert part2(lines) == 34

print(f'# Part 1: {part1(dimensions)}')
print(f'# Part 2: {part2(dimensions)}')

# Part 1: 1606483
# Part 2: 3842356


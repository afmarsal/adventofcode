from itertools import combinations
from math import prod

lines = open('input.txt').read().splitlines()


def part1(lines):
    result = 0
    for line in lines:
        dim = [int(s) for s in line.split('x')]
        dim_combo = [prod(l) for l in list(combinations(dim, 2))]
        result += 2 * sum(dim_combo) + min(dim_combo)

    return result

# lines = ['2x3x4']
# assert part1(lines) == 58

def part2(lines):
    result = 0
    for line in lines:
        dim = [int(s) for s in line.split('x')]
        bow = prod(dim)
        dim.remove(max(dim))
        peri = sum(dim) * 2
        result += bow + peri
    return result


# lines = ['2x3x4']
# assert part2(lines) == 34

print(f'Part 1: {part1(lines)}')
print(f'Part 2: {part2(lines)}')

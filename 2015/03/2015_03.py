from operator import add

route = open('input.txt').readline().strip()

DELTAS = {
    '^': (0, 1),
    '>': (1, 0),
    'v': (0, -1),
    '<': (-1, 0)
}


def houses(route):
    curr = (0, 0)
    result = {curr}
    for c in route:
        curr = tuple(map(add, curr, DELTAS[c]))
        result.add(curr)
    return result


def part1(route):
    return len(houses(route))


assert part1('>') == 2
assert part1('^>v<') == 4
assert part1('^v^v^v^v^v') == 2


def part2(route):
    santa, robo = route[::2], route[1::2]
    return len(houses(santa) | houses(robo))


assert part2('^v') == 3
assert part2('^>v<') == 3
assert part2('^v^v^v^v^v') == 11

print(f'# Part 1: {part1(route)}')
print(f'# Part 2: {part2(route)}')

# Part 1: 2572
# Part 2: 2631

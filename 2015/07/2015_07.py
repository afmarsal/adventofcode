import functools

MAX_SHORT = 0xffff

wires = dict()
values = dict()

OPS = {
    'NOT': lambda x, y: ~calc(y),
    'RSHIFT': lambda x, y: calc(x) >> calc(y),
    'LSHIFT': lambda x, y: calc(x) << calc(y),
    'AND': lambda x, y: calc(x) & calc(y),
    'OR': lambda x, y: calc(x) | calc(y),
    'SELF': lambda x, y: calc(x)
}


@functools.cache
def calc(op):
    if op.isdigit():
        return int(op)

    global wires

    spl = wires[op].split()
    if spl[0] == 'NOT':
        spl.insert(0, 'ignore')
    param1, op, param2 = spl if len(spl) > 1 else (spl[0], 'SELF', 0)
    return OPS[op](param1, param2)


def part1(lines, wire):
    global wires
    wires = dict(reversed(line.split(' -> ')) for line in lines)
    return calc(wire)


# sample1 = '''123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# '''

# DO NOT RUN WHEN USING @cache!!!!
# assert part1(sample1.splitlines(), 'd') == 72
# assert part1(sample1.splitlines(), 'e') == 507
# assert part1(sample1.splitlines(), 'f') == 492
# assert part1(sample1.splitlines(), 'g') == 114
# assert part1(sample1.splitlines(), 'h') == 65412
# assert part1(sample1.splitlines(), 'i') == 65079
# assert part1(sample1.splitlines(), 'x') == 123
# assert part1(sample1.splitlines(), 'y') == 456

lines = open('input.txt').read().splitlines()
print(f'# Part 1: {part1(lines, "a")}')
assert part1(lines, 'a') == 46065

# part 1: 46065

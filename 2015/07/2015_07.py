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
    if spl[0] == 'NOT': spl.insert(0, 'ignore')
    param1, op, param2 = spl if len(spl) > 1 else (spl[0], 'SELF', 0)
    return OPS[op](param1, param2)


def part1(lines, wire):
    global wires
    wires = dict(reversed(line.split(' -> ')) for line in lines)
    return calc(wire)


def part2(lines, wire, b_override):
    global wires
    wires = dict(reversed(line.split(' -> ')) for line in lines)
    wires['b'] = str(b_override)
    return calc(wire)


sample1 = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
'''

assert part1(sample1.splitlines(), 'd') == 72
assert part1(sample1.splitlines(), 'e') == 507
assert part1(sample1.splitlines(), 'f') == 492
assert part1(sample1.splitlines(), 'g') == 114
assert part1(sample1.splitlines(), 'h') == ~123
assert part1(sample1.splitlines(), 'i') == ~456
assert part1(sample1.splitlines(), 'x') == 123
assert part1(sample1.splitlines(), 'y') == 456

calc.cache_clear()
lines = open('input.txt').read().splitlines()
wire_a = part1(lines, 'a')
print(f'# Part 1: {wire_a}')
assert wire_a == 46065

calc.cache_clear()
new_wire_a = part2(lines, 'a', wire_a)
print(f'# Part 2: {new_wire_a}')

# part 1: 46065
# part 2: 14134

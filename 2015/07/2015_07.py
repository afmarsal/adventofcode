import functools

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


sample1 = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
'''


def sample(lines, wire):
    global wires
    wires = dict(reversed(line.split(' -> ')) for line in lines)
    return calc(wire)


assert sample(sample1.splitlines(), 'd') == 72
assert sample(sample1.splitlines(), 'e') == 507
assert sample(sample1.splitlines(), 'f') == 492
assert sample(sample1.splitlines(), 'g') == 114
assert sample(sample1.splitlines(), 'h') == ~123
assert sample(sample1.splitlines(), 'i') == ~456
assert sample(sample1.splitlines(), 'x') == 123
assert sample(sample1.splitlines(), 'y') == 456

lines = open('input.txt').read().splitlines()
wires = dict(reversed(line.split(' -> ')) for line in lines)

# Part 1
calc.cache_clear()
wire_a = calc('a')

print(f'# Part 1: {wire_a}')
assert wire_a == 46065

# Part 2
calc.cache_clear()
wires['b'] = str(wire_a)
new_wire_a = calc('a')

print(f'# Part 2: {new_wire_a}')
assert new_wire_a == 14134

# part 1: 46065
# part 2: 14134

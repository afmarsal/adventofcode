import operator
import re

MAX_SHORT = (2 ** 16 - 1)

OPS = {
    'RSHIFT': operator.rshift,
    'LSHIFT': operator.lshift,
    'AND': operator.and_,
    'OR': operator.or_,
}


values = dict()


def maybe_eval(wires, s):
    global values
    if s not in values:
        val = int(s) if s.isdigit() else calc(wires, s)
        values[s] = val
    return values[s]


def calc(wires, op):
    print(f'Processing {op} -> {wires[op]}')

    spl = wires[op].split()
    if len(spl) == 1:
        res = maybe_eval(wires, spl[0])
        assert 0 <= res <= MAX_SHORT
        # print(f'{op} -> {wires[op]} = {res}')
        return res
    elif len(spl) == 2:
        assert spl[0] == 'NOT'
        calc1 = maybe_eval(wires, spl[1])
        res = (~ calc1) & MAX_SHORT
        assert 0 <= res <= MAX_SHORT
        # print(f'{op} -> {wires[op]} = {res}')
        return res
    else:
        p1 = maybe_eval(wires, spl[0])
        p2 = maybe_eval(wires, spl[2])
        res = OPS[spl[1]](p1, p2)
        assert 0 <= res <= MAX_SHORT
        # print(f'{op} -> {wires[op]} -> {p1} {spl[1]} {p2} = {res}')
        return res


def part1(lines, wire):
    wires = dict(reversed(line.split(' -> ')) for line in lines)
    return calc(wires, wire)


# def part1(lines, wire):
#     def convert(s):
#         s = s.replace('AND', '&') \
#             .replace('OR', '|') \
#             .replace('LSHIFT', '<<') \
#             .replace('RSHIFT', '>>') \
#             .replace('->', '=') \
#             .strip()
#         s = re.sub(r'NOT (\w+)', r'(~ \1) & MAX_SHORT', s)
#         return re.sub(r'(.*) = (.*)', r'\2 = \1', s)
#
#     code = [convert(line) for line in lines]
#     print('\n'.join(code))
#     exec('\n'.join(code))
#     return eval(wire)


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
assert part1(sample1.splitlines(), 'h') == 65412
assert part1(sample1.splitlines(), 'i') == 65079
assert part1(sample1.splitlines(), 'x') == 123
assert part1(sample1.splitlines(), 'y') == 456

lines = open('input.txt').read().splitlines()
print(f'# Part 1: {part1(lines, "a")}')

# part 1
# 19210 TOO LOW
# 51978 TOO HIGH
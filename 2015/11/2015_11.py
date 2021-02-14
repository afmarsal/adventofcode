import re


def next_pass(p, suffix):
    for i in range(len(p)):
        idx = len(p) - i - 1
        nxt = ord(p[idx]) + 1
        if nxt <= ord('z'):
            return p[0:idx] + chr(nxt) + suffix
        else:
            return next_pass(p[0:idx], suffix + 'a')


def contains_streak(p):
    return any(ord(a) == ord(b) - 1 == ord(c) - 2 for a, b, c in zip(p, p[1:], p[2:]))


def part1(p):
    while True:
        p = next_pass(p, '')
        if 'i' in p or 'o' in p or 'l' in p:
            continue
        if not contains_streak(p):
            continue
        if len(re.findall(r'(\w)\1', p)) < 2:
            continue
        print(f'Pass found: {p}')
        return p


assert part1('abcdfezz') == 'abcdffaa'
assert part1('abcdefgh') == 'abcdffaa'
res1 = part1("vzbxkghb")
assert res1 == 'vzbxxyzz'
print(f'# Part 1: {res1}')
print(f'# Part 2: {part1(res1)}')
# Part 1: vzbxxyzz
# Part 2: vzcaabcc

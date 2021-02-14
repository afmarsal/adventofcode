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
    for i in range(len(p) - 2):
        if ord(p[i]) == ord(p[i + 1]) - 1 == ord(p[i + 2]) - 2:
            return True
    return False


def part1(p):
    while True:
        p = next_pass(p, '')
        if 'i' in p or 'o' in p or 'l' in p:
            continue
        if not contains_streak(p):
            continue
        if not re.match(r'.*(\w)\1.*(\w)\2.*', p):
            continue
        print(f'Pass found: {p}')
        return p


assert part1('abcdfezz') == 'abcdffaa'
assert part1('abcdefgh') == 'abcdffaa'
# assert part1('ghijklmn') == 'ghjaabcc'
res1 = part1("vzbxkghb")
print(f'# Part 1: {res1}')
print(f'# Part 2: {part1(res1)}')
# Part 1: vzbxxyzz
# Part 2: vzcaabcc

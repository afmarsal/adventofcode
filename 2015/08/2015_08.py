import re


def do_str(s1):
    trans = str.maketrans({'"': '\\"', '\\': '\\\\'})
    s2 = '"' + s1.translate(trans) + '"'
    return len(s2) - len(s1)


def part1(lines):
    return sum(len(line) - len(eval(line)) for line in lines)


def part2(lines):
    return sum(do_str(line) for line in lines)


sample_lines = r'''""
"abc"
"aaa\"aaa"
"\x27"
'''.splitlines()

lines = open('input.txt').read().splitlines()

assert part1(sample_lines) == 23 - 11
print(f'# Part 1: {part1(lines)}')

assert part2(sample_lines) == 42 - 23
print(f'# Part 2: {part2(lines)}')

# Part 1: 1333
# Part 2: 2046

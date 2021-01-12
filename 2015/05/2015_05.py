import re


def part1(s):
    if len(re.sub(r'[^aeiou]', '', string=s)) < 3:
        return False
    if not re.search(r'(\w)\1', string=s):
        return False
    if re.search(r'ab|cd|pq|xy', string=s):
        return False
    return True


def run(lines, f):
    return sum(f(s) for s in lines)


assert run(['ugknbfddgicrmopn'], part1) == 1
assert run(['aaa'], part1) == 1
assert run(['jchzalrnumimnmhp'], part1) == 0
assert run(['haegwjzuvuyypxyu'], part1) == 0
assert run(['dvszwmarrgswjxmb'], part1) == 0


def part2(s):
    if not re.search(r'(\w\w).*\1', s):
        return False
    if not re.search(r'(\w).\1', s):
        return False
    return True


assert run(['qjhvhtzxzqqjkmpb'], part2) == 1
assert run(['xxyxx'], part2) == 1
assert run(['uurcxstgmygtbstg'], part2) == 0
assert run(['ieodomkazucvgmuy'], part2) == 0

lines = open('input.txt').read().splitlines()
print(f'# Part 1: {run(lines, part1)}')
print(f'# Part 1: {run(lines, part2)}')

# Part 1: 258
# Part 1: 53


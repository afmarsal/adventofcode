from itertools import accumulate

s = open('input1.txt').readline().strip()


def part1(s):
    # str.countr returns the number of instances of the char passed as parameter
    return s.count('(') - s.count(')')


assert part1('(())') == 0
assert part1('()()') == 0


def part2(s):
    # itertools.accumulate generates a list that keeps track of the floor, so for an input like
    # '(()))' the "accumulated" list would be "[1, 2, 1, 0, -1]"
    # index returns the position of the first occurrence of the parameter (-1)
    return list(accumulate(s, lambda floor, c: floor + (1 if c == '(' else -1), initial=0)).index(-1)


assert part2(')') == 1
assert part2('()())') == 5
print(f'Part 1: {part1(s)}')
print(f'Part 1: {part2(s)}')

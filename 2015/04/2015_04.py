import itertools
import hashlib


def part1(input, start):
    for i in itertools.count():
        if hashlib.md5((input + str(i)).encode('utf-8')).hexdigest().startswith(start):
            return i


assert part1('abcdef', "00000") == 609043
assert part1('pqrstuv', "00000") == 1048970

print(f'# Part 1: {part1("iwrupvqb", "00000")}')
print(f'# Part 2: {part1("iwrupvqb", "000000")}')

# Part 1: 346386
# Part 1: 9958218

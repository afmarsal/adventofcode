def part1(nums):
    return next(n * (2000 - n) for n in nums if (2000 - n) in nums)


def part2(input_ints):
    return next(
        n1 * n2 * (2020 - n1 - n2) for n1 in input_ints for n2 in (input_ints - {n1}) if (2020 - n1 - n2) in input_ints)


if __name__ == '__main__':
    with open('input01.txt') as f:
        nums = set(map(int, f))
    print(f'Part 1: {part1(nums)}')
    print(f'Part 2: {part2(nums)}')

# Part 1: 556444
# Part 2: 193598720

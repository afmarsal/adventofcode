if __name__ == '__main__':
    with open('input01.txt') as f:
        nums = set(map(int, f))
        print(f'Part 1: {next(n * (2000 - n) for n in nums if (2000 - n) in nums)}')
        print(f'Part 2: {next(n1 * n2 * (2020 - n1 - n2) for n1 in nums for n2 in (nums - {n1}) if (2020 - n1 - n2) in nums)}')

# Part 1: 556444
# Part 2: 193598720

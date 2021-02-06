def generate_next_str(orig, dest):
    while len(orig) > 0:
        ch = orig[0]
        i = 0
        while i < len(orig) and orig[i] == ch:
            i += 1
        orig = orig[i:]
        dest = f'{dest}{i}{ch}'
    return dest


def part1(s, times):
    for i in range(times):
        s = generate_next_str(s, '')
        print(f'Next: {s}')
    return len(s)


assert part1('1', 5) == 6
print(f'# Part 1: {part1("1113122113", 40)}')

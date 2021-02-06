def generate_next_str(orig):
    changes = []
    last = 0
    for i in range(len(orig)):
        if i < len(orig) - 1:
            if orig[i] != orig[i + 1]:
                changes.append(str(i + 1 - last))
                changes.append(orig[last])
                last = i + 1
    changes.append(str(len(orig) - last))
    changes.append(orig[last])
    return ''.join(changes)


def part1(s, times):
    for i in range(times):
        s = generate_next_str(s)
        # print(f'Next: {s}')
    return len(s)


assert part1('1', 5) == 6
print(f'# Part 1: {part1("1113122113", 40)}')
print(f'# Part 2: {part1("1113122113", 50)}')

# Part 1: 360154
# Part 2: 5103798

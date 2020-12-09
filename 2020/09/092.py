WS = 5
# TOP = 22477624
# TOP_POS = 528
INPUT0 = '090.txt', 14, 127
INPUT1 = '091.txt', 528, 22477624


def do_it(filename):
    with open(filename) as f:
        lines = list(map(int, f))
    for i in range(WS + 1, len(lines)):
        s = set(lines[i - WS:i])
        for j in s:
            if (lines[i] - j) in s:
                break
        else:
            return i, lines[i]


def do_it(input):
    with open(input[0]) as f:
        lines = list(map(int, f))
    for i in range(0, input[1]):
        for j in range(i + 1, input[1]):
            s = sum(lines[i:j])
            if s == input[2]:
                return min(lines[i:j]) + max(lines[i:j])
            elif s > input[2]:
                break


if __name__ == '__main__':
    output = do_it(INPUT1)
    print(f'Result: {output}')

# Result: 2980044

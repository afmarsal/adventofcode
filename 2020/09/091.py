
WS = 25


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


if __name__ == '__main__':
    output = do_it('091.txt')
    print(f'Result: {output}')

# Result: 22477624

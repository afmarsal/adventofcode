def do_it(lines):
    deck1 = []
    for i in range(1, len(lines)):
        if len(lines[i]) == 0:
            break
        deck1.append(int(lines[i]))
    deck2 = []
    for i in range(i + 2, len(lines)):
        deck2.append(int(lines[i]))

    while len(deck1) > 0 and len(deck2) > 0:
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if c1 > c2:
            deck1.extend([c1, c2])
        else:
            deck2.extend([c2, c1])

    deck1.reverse()
    deck2.reverse()
    return sum((i + 1) * c for i, c in enumerate(deck1)) + sum((i + 1) * c for i, c in enumerate(deck2))


if __name__ == '__main__':
    with open('input1.txt') as f:
        lines = list(map(str.strip, f))

    output = do_it(lines)
    print(f'Part 1: {output}')

# Part 1: 32401

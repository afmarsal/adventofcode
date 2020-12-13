from itertools import count


def do_it(filename):
    with open(filename) as f:
        v0 = int(f.readline().strip())
        ids = f.readline().strip()

    freqs = {}
    for id in ids.split(','):
        if id == 'x':
            continue
        for i in count(0, int(id)):
            if i >= v0:
                freqs[int(id)] = i - v0
                break

    result = min(freqs, key=freqs.get)
    return result * freqs[result]


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 2176
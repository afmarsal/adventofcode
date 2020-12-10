from functools import reduce


def do_it(filename):
    with open(filename) as f:
        ints = sorted(list(map(int, f)))

    def inc(d, idx):
        d[idx] = d[idx] + 1
        return d

    d = reduce(lambda d, i: inc(d, ints[i] - ints[i - 1]), range(1, len(ints)), {1: 1, 3: 1})
    return d[1] * d[3]


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 1904

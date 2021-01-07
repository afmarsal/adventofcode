from collections import Counter


def do_it(filename):
    with open(filename) as f:
        ints = sorted(list(map(int, f)))
        ints = [0] + ints + [max(ints) + 3]
        c = Counter([ints[i + 1] - ints[i] for i in range(len(ints) - 1)])
        return c[1] * c[3]


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 1904

import util
from functools import reduce


def do_it(filename):
    return sum([len(reduce(lambda l1, l2: set(l1).intersection(l2), group)) for group in util.grouped_lines(filename)])


if __name__ == '__main__':
    output = do_it('input61.txt')
    print(f'Result: {output}')

# Result: 3323

import util


def do_it(filename):
    return sum([len(set(''.join(group))) for group in util.grouped_lines(filename)])


if __name__ == '__main__':
    output = do_it('input61.txt')
    print(f'Result: {output}')

# Result: 6530

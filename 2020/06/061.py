import util


def do_it(filename):
    result = 0
    group = set()
    for line in util.lines(filename, True):
        if len(line) > 0:
            group |= {c for c in line}
        else:
            result += len(group)
            group = set()
    return result


if __name__ == '__main__':
    output = do_it('input60.txt')
    print(f'Result: {output}')

# Result: 3323

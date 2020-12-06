import util


def do_it(filename):
    result = 0
    group = set()
    starting_group = True
    for line in util.lines(filename, True):
        if len(line) > 0:
            curr_group = {c for c in line}
            group = curr_group if starting_group else group & curr_group
            starting_group = False
            print(f'line {line}, group: {group}')
        else:
            result += len(group)
            group = set()
            starting_group = True
    return result


if __name__ == '__main__':
    output = do_it('input61.txt')
    print(f'Result: {output}')

# Result: 6530

import util


def do_it(filename):
    return max([calc_seat(line.strip()) for line in util.lines(filename)])


def calc_seat(line):
    return int(line.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), 2)


if __name__ == '__main__':
    output = do_it('input51.txt')
    print(f'Result: {output}')

# Result: 991

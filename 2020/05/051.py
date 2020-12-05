import util


def do_it(filename):
    return max([calc_seat(line.strip()) for line in util.lines(filename)])


def calc_seat(line):
    row = int(line[0:7].replace('F', '0').replace('B', '1'), 2)
    column = int(line[7:10].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + column


if __name__ == '__main__':
    output = do_it('input51.txt')
    print(f'Result: {output}')

# Result: 991

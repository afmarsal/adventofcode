import util


def do_it(filename):
    all_seats = set(range(991 + 1))  # 991 comes from solution 1
    for seat in [calc_seat(line.strip()) for line in util.lines(filename)]:
        all_seats.remove(seat)
    return max(all_seats)


def calc_seat(line):
    return int(line.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), 2)


if __name__ == '__main__':
    output = do_it('input51.txt')
    print(f'Result: {output}')

# Result: 534

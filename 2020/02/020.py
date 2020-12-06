import util


def do_it(filename):
    parsed_input = util.read_regex_from_file(filename, r'^(\d+)-(\d+) (\w+): (\w+)$')
    return sum((m[4][int(m[1]) - 1] == m[3]) != (m[4][int(m[2]) - 1] == m[3]) for m in parsed_input)


if __name__ == '__main__':
    output = do_it('input021.txt')
    print(f'Result: {output}')

# Result: 588

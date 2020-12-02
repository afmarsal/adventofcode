import util


def do_it_one(filename):
    parsed_input = util.read_regex_from_file(filename, r'^(\d+)-(\d+) (\w+): (\w+)$')
    result = 0
    for m in parsed_input:
        occurrences = m[4].count(m[3])
        if int(m[1]) <= occurrences <= int(m[2]):
            result = result + 1
    return result


def do_it(filename):
    parsed_input = util.read_regex_from_file(filename, r'^(\d+)-(\d+) (\w+): (\w+)$')
    return sum(int(m[1]) <= m[4].count(m[3]) <= int(m[2]) for m in parsed_input)


if __name__ == '__main__':
    output = do_it('input.txt')
    print(f'Result: {output}')

# Result: 636

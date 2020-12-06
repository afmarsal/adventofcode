import re
import util


def do_it(filename):
    parsed_input = (re.match(r'^(\d+)-(\d+) (\w+): (\w+)$', line) for line in util.lines(filename))
    return sum(int(m[1]) <= m[4].count(m[3]) <= int(m[2]) for m in parsed_input)


if __name__ == '__main__':
    output = do_it('input021.txt')
    print(f'Result: {output}')

# Result: 636

import re


def do_it(filename):
    regex = re.compile(r'^(\d+)-(\d+) (\w+): (\w+)$')
    with open(filename) as f:
        parsed_input = [regex.fullmatch(line.strip()) for line in f.readlines() if len(line.strip()) > 0]
    return sum(int(m[1]) <= m[4].count(m[3]) <= int(m[2]) for m in parsed_input)


if __name__ == '__main__':
    output = do_it('input021.txt')
    print(f'Result: {output}')

# Result: 636

import re


def parse_field(line):
    m = re.fullmatch(r'([^:]+): (\d+)-(\d+) or (\d+)-(\d+)', line)
    return [(m[1], (int(m[2]), int(m[3]), int(m[4]), int(m[5])))]


def parse_ticket(line):
    return [int(n) for n in line.split(',')]


def parse(filename):
    with open(filename) as f:
        lines = map(str.strip, f.readlines())
    # fields
    fields = {}
    line = next(lines)
    while len(line) > 0:
        fields.update(parse_field(line))
        line = next(lines)
    # your ticket
    next(lines)
    my_ticket = parse_ticket(next(lines))
    next(lines)  # Empty line
    # nearby tickets
    next(lines)
    line = next(lines)
    nearby = []
    try:
        while len(line) > 0:
            nearby.append(parse_ticket(line))
            line = next(lines)
    except StopIteration:
        pass
    return fields, my_ticket, nearby


def do_it(filename):
    fields, my_ticket, nearby = parse(filename)

    print(fields)
    print(my_ticket)
    print(nearby)

    rate = 0
    for ticket in nearby:
        for v in ticket:
            for ranges in fields.values():
                if ranges[0] <= v <= ranges[1] or ranges[2] <= v <= ranges[3]:
                    break
            else:
                rate += v
    return rate


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 26869

import re
from functools import reduce

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


def filter_invalid(fields, nearby):
    valid_nearby = nearby.copy()
    for ticket in nearby:
        for v in ticket:
            for ranges in fields.values():
                if ranges[0] <= v <= ranges[1] or ranges[2] <= v <= ranges[3]:
                    break
            else:
                valid_nearby.remove(ticket)
    return valid_nearby


def do_it(filename):
    fields, my_ticket, nearby = parse(filename)
    valid_nearby = filter_invalid(fields, nearby)

    positions = {pos: set(fields.keys()) for pos in range(0, len(my_ticket))}
    for ticket in valid_nearby:
        for pos, v in enumerate(ticket):
            for field, ranges in fields.items():
                if not (ranges[0] <= v <= ranges[1] or ranges[2] <= v <= ranges[3]):
                    positions[pos].discard(field)
    for pos, v in positions.items():
        print(f'{pos} -> {v}')

    unique_fields = set()
    final_positions = {}
    while len(unique_fields) < len(fields):
        curr_unique_field = set()
        # Find unique field
        for pos, fields in positions.items():
            if len(fields) == 1:
                curr_unique_field = fields.pop()
                final_positions[pos] = curr_unique_field
                break
        # Remove from the rest
        for fields in positions.values():
            fields.discard(curr_unique_field)
        # for pos, v in positions.items():
        #     print(f'{pos} -> {v}')

    for pos, v in final_positions.items():
        print(f'{pos} -> {v}')
    # print([pos for pos, field in final_positions.items() if field.startswith('departure')])

    result = 1
    for i, v in enumerate(my_ticket):
        if i in final_positions and final_positions[i].startswith('departure'):
            result *= v
    return result


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 855275529001

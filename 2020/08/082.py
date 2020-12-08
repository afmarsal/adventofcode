import util
from copy import deepcopy

NOT_FOUND = 99999999999


def parse_and_run(program):
    pc = 0
    accumulator = 0
    seen_pcs = set()
    while pc < len(program):
        if pc in seen_pcs:
            return NOT_FOUND

        seen_pcs.add(pc)
        op, arg = program[pc]
        if op == "acc":
            accumulator += int(arg)

        elif op == "jmp":
            pc += int(arg)
            continue

        pc += 1

    return accumulator


def replace_nop_jmp(program, pos):
    copy = deepcopy(program)
    for i in range(pos, len(copy)):
        if copy[i][0] in ("nop", "jmp"):
            copy[i][0] = "jmp" if copy[i][0] == "nop" else "nop"
            return copy, i + 1


def do_it(filename):
    program = [[l.split()[0], int(l.split()[1])] for l in util.lines(filename)]
    result = NOT_FOUND
    pos = 0
    while result == NOT_FOUND:
        curr, pos = replace_nop_jmp(program, pos)
        result = parse_and_run(curr)

    return result


if __name__ == '__main__':
    output = do_it('input81.txt')
    print(f'Result: {output}')

# Result: 1976

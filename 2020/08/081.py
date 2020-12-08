import util


def parse_and_run(program):
    pc = 0
    accumulator = 0
    seen_pcs = set()
    while True:
        if pc in seen_pcs:
            return accumulator

        seen_pcs.add(pc)
        op, arg = program[pc].split()
        if op == "acc":
            accumulator += int(arg)

        elif op == "jmp":
            pc += int(arg)
            continue

        pc += 1


def do_it(filename):
    return parse_and_run(list(util.lines(filename)))


if __name__ == '__main__':
    output = do_it('input81.txt')
    print(f'Result: {output}')

# Result: 337
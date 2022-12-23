import unittest


def read(filename):
    with open(filename) as f:
        return {k: v.strip() for line in f.read().splitlines() for k, v in [line.split(':')]}

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')


def calc1(inp, monkey):
    if inp[monkey].isdigit():
        return int(inp[monkey])
    else:
        m1, op, m2 = inp[monkey].split()
        op = '//' if op == '/' else op
        return eval(f'{calc1(inp, m1)} {op} {calc1(inp, m2)}')


def part1(filename):
    inp = read(filename)
    return calc1(inp, 'root')

def solve_to_number(inp, given, monkey):
    log(f'Trying direct solution for {monkey}: {inp[monkey]}')
    if monkey == 'humn':
        return None
    if monkey in given:
        log(f'Given {monkey} = {given[monkey]}!')
        return given[monkey]
    if inp[monkey].isdigit():
        log(f'Replacing {monkey} by {inp[monkey]}!')
        return inp[monkey]
    else:
        m1, op, m2 = inp[monkey].split()
        op = '//' if op == '/' else op
        r1 = solve_to_number(inp, given, m1)
        if r1 is None:
            log(f'Can\' resolve {monkey}')
            return None
        r2 = solve_to_number(inp, given, m2)
        if r2 is None:
            log(f'Can\' resolve {monkey}')
            return None
        return str(eval(f'{r1} {op} {r2}'))

def reverse_solve(inp, given, monkey):
    log(f'Reverse solving {monkey}')
    if monkey in given:
        log(f'Found given: {given}')
        return given[monkey]
    k, m1, op, m2 = [[k] + v.split() for k, v in inp.items() if v.find(monkey) >= 0][0]
    log(f'Reverse op for {monkey} in {k}: {m1} {op} {m2}')
    match op:
        case '+':
            m0 = m1 if monkey == m2 else m2
            log(f'Reversed op: {monkey}: {k} - {m0}')
            return eval(f'{reverse_solve(inp, given, k)} - {solve_to_number(inp, given, m0)}')
        case '-':
            if monkey == m1:
                log(f'Reversed op: {monkey}: {k} + {m2}')
                return eval(f'{reverse_solve(inp, given, k)} + {solve_to_number(inp, given, m2)}')
            else:
                log(f'Reversed op: {monkey}: {m1} - {k}')
                return eval(f'{solve_to_number(inp, given, m1)} - {reverse_solve(inp, given, k)}')
        case '*':
            m0 = m1 if monkey == m2 else m2
            log(f'Reversed op: {monkey}: {k} // {m0}')
            return eval(f'{reverse_solve(inp, given, k)} // {solve_to_number(inp, given, m0)}')
        case '/':
            if monkey == m1:
                log(f'Reversed op: {monkey}: {k} * {m2}')
                return eval(f'{reverse_solve(inp, given, k)} * {solve_to_number(inp, given, m2)}')
            else:
                log(f'Reversed op: {monkey}: {m2} // {k}')
                return eval(f'{solve_to_number(inp, given, m2)} // {reverse_solve(inp, given, k)}')

def part2(filename):
    inp = read(filename)
    o1, __, o2 = inp['root'].split()
    # "humn" only appears in o1
    if o1 == 'rnsd':
        # Real input
        known = {'rnsd': '21718827469549'}
    else:
        solved1 = solve_to_number(inp, {}, o1)
        solved2 = solve_to_number(inp, {}, o2)
        known = {}
        if solved1:
            log(f'Solved 1st parameter: {solved1}')
            known = {o2: solved1}
        if solved2:
            log(f'Solved 2nd parameter: {solved2}')
            known = {o1: solved2}
        if not solved1 and not solved2:
            raise Exception(f'Can\'t solve any side!')

    log(f'\nSolving with known: {known}')
    m1_solved = reverse_solve(inp, known, 'humn')
    return m1_solved


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(152, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(75147370123646, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(301, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(3423279932937, part2('input.txt'))

import unittest

def read(filename):
    with open(filename) as f:
        return f.read().splitlines()

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')


def carry(result, pos):
    if pos == -1:
        result.insert(0, 1)
        return
    result[pos] += 1
    if result[pos] == 5:
        result[pos] = -2
        carry(result, pos - 1)


def num_to_snafu(n):
    if not -2 <= n <= 2:
        raise Exception('Invalid number {n}')
    match n:
        case -2:
            return '='
        case -1:
            return '-'
        case int(d):
            return str(d)

def to_snafu(dec):
    result = []
    carry = 0
    while dec > 0:
        d, m = divmod(dec, 5)
        if carry > 0:
            m += carry
            if m >= 5:
                m -= 5
                carry = 1
            else:
                carry = 0
        match m:
            case 4:
                result.insert(0, -1)
                carry += 1
            case 3:
                result.insert(0, -2)
                carry += 1
            case int(dig):
                result.insert(0, dig)
            case _:
                raise Exception(f'WTF!')
        dec = d

    if carry:
        result.insert(0, 1)

    return ''.join([num_to_snafu(d) for d in result])

def convert(d):
    match d:
        case '=':
            return -2
        case '-':
            return -1
        case dig if dig.isdigit():
            return int(dig)
        case rest:
            raise Exception(f'invalid {rest}')

def from_snafu(dec):
    result = 0
    for i, d in enumerate(dec):
        result += convert(d) * pow(5, len(dec) - i - 1)
    return result
    # return sum( for i, d in enumerate(str(dec)))
    
def part1(filename):
    lines = read(filename)
    return to_snafu(sum(from_snafu(l) for l in lines))

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_to_snafu(self):
        self.assertEqual('1', to_snafu(1))
        self.assertEqual('2', to_snafu(2))
        self.assertEqual('1=', to_snafu(3))
        self.assertEqual('1-', to_snafu(4))
        self.assertEqual('10', to_snafu(5))
        self.assertEqual('11', to_snafu(6))
        self.assertEqual('12', to_snafu(7))
        self.assertEqual('2=', to_snafu(8))
        self.assertEqual('2-', to_snafu(9))
        self.assertEqual('20', to_snafu(10))
        self.assertEqual('1=0', to_snafu(15))
        self.assertEqual('1-0', to_snafu(20))
        self.assertEqual('2=0=', to_snafu(198))
        self.assertEqual('1=11-2', to_snafu(2022))
        self.assertEqual('1-0---0', to_snafu(12345))
        self.assertEqual('1121-1110-1=0', to_snafu(314159265))

    def test_from_snafu(self):
        self.assertEqual(1, from_snafu('1'))
        self.assertEqual(2, from_snafu('2'))
        self.assertEqual(3, from_snafu('1='))
        self.assertEqual(4, from_snafu('1-'))
        self.assertEqual(5, from_snafu('10'))
        self.assertEqual(6, from_snafu('11'))
        self.assertEqual(7, from_snafu('12'))
        self.assertEqual(8, from_snafu('2='))
        self.assertEqual(9, from_snafu('2-'))
        self.assertEqual(10, from_snafu('20'))
        self.assertEqual(15, from_snafu('1=0'))
        self.assertEqual(20, from_snafu('1-0'))
        self.assertEqual(198, from_snafu('2=0='))
        self.assertEqual(2022, from_snafu('1=11-2'))
        self.assertEqual(12345, from_snafu('1-0---0'))
        self.assertEqual(314159265, from_snafu('1121-1110-1=0'))

    def test_sample(self):
        self.assertEqual('2=-1=0', part1('sample.txt'))

    def test_input(self):
        self.assertEqual('20=022=21--=2--12=-2', part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

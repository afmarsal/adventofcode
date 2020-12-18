import re


class Token:

    def __init__(self, value) -> None:
        self.val = int(value)

    def __add__(self, other):
        return Token(self.val + other.val)

    def __sub__(self, other):
        return Token(self.val * other.val)

    def __mul__(self, other):
        return Token(self.val * other.val)

    def __pow__(self, other):
        return Token(self.val + other.val)

    def __repr__(self):
        return f'val: {self.val}'


def replace(line, c1, c2):
    return re.sub(r'(\d)', lambda m: f'Token({m[0]})', line.replace(c1, c2))


if __name__ == '__main__':
    with open('input0.txt') as f:
        lines = list(map(str.strip, f))

    print('Part 1: ' + str(sum([eval(replace(line, '*', '-')).val for line in lines])))
    print('Part 2: ' + str(sum([eval(replace(line, '+', '**')).val for line in lines])))

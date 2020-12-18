import re


class Token:

    def __init__(self, value) -> None:
        self.val = int(value)
        Token.__add__ = Token.__pow__
        Token.__mul__ = Token.__sub__

    def __sub__(self, other):
        return Token(self.val * other.val)

    def __pow__(self, other):
        return Token(self.val + other.val)


def to_token(line):
    return re.sub(r'(\d)', lambda m: f'Token({m[0]})', line)


if __name__ == '__main__':
    with open('input0.txt') as f:
        lines = list(map(lambda line: to_token(line), f))

    print('Part 1: ' + str(sum([eval(line.replace('*', '-')).val for line in lines])))
    print('Part 2: ' + str(sum([eval(line.replace('+', '**')).val for line in lines])))

import re
import util


def validate(passport):
    if 'cid' in passport:
        del passport['cid']
    if len(passport) != 7:
        return False
    if not 1920 <= int(passport['byr']) <= 2002:
        return False
    if not 2010 <= int(passport['iyr']) <= 2020:
        return False
    if not 2020 <= int(passport['eyr']) <= 2030:
        return False
    match = re.match(r'^(\d+)(cm|in)$', passport['hgt'])
    if not match:
        return False
    if match[2] == 'cm':
        if not 150 <= int(match[1]) <= 193:
            return False
    elif not 59 <= int(match[1]) <= 76:
        return False
    if not re.match(r'^#[0-9a-f]{6}$', passport['hcl']):
        return False
    if passport['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False
    if not re.match(r'^\d{9}$', passport['pid']):
        return False
    return True


def do_it(filename):
    def to_passport(group):
        tokens = (token for pair in ' '.join(group).split() for token in pair.split(':'))
        passport = dict(zip(tokens, tokens))
        if 'cid' in passport:
            del passport['cid']
        return passport

    return sum([validate(to_passport(group)) for group in util.grouped_lines(filename)])


if __name__ == '__main__':
    output = do_it('input041.txt')
    print(f'Result: {output}')

# Result: 116

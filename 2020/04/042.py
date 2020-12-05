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
    result = 0
    passport = dict()
    for line in util.lines(filename, True):
        if len(line) > 0:
            tokens = iter([token for pair in line.split() for token in pair.split(':')])
            line_batch = dict(zip(tokens, tokens))
            passport.update(line_batch)
        else:
            # print(passport)
            result += validate(passport)
            passport = dict()

    return result


if __name__ == '__main__':
    output = do_it('input041.txt')
    print(f'Result: {output}')

# Result: 116

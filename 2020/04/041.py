import util


def do_it(filename):
    def to_passport(group):
        tokens = (token for pair in ' '.join(group).split() for token in pair.split(':'))
        passport = dict(zip(tokens, tokens))
        if 'cid' in passport:
            del passport['cid']
        return passport

    return sum([len(to_passport(group)) == 7 for group in util.grouped_lines(filename)])


if __name__ == '__main__':
    output = do_it('input041.txt')
    print(f'Result: {output}')

# Result: 200

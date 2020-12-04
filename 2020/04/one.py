def do_it(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    result = 0
    passport = dict()
    for line in lines:
        if len(line) > 0:
            tokens = iter([token for pair in line.split() for token in pair.split(':')])
            line_batch = dict(zip(tokens, tokens))
            passport.update(line_batch)
        else:
            print(passport)
            if 'cid' in passport:
                del passport['cid']
            if len(passport) == 7:
                result += 1
            passport = dict()

    return result


if __name__ == '__main__':
    output = do_it('input.txt')
    print(f'Result: {output}')

# Result: 200

def do_it(filename):
    result = 0
    passport = dict()
    with open(filename) as f:
        for line in [line.strip() for line in f.readlines()]:
            if len(line) > 0:
                tokens = iter([token for pair in line.split() for token in pair.split(':')])
                line_batch = dict(zip(tokens, tokens))
                passport.update(line_batch)
            else:
                # print(passport)
                if 'cid' in passport:
                    del passport['cid']
                result += len(passport) == 7
                passport = dict()

    return result


if __name__ == '__main__':
    output = do_it('input.txt')
    print(f'Result: {output}')

# Result: 200

import time


def split_rule(rule):
    if rule[1] == '|':
        return [rule[0]], [rule[2]]
    elif rule[2] == '|':
        return rule[0:2], rule[3:]
    else:
        raise Exception("Where's the |!!!")


def subst(rules, pending, matches):
    # print(f'Before: {pending}, {matches}')
    if len(pending) == 0:
        return matches
    new_pending = []
    for repl in pending:
        output = [[]]
        for token in repl:
            new_output = []
            if token in rules:
                if '|' in rules[token]:
                    rule1, rule2 = split_rule(rules[token])
                    for s in output:
                        new_output.append(s + rule1)
                        new_output.append(s + rule2)
                else:
                    for s in output:
                        new_output.append(s + rules[token])
            else:
                for s in output:
                    new_output.append(s + [token])
            output = new_output

        start_time = time.time()
        for l in output:
            if all([m.replace('a', 'b') == 'b' * len(m) for m in l]):
                matches.append(''.join(l))
            else:
                new_pending.append(l)
        if (time.time() - start_time) > 1:
            print("Check output final %s seconds ---" % (time.time() - start_time))
    print(f'Pending: {len(pending)}, matches: {len(matches)}')
    # print(f'new matches: {len(new_matches)} {new_matches}')
    return subst(rules, new_pending, matches)


def do_it(lines):
    rules = dict()
    for i, line in enumerate(lines):
        if len(line) == 0:
            break
        rules[line.split(":")[0]] = list(line.split(":")[1].strip().replace('"', '').split())
    strings = [lines[i] for i in range(i + 1, len(lines))]

    pending = [rules["0"]]
    matches = []
    matches = subst(rules, pending, matches)
    return sum([s in matches for s in strings])


if __name__ == '__main__':
    with open('input1.txt') as f:
        filelines = list(map(str.strip, f))

    output = do_it(filelines)
    print(f'Part 1: {output}')

# Part 1: 165

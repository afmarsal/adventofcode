import re

RULE_42 = ['(', '42', ')']
RULE_31 = ['(', '31', ')']


def subst(rules, regex):
    if all([c in 'ab()|+' for c in regex]):
        return ''.join(regex)
    new_regex = []
    for t in regex:
        if t not in rules:
            new_regex.append(t)
        else:
            if '|' in rules[t]:
                l = list(rules[t].split())
                l.insert(0, '(')
                l.append(')')
                new_regex.extend(l)
            else:
                if t == '8':
                    new_regex.extend(RULE_42 + ['+'])
                elif t == '11':
                    new_regex.append('(')
                    for i in range(1, 40):
                        new_regex.extend(RULE_42 * i + RULE_31 * i)
                        new_regex.append('|')
                    new_regex.pop()
                    new_regex.append(')')
                else:
                    new_regex.extend(rules[t].split())
    return subst(rules, new_regex)


def do_it(lines):
    rules = dict()
    for i, line in enumerate(lines):
        if len(line) == 0:
            break
        rules[line.split(":")[0]] = line.split(":")[1].replace('"', '').strip()
    strings = [lines[i] for i in range(i + 1, len(lines))]

    regex = rules['0'].split()
    regex = subst(rules, regex)
    # print(regex)
    compiled = re.compile(regex)
    return sum([compiled.fullmatch(s) is not None for s in strings])


if __name__ == '__main__':
    with open('input1.txt') as f:
        filelines = list(map(str.strip, f))

    output = do_it(filelines)
    print(f'Part 1: {output}')

# Part 2: 274

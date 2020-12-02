import re


def read_ints_from_file(filename):
    with open(filename) as f:
        result = []
        content = f.readlines()
        for line in content:
            if len(line) == 0:
                continue
            i = int(line.strip())
            result.append(i)
        return result


def read_regex_from_file(filename, regex):
    prog = re.compile(regex)
    with open(filename) as f:
        result = []
        content = f.readlines()
        for line in content:
            if len(line) == 0:
                continue
            matched = prog.fullmatch(line.strip())
            if not matched:
                print(f'Line {line} does not match!')
                raise Exception
            result.append(matched)
        return result

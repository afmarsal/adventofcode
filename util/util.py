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
    regex = re.compile(regex)
    with open(filename) as f:
        return [regex.fullmatch(line.strip()) for line in f.readlines() if len(line.strip()) > 0]

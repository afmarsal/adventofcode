import re
import itertools


def read_ints_from_file(filename):
    return (int(line) for line in lines(filename))


def read_regex_from_file(filename, regex):
    regex = re.compile(regex)
    return (regex.fullmatch(line.strip()) for line in lines(filename))


def lines(filename):
    with open(filename) as f:
        return (line.strip() for line in f.readlines() if len(line.strip()) > 0)


def grouped_lines(filename):
    with open(filename) as f:
        return (list(v) for k, v in itertools.groupby([l.strip() for l in f], lambda l: l == '') if not k)


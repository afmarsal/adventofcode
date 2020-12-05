import re


def read_ints_from_file(filename):
    return [int(line) for line in lines(filename)]


def read_regex_from_file(filename, regex):
    regex = re.compile(regex)
    return [regex.fullmatch(line.strip()) for line in lines(filename)]


def lines(filename, include_empty = False):
    with open(filename) as f:
        return [line.strip() for line in f.readlines() if include_empty or len(line.strip()) > 0]

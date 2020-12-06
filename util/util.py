import re
import itertools


def read_ints_from_file(filename):
    return [int(line) for line in lines(filename)]


def read_regex_from_file(filename, regex):
    regex = re.compile(regex)
    return [regex.fullmatch(line.strip()) for line in lines(filename)]


def lines(filename, include_empty=False):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines() if include_empty or len(line.strip()) > 0]
        if include_empty:
            lines.append('')
    return lines

def grouped_lines(filename):
    with open(filename) as f:
        all_lines = [line.strip() for line in f.readlines()]
        return (list(v) for k, v in itertools.groupby(all_lines, lambda l: l == '') if not k)


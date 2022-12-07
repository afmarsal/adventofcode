import unittest
import re


def read(filename):
    with open(filename) as f:
        return f.read().splitlines()

CD_OUT = re.compile(r"\$ cd \.\.")
CD_IN = re.compile(r"\$ cd (\w+)")
A_DIR = re.compile(r"dir (\w+)")
A_FILE = re.compile(r"(\d+) (\w+)")

NAME = 0
SIZE = 1
PARENT = 2
CHILDREN = 3


def log(param):
    # print(param)
    pass

def parse_fs(lines):
    fs = dict()
    # dir name, size, parent, children
    curr_dir = ["/", 0, None, []]
    fs["/"] = curr_dir
    pwd = [curr_dir]
    for line in lines[1:]:  # skip first line, which is always "cd /"
        # Don't care about ls and dirs

        a_file = A_FILE.match(line)
        if a_file:
            size = int(a_file.group(1))
            for dir in pwd:
                dir[SIZE] += size
                log("Added size {}. New size: [{}]={}".format(size, dir[NAME], dir[SIZE]))
            continue

        cd_in = CD_IN.match(line)
        if cd_in:
            dir_name = curr_dir[NAME] + cd_in.group(1) + "/"
            curr_dir = [dir_name, 0, curr_dir[NAME], []]
            pwd.append(curr_dir)
            fs[dir_name] = curr_dir
            log("Entering dir {}".format(curr_dir[NAME]))
            continue

        if CD_OUT.match(line):
            pwd.pop()
            curr_dir = pwd[len(pwd)-1]
            log("Leaving dir. Curr dir {}".format(curr_dir[NAME]))

    return fs

def part1(filename):
    fs = parse_fs(read(filename))
    return sum([dir[SIZE] for dir in fs.values() if dir[SIZE] <= 100000])

def part2(filename):
    fs = parse_fs(read(filename))
    free = 70000000 - fs["/"][SIZE]
    return min([dir[SIZE] for dir in fs.values() if dir[SIZE] >= (30000000 - free)])


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(95437, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(1908462, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(24933642, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(3979145, part2('input.txt'))

import unittest
import re


def read(filename):
    with open(filename) as f:
        return f.read().splitlines()

def log(param):
    # print(param)
    pass

NAME = 0
SIZE = 1

def parse_fs(lines):
    fs = dict()
    # dir name, size
    curr_dir = ["/", 0]
    fs["/"] = curr_dir
    pwd = [curr_dir]
    for line in lines[1:]:  # skip first line, which is always "cd /"
        match line.split():
            case ['$', 'ls'] | ['dir', _]:
                continue

            case ['$', 'cd', '..']:
                pwd.pop()
                curr_dir = pwd[len(pwd) - 1]
                log("Leaving dir. Curr dir {}".format(curr_dir[NAME]))

            case ['$', 'cd', dir_name]:
                dir_name = curr_dir[NAME] + dir_name + "/"
                curr_dir = [dir_name, 0, curr_dir[NAME], []]
                pwd.append(curr_dir)
                fs[dir_name] = curr_dir
                log("Entering dir {}".format(curr_dir[NAME]))

            case [size, _]:
                for dir in pwd:
                    dir[SIZE] += int(size)
                    log("Added size {}. New size: [{}]={}".format(size, dir[NAME], dir[SIZE]))

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

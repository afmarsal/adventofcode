import copy
import dataclasses
import unittest

def read(filename):
    with open(filename) as f:
        return list(map(int, f.read().splitlines()))

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')

preexisting = [
    [2, 1, -3, 3, -2, 0, 4],
    [1, -3, 2, 3, -2, 0, 4],
    [1, 2, 3, -2, -3, 0, 4],
    [1, 2, -2, -3, 0, 3, 4],
    [1, 2, -3, 0, 3, 4, -2],
    [1, 2, -3, 0, 3, 4, -2],
    [1, 2, -3, 4, 0, 3, -2]
]

class Node:
    def __init__(self, pos, num) -> None:
        self.pos = pos
        self.num = num
        # self.prev = None
        # self.nxt = None

    def __repr__(self) -> str:
        return f'[{self.pos}]:{self.num}'


def build_linked_list(original_numbers):
    result = [Node(i, n) for i, n in enumerate(original_numbers)]
    for i in range(len(result)):
        result[i].nxt = result[(i+1)%len(result)]
        result[i].prev = result[(i-1)%len(result)]
    log(result)
    return result[0]


def find_current_pos(numbers, i):
    for curr_pos, n in enumerate(numbers):
        if n.pos == i:
            return curr_pos, n.num

def find_by_num(numbers, num):
    for pos, n in enumerate(numbers):
        if n.num == num:
            return pos, n

def build_list(numbers):
    return [Node(i, n) for i, n in enumerate(numbers)]


def part1(filename):
    original_numbers = read(filename)
    numbers = build_list(original_numbers)
    for i, n in enumerate(original_numbers):
        pos, n = find_current_pos(numbers, i)
        new_pos = (pos + n) % (len(numbers) - 1)
        if pos == new_pos:
            continue
        if pos < new_pos:
            next_numbers = numbers[0:pos] + numbers[pos + 1:new_pos + 1] + [numbers[pos]] + numbers[new_pos + 1:]
        else:
            next_numbers = numbers[0:new_pos] + [numbers[pos]] + numbers[new_pos:pos] + numbers[pos + 1:]
        # log(f'[{n}]: {numbers} -> {next_numbers}')
        numbers = next_numbers
        # if 0 <= i < len(preexisting):
        #     if numbers != preexisting[i]:
        #         log(f'{i} Sequences dont match {numbers} != {preexisting[i]}')
    zero_pos, __ = find_by_num(numbers, 0)
    # result = 0
    # for p in 1000, 2000, 3000:
    #     result += numbers[(zero_pos + p) % len(numbers)]
    mil_pos = numbers[(zero_pos + 1000) % len(numbers)].num
    dmil_pos = numbers[(zero_pos + 2000) % len(numbers)].num
    tmil_pos = numbers[(zero_pos + 3000) % len(numbers)].num
    log(f'{zero_pos} -> {mil_pos}, {dmil_pos}, {tmil_pos}')
    result = mil_pos + dmil_pos + tmil_pos
    return result


def part2(filename):
    numbers = read(filename)
    numbers = [n * 811589153 for n in numbers]
    lst = build_linked_list(numbers)
    for i in range(10):
        mix(numbers, lst)

    node = find_by_num(0, lst)
    result = 0
    for i in range(1, 3001):
        node = node.nxt
        if i % 1000 == 0:
            result += node.num
    return result


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(3, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(5498, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1623178306, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

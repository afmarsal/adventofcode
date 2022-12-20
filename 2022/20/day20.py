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
        self.prev = None
        self.nxt = None

    def __repr__(self) -> str:
        return f'[{self.pos}]:{self.num}'


def build_linked_list(original_numbers):
    result = [Node(i, n) for i, n in enumerate(original_numbers)]
    for i in range(len(result)):
        result[i].nxt = result[(i+1)%len(result)]
        result[i].prev = result[(i-1)%len(result)]
    log(result)
    return result[0]


def find_by_pos(i, lst):
    node = lst
    while True:
        if node.pos == i:
            return node
        node = node.nxt

def find_by_num(i, lst):
    node = lst
    while True:
        if node.num == i:
            return node
        node = node.nxt


def part1(filename):
    original_numbers = read(filename)
    lst = build_linked_list(original_numbers)
    node = lst
    for i, n in enumerate(original_numbers):
        node = find_by_pos(i, node)
        move = node.num % (len(original_numbers) - 1)
        for j in range(move):
            old_next = node.nxt
            old_prev = node.prev
            node.nxt = old_next.nxt
            node.prev = old_next

            old_next.prev = old_prev
            old_next.nxt = node

            old_prev.nxt = old_next

        # c = lst
        # log_nolf(f'{i}-{n} -> ')
        # for k in range(len(original_numbers)):
        #     log_nolf(c)
        #     log_nolf(',')
        #     c = c.nxt
        # log()

    node = find_by_num(0, lst)
    result = 0
    for i in range(1, 3001):
        node = node.nxt
        if i % 1000 == 0:
            result += node.num
    # mil_pos = numbers[(zero_pos + 1000) % len(numbers)]
    # dmil_pos = numbers[(zero_pos + 2000) % len(numbers)]
    # tmil_pos = numbers[(zero_pos + 3000) % len(numbers)]
    # log(f'{zero_pos} -> {mil_pos}, {dmil_pos}, {tmil_pos}')
    # result = mil_pos + dmil_pos + tmil_pos
    return result

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(3, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(5498, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

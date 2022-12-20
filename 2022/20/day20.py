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

class Node:
    def __init__(self, pos, num) -> None:
        self.pos = pos
        self.num = num

    def __repr__(self) -> str:
        return f'[{self.pos}]:{self.num}'

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

def mix(original_numbers, numbers):
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
    return numbers

def part1(filename):
    original_numbers = read(filename)
    numbers = build_list(original_numbers)
    numbers = mix(original_numbers, numbers)
    zero_pos, __ = find_by_num(numbers, 0)
    result = 0
    for i in range(1, 3001):
        if i % 1000 == 0:
            result += numbers[(zero_pos + i) % len(numbers)].num
    return result


def part2(filename):
    original_numbers = read(filename)
    original_numbers = [n * 811589153 for n in original_numbers]
    numbers = build_list(original_numbers)
    for i in range(10):
        numbers = mix(original_numbers, numbers)
    zero_pos, __ = find_by_num(numbers, 0)
    result = 0
    for i in range(1, 3001):
        if i % 1000 == 0:
            result += numbers[(zero_pos + i) % len(numbers)].num
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

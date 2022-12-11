import unittest
import re

def read(filename):
    monkeys = []
    with open(filename) as f:
        for chunk in f.read().split('\n\n'):
            lines = chunk.splitlines()
            attrs = {'items': re.findall(r'\d+', lines[1]),
                     'op': lines[2].replace('Operation: new = ', '').split(),
                     'div': int(re.findall(r'\d+', lines[3])[0]),
                     'true': int(re.findall(r'\d+', lines[4])[0]),
                     'false': int(re.findall(r'\d+', lines[5])[0]),
                     'inspected': 0}
            monkeys.append(attrs)
    return monkeys

def part1(filename):
    monkeys = read(filename)
    for round in range(20):
        for monkey in monkeys:
            for item in monkey['items']:
                monkey['inspected'] += 1
                op1 = int(item) if monkey['op'][0] == 'old' else int(monkey['op'][0])
                op2 = int(item) if monkey['op'][2] == 'old' else int(monkey['op'][2])
                new_level = op1 * op2 if monkey['op'][1] == '*' else op1 + op2
                new_level = new_level // 3
                if new_level % monkey['div'] == 0:
                    monkeys[monkey['true']]['items'].append(new_level)
                else:
                    monkeys[monkey['false']]['items'].append(new_level)
            monkey['items'] = []
    inspections = [monkey['inspected'] for monkey in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]

def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(10605, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(78960, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-1, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

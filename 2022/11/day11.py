import unittest
import re
import numpy

def read(filename):
    monkeys = []
    with open(filename) as f:
        for chunk in f.read().split('\n\n'):
            lines = chunk.splitlines()
            attrs = {'items': re.findall(r'\d+', lines[1]),
                     'op': lines[2].replace('Operation: new = ', ''),
                     'div': int(re.findall(r'\d+', lines[3])[0]),
                     'true': int(re.findall(r'\d+', lines[4])[0]),
                     'false': int(re.findall(r'\d+', lines[5])[0]),
                     'inspected': 0}
            monkeys.append(attrs)
    return monkeys

def calc(filename, rounds):
    monkeys = read(filename)
    mcm = numpy.prod([monkey['div'] for monkey in monkeys])
    for round in range(rounds):
        for monkey in monkeys:
            for item in monkey['items']:
                monkey['inspected'] += 1
                new_level = eval(monkey['op'].replace('old', str(item)))
                new_level = new_level // 3 if rounds == 20 else new_level % mcm
                if new_level % monkey['div'] == 0:
                    monkeys[monkey['true']]['items'].append(new_level)
                else:
                    monkeys[monkey['false']]['items'].append(new_level)
            monkey['items'] = []
    inspections = [monkey['inspected'] for monkey in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]

def part1(filename):
    return calc(filename, 20)

def part2(filename):
    return calc(filename, 10000)

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(10605, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(78960, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(2713310158, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(14561971968, part2('input.txt'))

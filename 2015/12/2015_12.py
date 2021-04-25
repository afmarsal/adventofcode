import json
import unittest


def recurse(obj):
    if type(obj) == dict:
        obj = list(obj.values())
    if type(obj) == list:
        return sum([recurse(e) for e in obj])
    if type(obj) == int:
        return obj
    return 0


def decode(string, object_hook):
    obj = json.loads(string, object_hook=object_hook)
    res = recurse(obj)
    # print(f'{string} -> {obj}')
    return res


def part1(string):
    return decode(string, None)


def part2(string):
    def discard_reds(obj):
        return {} if 'red' in obj.values() else obj

    return decode(string, discard_reds)


file_input = open('input.txt').read()


class TestPart1(unittest.TestCase):
    def test1(self):
        self.assertEqual(part1('[1,2,3]'), 6)

    def test2(self):
        self.assertEqual(part1('{"a":2,"b":4}'), 6)

    def test3(self):
        self.assertEqual(part1('[[[3]]]'), 3)

    def test4(self):
        self.assertEqual(part1('{"a":{"b":4},"c":-1}'), 3)

    def test_solution_part1(self):
        res = part1(file_input)
        self.assertEqual(res, 119433)
        print(f'# Part 1: {res}')


class TestPart2(unittest.TestCase):

    def test1(self):
        self.assertEqual(part2('[1,2,3]'), 6)

    def test2(self):
        self.assertEqual(part2('[1,{"c":"red","b":2},3]'), 4)

    def test3(self):
        self.assertEqual(part2('{"d":"red","e":[1,2,3,4],"f":5}'), 0)

    def test4(self):
        self.assertEqual(part2('[1,"red",5]'), 6)

    def test_solution_part2(self):
        res = part2(file_input)
        self.assertEqual(res, 68466)
        print(f'# Part 2: {res}')


if __name__ == '__main__':
    unittest.main()

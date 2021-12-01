import unittest


def get_nums(filename):
    with open(filename) as f:
        return [int(l) for l in f.read().splitlines()]


def part1(nums):
    return sum([1 if y > x else 0 for x, y in zip(nums, nums[1:])])


def part2(nums):
    return sum([1 if v1+v2+v3 > v0+v1+v2 else 0 for v0, v1, v2, v3 in zip(nums, nums[1:], nums[2:], nums[3:])])


class TestPart1(unittest.TestCase):
    def test10(self):
        nums = get_nums('input0.txt')
        self.assertEqual(part1(nums), 7)

    def test1(self):
        nums = get_nums('input.txt')
        self.assertEqual(part1(nums), 1139)


class TestPart2(unittest.TestCase):
    def test20(self):
        nums = get_nums('input0.txt')
        self.assertEqual(part2(nums), 5)

    def test21(self):
        nums = get_nums('input.txt')
        self.assertEqual(part2(nums), 1103)

import unittest


def get_nums(filename):
    with open(filename) as f:
        return [int(l) for l in f.read().splitlines()]


def part1(nums):
    ini = nums[0]
    c = 0
    for l in nums[1:]:
        if l > ini:
            c += 1
        ini = l

    return c


def part2(nums):
    ini = sum(nums[0:3])
    c = 0
    for j, __ in enumerate(nums[1:-2]):
        i = j + 1
        curr = sum(nums[i:i + 3])
        # print(f'ini: {ini}, c = {c}, i = {i}, curr = {curr}')
        if curr > ini:
            c += 1
        ini = curr
    return c


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

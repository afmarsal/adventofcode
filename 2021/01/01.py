import unittest


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
        with open('input0.txt') as f:
            nums = [int(l) for l in f.read().splitlines()]
        self.assertEqual(part1(nums), 7)

    def test1(self):
        with open('input.txt') as f:
            nums = [int(l) for l in f.read().splitlines()]
        self.assertEqual(part1(nums), 1139)


class TestPart2(unittest.TestCase):
    def test20(self):
        with open('input0.txt') as f:
            nums = [int(l) for l in f.read().splitlines()]
        self.assertEqual(part2(nums), 5)

    def test21(self):
        with open('input.txt') as f:
            nums = [int(l) for l in f.read().splitlines()]
        self.assertEqual(part2(nums), 1103)


def get_nums():
    return

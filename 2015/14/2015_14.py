import unittest
import re
from collections import namedtuple

regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.'

ReindeerInfo = namedtuple('ReindeerInfo', ['speed', 'run_duration', 'rest_duration'])


def parse_input(lines):
    reindeers = dict()
    for line in lines:
        m = re.fullmatch(regex, line)
        if not m:
            raise RuntimeError(f'line "{line}" does not match')
        reindeers[m[1]] = [int(m[2])] * int(m[3]) + [0] * int(m[4])
    return reindeers


def solve(lines, elapsed_sec):
    reindeer_steps = parse_input(lines)
    reindeers_distances = {reindeer: 0 for reindeer in reindeer_steps.keys()}
    reindeers_points = reindeers_distances.copy()
    for sec in range(elapsed_sec):
        top_distance = 0
        for reindeer, steps in reindeer_steps.items():
            reindeers_distances[reindeer] += steps[sec % len(steps)]
            top_distance = max(top_distance, reindeers_distances[reindeer])
        top_reindeers = [reindeer for reindeer, distance in reindeers_distances.items() if distance == top_distance]
        for reindeer in top_reindeers:
            reindeers_points[reindeer] += 1

    return max(reindeers_distances.values()), max(reindeers_points.values())


def part1(lines, elapsed_sec):
    res = solve(lines, elapsed_sec)
    return res[0]


def part2(lines, elapsed_sec):
    res = solve(lines, elapsed_sec)
    return res[1]


class TestPart1(unittest.TestCase):
    def test10(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part1(lines, 1), 16)
            self.assertEqual(part1(lines, 10), 160)
            self.assertEqual(part1(lines, 11), 176)
            self.assertEqual(part1(lines, 1000), 1120)

    def test1(self):
        with open('input_part1.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part1(lines, 2503), 2696)


class TestPart2(unittest.TestCase):
    def test20(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part2(lines, 1), 1)
            self.assertEqual(part2(lines, 10), 10)
            self.assertEqual(part2(lines, 11), 11)
            self.assertEqual(part2(lines, 1000), 689)

    def test2(self):
        with open('input_part1.txt') as f:
            lines = f.read().splitlines()
            # 3724 too high
            self.assertEqual(part2(lines, 2503), 1084)


if __name__ == '__main__':
    unittest.main()

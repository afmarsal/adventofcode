import unittest
import re
import itertools as it
from collections import namedtuple

regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.'

ReindeerInfo = namedtuple('ReindeerInfo', ['speed', 'run_duration', 'rest_duration'])

def model_input(lines):
    reindeers = dict()
    for line in lines:
        m = re.fullmatch(regex, line)
        if not m:
            raise RuntimeError(f'line "{line}" does not match')
        reindeers[m[1]] = ReindeerInfo(speed=int(m[2]), run_duration=int(m[3]), rest_duration=int(m[4]))
    return reindeers


def solve(lines, elapsed_sec):
    reindeers = model_input(lines)
    result = dict()
    for reindeer, info in reindeers.items():
        cycle_duration = info.run_duration + info.rest_duration
        # how many "cycles" a reindeer completes
        complete_cycles = elapsed_sec // cycle_duration
        complete_cycles_distance = complete_cycles * (info.run_duration * info.speed)

        partial_cycles_duration = elapsed_sec % cycle_duration
        partial_cycles_distance = info.speed * min(info.run_duration, partial_cycles_duration)

        result[reindeer] = complete_cycles_distance + partial_cycles_distance
    print(f'Results after {elapsed_sec} seconds: {result}')
    return max(result.values())


def part1(lines, elapsed_sec):
    return solve(lines, elapsed_sec)


def part2(lines):
    return solve(lines, True)


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
    def test10(self):
        with open('input_part2.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(part2(lines), 640)


if __name__ == '__main__':
    unittest.main()

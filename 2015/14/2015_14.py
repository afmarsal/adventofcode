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


def solve1(lines, elapsed_sec):
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


def is_running(sec, info):
    cycle_duration = info.run_duration + info.rest_duration
    sec_in_cycle = sec % cycle_duration
    return 0 < sec_in_cycle <= info.run_duration


def part1(lines, elapsed_sec):
    reindeers = model_input(lines)
    reindeers_distances = {reindeer: 0 for reindeer in reindeers.keys()}
    reindeers_points = {reindeer: 0 for reindeer in reindeers.keys()}
    for sec in range(1, elapsed_sec + 1):
        top_distance = 0
        for reindeer, info in reindeers.items():
            if is_running(sec, info):
                reindeers_distances[reindeer] += info.speed
            top_distance = max(top_distance, reindeers_distances[reindeer])
        top_reindeers = [reindeer for reindeer, distance in reindeers_distances.items() if distance == top_distance]
        for reindeer in top_reindeers:
            reindeers_points[reindeer] += 1

    for reindeer in reindeers_points:
        reindeers_points[reindeer] += reindeers_distances[reindeer]
    return max(reindeers_points.values())


def part2(lines):
    return solve1(lines, True)


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
            self.assertEqual(part1(lines, 1), 17)
            self.assertEqual(part1(lines, 10), 170)
            self.assertEqual(part1(lines, 11), 187)
            self.assertEqual(part1(lines, 1000), 1056 + 689)

    def test2(self):
        with open('input_part1.txt') as f:
            lines = f.read().splitlines()
            # 3724 too high
            self.assertEqual(part1(lines, 2503), 3724)


if __name__ == '__main__':
    unittest.main()

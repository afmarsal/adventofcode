import unittest
from collections import defaultdict


def read(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        start = [x for x, c in enumerate(lines[0]) if c == '.'][0], 0
        end = [x for x, c in enumerate(lines[len(lines)-1]) if c == '.'][0], len(lines)-1
        blizzards = []
        for y, line in enumerate(lines[1:len(lines)-1]):
            for x, c in enumerate(line):
                if c not in {'.', '#'}:
                    blizzards.append(((x, y+1), c))

        return start, end, len(lines[0]) - 1, len(lines) - 1, blizzards

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')


def print_valley(elf, start, end, wall_x, wall_y, blizzards):
    all_blizzards = defaultdict(list)
    for p, d in blizzards:
        all_blizzards[p].append(d)
    for y in range(wall_y + 1):
        for x in range(wall_x + 1):
            if (x, y) == elf:
                c = 'E'
            elif y == 0 or y == wall_y:
                c = '.' if (x, y) in {start, end} else '#'
            elif x == 0 or x == wall_x:
                c = '#'
            elif (x, y) in all_blizzards:
                if len(all_blizzards[(x, y)]) == 1:
                    c = all_blizzards[(x, y)][0]
                else:
                    c = len(all_blizzards[(x, y)])
            else:
                c = '.'
            log_nolf(c)
        log()


def add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def move_blizzard(b_pos, dir, wall_x, wall_y):
    match dir:
        case '^':
            new_pos = add(b_pos, UP)
            if new_pos[1] == 0:
                new_pos = (new_pos[0], wall_y - 1)
        case 'v':
            new_pos = add(b_pos, DOWN)
            if new_pos[1] == wall_y:
                new_pos = (new_pos[0], 1)
        case '<':
            new_pos = add(b_pos, LEFT)
            if new_pos[0] == 0:
                new_pos = (wall_x - 1, new_pos[1])
        case '>':
            new_pos = add(b_pos, RIGHT)
            if new_pos[0] == wall_x:
                new_pos = (1, new_pos[1])
    return new_pos

def best_path(start, end, wall_x, wall_y, blizzards):
    elf_pos = {start}
    # print_valley(elf, start, end, wall_x, wall_y, blizzards)
    i = 0
    while True:
        i = i + 1
        # Move blizzards
        all_blizzards = set()
        next_blizzards = []
        for b_pos, dir in blizzards:
            new_b_pos = move_blizzard(b_pos, dir, wall_x, wall_y)
            next_blizzards.append((new_b_pos, dir))
            all_blizzards.add(new_b_pos)
        blizzards = next_blizzards

        # Move elf
        next_elf_pos = set()
        for elf in elf_pos:
            if elf == end:
                return i - 1, blizzards
            for d in DOWN, RIGHT, UP, LEFT:
                new_elf = add(elf, d)
                if new_elf == end:
                    next_elf_pos.add(new_elf)
                elif 1 <= new_elf[0] < wall_x and 1 <= new_elf[1] < wall_y:
                    if new_elf not in all_blizzards:
                        # log(f'Adding way {d} {elf} -> {new_elf}')
                        next_elf_pos.add(new_elf)
            if elf not in all_blizzards:
                # log(f'Adding quiet {elf}')
                next_elf_pos.add(elf)
        elf_pos = next_elf_pos

        if i % 10 == 0:
            log(f'Minute: {i}')
        # for elf in elf_pos:
        #     log(f'elf at {elf}')
        #     print_valley(elf, start, end, wall_x, wall_y, blizzards)

def part1(filename):
    start, end, wall_x, wall_y, blizzards = read(filename)
    round, blizzards = best_path(start, end, wall_x, wall_y, blizzards)
    return round

def part2(filename):
    start, end, wall_x, wall_y, blizzards = read(filename)
    round1, blizzards = best_path(start, end, wall_x, wall_y, blizzards)
    round2, blizzards = best_path(end, start, wall_x, wall_y, blizzards)
    round3, blizzards = best_path(start, end, wall_x, wall_y, blizzards)
    log(f'r1: {round1}, r2: {round2}, r3: {round3}')
    # round 2 and 3 take 1 more, still don't know why
    return round1 + (round2 + 1) + (round3 + 1)


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(18, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(262, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(54, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(785, part2('input.txt'))

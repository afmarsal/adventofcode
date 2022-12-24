import unittest


def read(filename):
    with open(filename) as f:
        pairs = [((x, y), DIRECTIONS.copy()) for y, line in enumerate(f.read().splitlines()) for x, c in enumerate(line) if c == '#']
        return dict((p[0], p[1]) for p in pairs)

OFFSETS = {
    'N': [(-1, -1), (0, -1), (1, -1)],
    'S': [(-1, 1),  (0, 1),  (1, 1)],
    'W': [(-1, -1), (-1, 0), (-1, 1)],
    'E': [(1, -1),  (1, 0),  (1, 1)],
}
ALL_OFFSETS = {o for k, v in OFFSETS.items() for o in v}

DIRECTIONS = ['N', 'S', 'W', 'E']

def log(param='', end='\n'):
    # print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')


def print_map(elves):
    min_x = min(t[0] for t in elves) - 2
    min_y = min(t[1] for t in elves) - 2
    max_x = max(t[0] for t in elves) + 2
    max_y = max(t[1] for t in elves) + 2

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x + 1):
            log_nolf('#' if (x,y) in elves else '.')
        log()

def add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]

def move(elves):
    next_elves = {}
    curr_positions = elves.keys()
    # for each position, which elves end up there
    next_positions = {}
    for elf_pos, elf_directions in elves.items():
        # Elf not surrounded
        if all(add(elf_pos, o) not in curr_positions for o in ALL_OFFSETS):
            log(f'Elf at {elf_pos}: {elf_directions} not moving because its isolated')
            next_positions[elf_pos] = [elf_pos]
            continue
        for d in elf_directions:
            log(f'Trying to move elf at {elf_pos} {d}')
            for o in OFFSETS[d]:
                new_pos = add(elf_pos, o)
                if new_pos in curr_positions:
                    log(f'Elf at {elf_pos} can\'t move {o}')
                    break
            else:
                new_pos = add(elf_pos, OFFSETS[d][1])  # Final position is the "middle" offset
                if new_pos not in next_positions:
                    next_positions[new_pos] = []
                log(f'Elf at {elf_pos} will move to {new_pos}')
                next_positions[new_pos].append(elf_pos)
                break
        else:
            # Could not find a new pos to move
            log(f'Elf at {elf_pos} could not move in any direction')
            next_positions[elf_pos] = [elf_pos]
    for next_pos, original_pos_list in next_positions.items():
        if len(original_pos_list) == 1:
            original_pos = original_pos_list[0]
            next_elves[next_pos] = elves[original_pos][1:] + [elves[original_pos][0]]
        else:
            log(f'More than one elf at {next_pos}: can\'t move')
            for original_pos in original_pos_list:
                next_elves[original_pos] = elves[original_pos][1:] + [elves[original_pos][0]]
                log(f'Updating directions for elf at {original_pos}: {next_elves[original_pos]}')
    return next_elves


def part1(filename):
    elves = read(filename)
    print_map(elves.keys())
    for i in range(10):
        elves = move(elves)

    min_x = min(t[0] for t in elves)
    min_y = min(t[1] for t in elves)
    max_x = max(t[0] for t in elves)
    max_y = max(t[1] for t in elves)
    print_map(elves)
    return (max_y - min_y + 1) * (max_x - min_x + 1) - len(elves)


def part2(filename):
    elves = read(filename)
    print_map(elves.keys())
    i = 1
    while True:
        new_elves = move(elves)
        if new_elves.keys() == elves.keys():
            return i
        elves = new_elves
        i = i + 1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(110, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(3917, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(20, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(988, part2('input.txt'))

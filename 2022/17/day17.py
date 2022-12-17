import unittest

def read(filename):
    with open(filename) as f:
        return f.read().strip()

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')


def build_pieces():
    piece1 = {(0, 0), (1, 0), (2, 0), (3, 0)}
    piece2 = {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}
    piece3 = {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)}
    piece4 = {(0, 0), (0, 1), (0, 2), (0, 3)}
    piece5 = {(0, 0), (0, 1), (1, 0), (1, 1)}
    return [piece1, piece2, piece3, piece4, piece5]


def move_to(piece, x_offset, max_y):
    return set(map(lambda p: (p[0] + x_offset, max_y + p[1]), piece))


def move(piece, offset):
    return set(map(lambda p: (p[0] + offset[0], p[1] + offset[1]), piece))


def log_chamber(chamber, piece=frozenset()):
    max_y = max(y for x, y in chamber) + 6
    for y in range(max_y, 0, -1):
        log_nolf(f'{y:03d} |')
        for x in range(1, 8):
            if (x, y) in piece:
                char = '@'
            elif (x, y) in chamber:
                char = '#'
            else:
                char = '.'
            log_nolf(char)
        log('|')
    log('    +-------+')
    log()

FLOOR = {(x, 0) for x in range(9)}

def settle_piece(jets, jet_idx, piece, base):
    if not base:
        max_y = 0
    else:
        max_y = max(y for x, y in base)
    piece = move_to(piece, 3, max_y + 4)
    chamber = FLOOR | base.copy()
    settled = False
    while not settled:
        # move left, right
        jet = jets[jet_idx % len(jets)]
        jet_idx += 1
        offset = (1, 0) if jet == '>' else (-1, 0)
        moved_piece = move(piece, offset)
        if moved_piece.isdisjoint(chamber) \
                and all(0 < x < 8 for x, y in moved_piece):
            piece = moved_piece
        # move down
        offset = (0, -1)
        moved_piece = move(piece, offset)
        if moved_piece.isdisjoint(chamber):
            piece = moved_piece
        else:
            chamber.update(piece)
            settled = True
        # log_chamber(chamber, piece)
    return jet_idx, chamber

def calc_height(filename, rocks):
    jets = read(filename)
    pieces = build_pieces()

    cycle_start = 16
    rocks_in_cycle = 35
    # After cycle_start (16) iterations, there's a cycle of rocks_in_cycle (35)

    # Start the first group of rocks
    jet_idx = 0
    chamber = set()
    for rock in range(cycle_start):
        piece = pieces[rock % len(pieces)]
        jet_idx, chamber = settle_piece(jets, jet_idx, piece, chamber)
    next_rock = cycle_start
    max_y = max(y for x, y in chamber)
    # log_chamber(chamber)
    first_height = max_y

    # Calculate the delta height for a cycle
    jet_idx2 = jet_idx
    log(f'rock: {next_rock}, jet: {jet_idx2}')
    for rock in range(next_rock, next_rock + rocks_in_cycle):
        piece = pieces[rock % len(pieces)]
        jet_idx2, chamber = settle_piece(jets, jet_idx2, piece, chamber)
        log(f'rock: {rock}, jet: {jet_idx2}')
    max_y = max(y for x, y in chamber)
    height_delta = max_y - first_height

    # Now put on top the last "batch" of rocks
    num_cycles, remainder = divmod(rocks - cycle_start, rocks_in_cycle)
    jet_idx3 = jet_idx2
    next_rock = next_rock + rocks_in_cycle
    for rock in range(next_rock, next_rock + remainder):
        piece = pieces[rock % len(pieces)]
        jet_idx3, chamber = settle_piece(jets, jet_idx3, piece, chamber)
        log(f'rock: {rock}, jet: {jet_idx2}')
    max_y = max(y for x, y in chamber)
    last_height = max_y - (first_height + height_delta)

    log_chamber(chamber)

    return first_height + height_delta * num_cycles + last_height

def part1(filename):
    return calc_height(filename, 2022)


def part2(filename):
    return calc_height(filename, 1000000000000)

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(3068, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(3102, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1514285714288, part2('sample.txt'))

    def test_input(self):
        # 1571428571425 too high
        self.assertEqual(-2, part2('input.txt'))

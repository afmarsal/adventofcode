import unittest

def read(filename):
    with open(filename) as f:
        return f.read().strip()

def log(param='', end='\n'):
    # print(param, end=end)
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

def guess_cycle_len(seq):
    min_cycle_length = 20
    if len(seq) // 2 <= min_cycle_length:
        return None, None
    for x in range(len(seq)//2):
        cycle_length = min_cycle_length + x
        if 2 * cycle_length >= len(seq):
            return None, None
        if seq[-cycle_length:] == seq[-2 * cycle_length:-cycle_length]:
            log(f'Seq found. len: {x+min_cycle_length}')
            return len(seq) - 2*cycle_length, cycle_length
    return None, None

def find_cycles(jets, pieces):
    jet_idx = 0
    chamber = set()
    jet_idxs = []
    rock = 0
    while True:
        piece = pieces[rock % len(pieces)]
        jet_idx, chamber = settle_piece(jets, jet_idx, piece, chamber)
        jet_idxs.append(jet_idx % len(jets))
        log(f'idx: {rock}, jet: {jet_idx % len(jets)}')
        cycle_start, cycle_len = guess_cycle_len(jet_idxs)
        if cycle_start:
            return cycle_start, cycle_len
        rock += 1

def calc_height(filename, rocks):
    jets = read(filename)
    pieces = build_pieces()

    # After cycle_start (16) iterations, there's a cycle of rocks_in_cycle (35)
    cycle_start, rocks_in_cycle = find_cycles(jets, pieces)
    cycle_start += 2   # For some reason have to add this small offset to make it work

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
        self.assertEqual(1539823008825, part2('input.txt'))

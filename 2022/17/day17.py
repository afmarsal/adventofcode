import unittest

import numpy as np


def read(filename):
    with open(filename) as f:
        return f.read().strip()

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')


def build_chamber():
    piece1 = {(0, 0), (1, 0), (2, 0), (3, 0)}
    piece2 = {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}
    piece3 = {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)}
    piece4 = {(0, 0), (0, 1), (0, 2), (0, 3)}
    piece5 = {(0, 0), (0, 1), (1, 0), (1, 1)}
    pieces = [piece1, piece2, piece3, piece4, piece5]
    
    # wall_left = {(0, y) for y in range(4000)}
    # wall_right = {(8, y) for y in range(4000)}
    chamber = {(x, 0) for x in range(9)}
    return chamber, pieces


def move_to(piece, x_offset, max_y):
    return set(map(lambda p: (p[0] + x_offset, max_y + p[1]), piece))


def move(piece, offset):
    return set(map(lambda p: (p[0] + offset[0], p[1] + offset[1]), piece))


def log_chamber(chamber, piece):
    max_y = max(y for x, y in chamber) + 6
    for y in range(max_y, 0, -1):
        log_nolf('|')
        for x in range(1, 8):
            if (x, y) in piece:
                char = '@'
            elif (x, y) in chamber:
                char = '#'
            else:
                char = '.'
            log_nolf(char)
        log('|')
    log('+-------+')
    log()

def part1(filename):
    jets = read(filename)
    log(f'jets: {jets}')
    max_y = 0
    rocks = 2022
    chamber, pieces = build_chamber()
    jet_idx = 0
    for i in range(rocks):
        piece = pieces[i % len(pieces)]
        piece = move_to(piece, 3, max_y + 4)
        # log(f'Start')
        # log_chamber(chamber, piece)
        settled = False
        while not settled:
            # move left, right
            # log('Before  move')
            # log_chamber(chamber, piece)
            jet = jets[jet_idx % len(jets)]
            jet_idx += 1
            offset = (1, 0) if jet == '>' else (-1, 0)
            moved_piece = move(piece, offset)
            if moved_piece.isdisjoint(chamber) and all(0 < x < 8 for x, y in moved_piece):
                piece = moved_piece
            # log(f'After move 1, offset: {offset}')
            # log_chamber(chamber, piece)
            # move down
            offset = (0, -1)
            moved_piece = move(piece, offset)
            if moved_piece.isdisjoint(chamber):
                piece = moved_piece
            else:
                chamber.update(piece)
                max_y = max(y for x, y in chamber)
                settled = True
                # log(f'Settled at: {piece}')
                # log_chamber(chamber, set())
            # log(f'After move 2. Settled: {settled}')

    return max_y

def part2(filename):
    return -1

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(3068, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

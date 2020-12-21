import functools
import math
import operator
import re
import numpy as np


def up(arr):
    return ''.join(arr[0,])


def down(arr):
    return ''.join(arr[-1,])


def right(arr):
    return ''.join(arr[:, -1])


def left(arr):
    return ''.join(arr[:, 0])


DIRECTIONS = {'up': ('down', up),
              'down': ('up', down),
              'left': ('right', left),
              'right': ('left', right)}


class Tile:

    def __init__(self, id, pieces) -> None:
        self.id = id
        self.tile = np.array([list(s) for s in pieces])
        self.combos = []
        self.combos.append(self.tile)
        self.combos.append(np.rot90(self.tile, 1, (1, 0)))
        self.combos.append(np.rot90(self.tile, 2, (1, 0)))
        self.combos.append(np.rot90(self.tile, 3, (1, 0)))
        self.combos.append(np.flipud(self.tile))
        self.combos.append(np.flipud(np.rot90(self.tile, 1, (1, 0))))
        self.combos.append(np.flipud(np.rot90(self.tile, 2, (1, 0))))
        self.combos.append(np.flipud(np.rot90(self.tile, 3, (1, 0))))

    def sides(self):
        return {'up': up(self.tile),
                'down': down(self.tile),
                'right': right(self.tile),
                'left': left(self.tile)}

    def __repr__(self) -> str:
        # return f"tile: {self.id}\n{self.tile}\n{self.sides}"
        return f"tile: {self.id}"


def parse(lines):
    tiles = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('Tile'):
            tile_id = int(re.match(r'Tile (\d+):', lines[i])[1])
            i += 1
            pieces = lines[i:i + 10]
            tiles.append(Tile(tile_id, pieces))
            i += 11
    print(f'Total tiles: {len(tiles)}')
    return tiles


def do_it(lines):
    tiles = parse(lines)
    matching = {tile.id: [] for tile in tiles}
    for i, tile in enumerate(tiles):
        for j in range(i + 1, len(tiles)):
            found = False
            for ori, side in tile.sides().items():
                for direction in DIRECTIONS:
                    for combo_j in tiles[j].combos:
                        if side == DIRECTIONS[direction][1](combo_j):
                            matching[tile.id].append((ori, tiles[j].id, DIRECTIONS[ori][0], combo_j))
                            matching[tiles[j].id].append((DIRECTIONS[ori][0], tile.id, ori, tile.tile))
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
    # print(matching)
    # for k, v in matching.items():
    #     print(f'{k} -> {v}')
    # Take first border
    sides = int(math.sqrt(len(tiles)))
    square = [[None] * sides] * sides
    # corner0 = [k for k, v in matching.items() if v == 4][0]


if __name__ == '__main__':
    with open('input0.txt') as f:
        lines = list(map(str.strip, f))

    output = do_it(lines)
    print(f'Part 2: {output}')

# Part 2:

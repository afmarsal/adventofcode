import functools
import operator
import re


class Tile:

    def __init__(self, id, pieces) -> None:
        self.id = id
        self.sides = []
        self.sides.append(pieces[0])
        self.sides.append(pieces[0][::-1])
        self.sides.append(pieces[-1])
        self.sides.append(pieces[-1][::-1])
        s = ''.join([p[0] for p in pieces])
        self.sides.append(s)
        self.sides.append(s[::-1])
        s = ''.join([p[-1] for p in pieces])
        self.sides.append(s)
        self.sides.append(s[::-1])

    def __repr__(self) -> str:
        return f"tile: {self.id}\n{self.sides}"


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
    matching = {tile.id: 0 for tile in tiles}
    for i, tile in enumerate(tiles):
        for side in tile.sides:
            for j in range(i + 1, len(tiles)):
                if side in tiles[j].sides:
                    matching[tile.id] += 1
                    matching[tiles[j].id] += 1
    return functools.reduce(operator.mul, [k for k, v in matching.items() if v == 4], 1)


if __name__ == '__main__':
    with open('input1.txt') as f:
        lines = list(map(str.strip, f))

    output = do_it(lines)
    print(f'Part 1: {output}')

# Part 1: 15670959891893

import math
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

    # def sides(self):
    #     return {'up': up(self.tile),
    #             'down': down(self.tile),
    #             'right': right(self.tile),
    #             'left': left(self.tile)}

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Tile):
            return self.id == o.id
        raise NotImplemented

    def __hash__(self) -> int:
        return self.id

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


def get_matches(tiles):
    matching = {tile.id: set() for tile in tiles}
    for i, tile in enumerate(tiles):
        for side in tile.sides:
            for j in range(i + 1, len(tiles)):
                if side in tiles[j].sides:
                    matching[tile.id].add(tiles[j])
                    matching[tiles[j].id].add(tile)
    print(matching)
    return matching


def print_board(board):
    s = 0
    for i in range(10):
        for s in range(2):
            print(''.join([str(j) for j in board[0][s][i]]), end='')
            print(' ', end='')
        print()


def arrange(tiles, matching):
    sides = int(math.sqrt(len(tiles)))
    board = np.empty((sides, sides), dtype=object)
    corner_id = [m for m, k in matching.items() if len(k) == 2][0]
    print(f'up left corner: {corner_id}')
    top_right = [t for t in tiles if t.id == corner_id][0]
    # Fix one corner as the top right corner, and match it with the next to the right
    for top_right_combo in top_right.combos:
        found = False
        for adj in matching[corner_id]:
            for adj_combo in adj.combos:
                if right(top_right_combo) == left(adj_combo):
                    found = True
                    board[0][0] = top_right_combo
                    board[0][1] = adj_combo
                    matching[top_right.id].remove(adj)
                    break
            if found:
                break
        if found:
            break

    print('Before orienting')
    print_board(board)
    # get right orientation: match the tile below the top right corner
    adj = list(matching[corner_id])[0]
    for adj_combo in adj.combos:
        if down(board[0][0]) == up(adj_combo):
            print(f'1,0: {adj.id}')
            board[1][0] = adj_combo
            break
    else:
        # Could not find match => flip
        board[0][0] = np.flipud(board[0][0])
        board[0][1] = np.flipud(board[0][1])
        # And now the 1, 0 piece should match
        for adj_combo in adj.combos:
            if down(board[0][0]) == up(adj_combo):
                print(f'1,0: {adj.id}')
                board[1][0] = adj_combo
                break
        else:
            raise Exception('Could not match 1, 0!!!')

    # for top_right_combo in curr.combos:
    #     found = False
    #     for adj in matching[corner_id]:
    #         for adj_combo in adj.combos:
    #             if right(top_right_combo) == left(adj_combo):
    #                 found = True
    #                 print(f'next: {adj.id}')
    #                 board[0][2] = adj_combo.tolist()
    #                 curr = adj
    #                 break
    #         if found:
    #             break
    #     if found:
    #         break

    print('After orienting')
    print_board(board)


def do_it(lines):
    tiles = parse(lines)
    matches = get_matches(tiles)
    arrange(tiles, matches)
    # corner0 = [k for k, v in matching.items() if v == 4][0]


if __name__ == '__main__':
    with open('input0.txt') as f:
        lines = list(map(str.strip, f))

    output = do_it(lines)
    print(f'Part 2: {output}')

# Part 2:

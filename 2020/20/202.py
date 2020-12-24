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
        self.final_combo = None

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
    for board_row in range(len(board)):
        for tile_row in range(10):
            for board_col in range(len(board)):
                print(''.join([str(j) for j in board[board_row][board_col].final_combo[tile_row]]), end='')
                print(' ', end='')
            print()
        print()


def arrange(tiles, matching):
    sides = int(math.sqrt(len(tiles)))
    # The full board where all the tiles are positioned
    # X axis is second coordinate -> 0,1; 0,2 and so on
    board = np.empty((sides, sides), dtype=object)
    # Select one random corner as the top left corner
    corner_id = [m for m, k in matching.items() if len(k) == 2][0]
    print(f'up left corner: {corner_id}')
    top_left = [t for t in tiles if t.id == corner_id][0]
    # Find the tile to the right
    for top_left_combo in top_left.combos:
        found = False
        for adj in matching[corner_id]:
            for adj_combo in adj.combos:
                if right(top_left_combo) == left(adj_combo):
                    found = True
                    fix_tile(board, matching, (0, 0), top_left, top_left_combo, adj)
                    fix_tile(board, matching, (0, 1), adj, adj_combo, top_left)
                    break
            if found:
                break
        if found:
            break

    # Make sure the orientation is correct (as of now, it could be the bottom left)
    adj = list(matching[corner_id])[0]
    for adj_combo in adj.combos:
        if down(board[0][0].final_combo) == up(adj_combo):
            fix_tile(board, matching, (1, 0), adj, adj_combo, board[0][0])
            break
    else:
        # Could not find match => flip
        board[0][0].final_combo = np.flipud(board[0][0].final_combo)
        board[0][1].final_combo = np.flipud(board[0][1].final_combo)
        # And now the 1, 0 piece should match
        for adj_combo in adj.combos:
            if down(board[0][0].final_combo) == up(adj_combo):
                print(f'1,0: {adj.id}')
                fix_tile(board, matching, (1, 0), adj, adj_combo, board[0][0])
                break
        else:
            raise Exception('Could not match 1, 0!!!')

    # We have positions (0, 0), (1, 0) and (0, 1) fixed.
    # Let's match the rest first row
    for board_col in range(1, sides - 1):
        ref = board[0][board_col]
        for adj in matching[ref.id]:
            for adj_combo in adj.combos:
                if right(ref.final_combo) == left(adj_combo):
                    fix_tile(board, matching, (0, board_col + 1), adj, adj_combo, ref)

    # rest of rows
    for board_row in range(1, sides):
        for board_col in range(0, sides):
            ref = board[board_row-1][board_col]
            for adj in matching[ref.id]:
                for adj_combo in adj.combos:
                    if down(ref.final_combo) == up(adj_combo):
                        fix_tile(board, matching, (board_row, board_col), adj, adj_combo, ref)

    print('After orienting')
    print_board(board)
    return board


def fix_tile(board, matching, pos, tile, tile_combo, adj):
    tile.final_combo = tile_combo
    matching[tile.id].discard(adj)
    board[pos[0]][pos[1]] = tile


def do_it(lines):
    tiles = parse(lines)
    matches = get_matches(tiles)
    arrange(tiles, matches)
    # corner0 = [k for k, v in matching.items() if v == 4][0]


if __name__ == '__main__':
    with open('input1.txt') as f:
        lines = list(map(str.strip, f))

    output = do_it(lines)
    print(f'Part 2: {output}')

# Part 2:

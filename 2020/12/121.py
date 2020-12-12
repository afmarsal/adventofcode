class Coord:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if type(other) == int:
            return Coord(self.x * other, self.y * other)
        else:
            raise NotImplemented

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y

    def __repr__(self) -> str:
        return f'Coord({self.x},{self.y})'


NORTH = Coord(0, 1)
EAST = Coord(1, 0)
SOUTH = Coord(0, -1)
WEST = Coord(-1, 0)
DIRECTIONS = {'N': NORTH, 'E': EAST, 'S': SOUTH, 'W': WEST}
ALL = list(DIRECTIONS.values())


def rotate(coord, direction, times):
    factor = 1 if direction == 'R' else -1
    nex_idx = (ALL.index(coord) + (factor * times)) % len(ALL)
    return ALL[nex_idx]


class Boat:

    def __init__(self) -> None:
        self.pos = Coord(0, 0)
        self.dir = EAST

    def move(self, move, distance):
        original_pos = Coord(self.pos.x, self.pos.y)
        original_dir = Coord(self.dir.x, self.dir.y)
        if move in DIRECTIONS.keys():
            self.pos = self.pos + (DIRECTIONS[move] * distance)
        elif move in ('L', 'R'):
            self.dir = rotate(self.dir, move, int(distance / 90))
        elif move == 'F':
            self.pos = self.pos + (self.dir * distance)
        else:
            print(f'Dont know {move}, {distance}')
            raise Exception('WAT!')
        print(f'{original_pos}, {original_dir} + [{move}:{distance}] -> {self.pos}, {self.dir}')


def do_it(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f]
    boat = Boat()
    for line in lines:
        boat.move(line[0], int(line[1:]))
    return boat.pos.manhattan()


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 1007

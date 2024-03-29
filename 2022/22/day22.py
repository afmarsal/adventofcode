import functools
import unittest

def read(filename):
    global lines
    with open(filename) as f:
        lines = f.read().splitlines()
        max_x = max(x for y, line in enumerate(lines) for x, c in enumerate(line))
        for y, line in enumerate(lines):
            lines[y] = line + ' ' * (max_x - len(line) + 1)
        return lines

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)
DIRECTIONS = [RIGHT, DOWN, LEFT, UP]

def add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]

@functools.cache
def find_max_y(row):
    return max(y for y, line in enumerate(lines) if line[row] != ' ')

@functools.cache
def find_min_y(row):
    return min(y for y, line in enumerate(lines) if line[row] != ' ')

@functools.cache
def find_max_x(col):
    return max(x for x, c in enumerate(lines[col]) if c != ' ')

@functools.cache
def find_min_x(col):
    return min(x for x, c in enumerate(lines[col]) if c != ' ')

def new_pos1(pos_y, pos_x, dir):
    global lines
    new_y, new_x = add((pos_y, pos_x), dir)
    if not 0 <= new_y < len(lines) \
            or not 0 <= new_x < len(lines[0]) \
            or lines[new_y][new_x] == ' ':
        if dir == UP:
            new_y = find_max_y(new_x)
        elif dir == DOWN:
            new_y = find_min_y(new_x)
        elif dir == LEFT:
            new_x = find_max_x(new_y)
        elif dir == RIGHT:
            new_x = find_min_x(new_y)
    return new_y, new_x, dir


def calc(filename, path, new_pos_func):
    global lines
    read(filename)
    starting_x = min(x for x, c in enumerate(lines[0]) if c == '.')
    dir = RIGHT
    pos_y, pos_x = 0, starting_x
    log(f'Starting: {pos_y}, {pos_x}, direction: {dir}')
    idx = 0
    reading_steps = True
    while idx < len(path):
        # Parse path
        if reading_steps:
            token = path[idx]
            if idx + 1 < len(path) and path[idx+1].isdigit():
                token += path[idx+1]
                idx += 1
            if idx + 1 < len(path) and path[idx+1].isdigit():
                token += path[idx+2]
                idx += 1
            steps = int(token)
            rotate = None
        else:
            rotate = path[idx]
            steps = -1
        reading_steps = not reading_steps
        idx += 1

        match rotate:
            case 'R':
                dir = DIRECTIONS[(DIRECTIONS.index(dir) + 1) % len(DIRECTIONS)]
            case 'L':
                dir = DIRECTIONS[(DIRECTIONS.index(dir) - 1) % len(DIRECTIONS)]
            case _:
                for s in range(steps):
                    new_y, new_x, new_dir = new_pos_func(pos_y, pos_x, dir)
                    if lines[new_y][new_x] == '#':
                        log(f'Found wall at: {new_y}, {new_x}')
                        break
                    pos_y, pos_x, dir = new_y, new_x, new_dir
                    log(f'Moved to {pos_y}, {pos_x}')

    return (pos_y + 1) * 1000 + (pos_x + 1) * 4 + DIRECTIONS.index(dir)


def part1(filename, path):
    return calc(filename, path, new_pos1)


def quadrant(pos_y, pos_x):
    global lines
    quad_size = quadrant_size()
    return pos_y // quad_size, pos_x // quad_size


def quadrant_size():
    global lines
    return max(len(lines), len(lines[0])) // 4


def new_pos2(pos_y, pos_x, dir):
    global lines
    global quadrant_mappings
    new_y, new_x = add((pos_y, pos_x), dir)
    if quadrant(pos_y, pos_x) != quadrant(new_y, new_x):
        new_quadrant, new_dir = quadrant_mappings[quadrant(pos_y, pos_x)][dir]
        rel_y = pos_y % quadrant_size()
        rel_x = pos_x % quadrant_size()
        if new_dir == UP:
            new_rel_y = quadrant_size() - 1
            if dir == UP:
                new_rel_x = rel_x
            elif dir == DOWN:
                new_rel_x = quadrant_size() - 1 - rel_x
            elif dir == RIGHT:
                new_rel_x = rel_y
            else:
                new_rel_x = quadrant_size() - 1 - rel_y
        elif new_dir == DOWN:
            new_rel_y = 0
            if dir == UP:
                new_rel_x = quadrant_size() - 1 - rel_x
            elif dir == DOWN:
                new_rel_x = rel_x
            elif dir == RIGHT:
                new_rel_x = quadrant_size() - 1 - rel_y
            else:
                new_rel_x = rel_y
        elif new_dir == LEFT:
            new_rel_x = quadrant_size() - 1
            if dir == UP:
                new_rel_y = quadrant_size() - 1 - rel_x
            elif dir == DOWN:
                new_rel_y = rel_x
            elif dir == RIGHT:
                new_rel_y = quadrant_size() - 1 - rel_y
            else:
                new_rel_y = rel_y
        elif new_dir == RIGHT:
            new_rel_x = 0
            if dir == UP:
                new_rel_y = rel_x
            elif dir == DOWN:
                new_rel_y = quadrant_size() - 1 - rel_x
            elif dir == RIGHT:
                new_rel_y = rel_y
            else:
                new_rel_y = quadrant_size() - 1 - rel_y
        else:
            raise Exception('Invalid dir')
        new_y = new_quadrant[0] * quadrant_size() + new_rel_y
        new_x = new_quadrant[1] * quadrant_size() + new_rel_x
        log(f'Moving from\n[{pos_y}, {pos_x}] (rel: {rel_y}, {rel_x}, d: {dir}), q: {quadrant(pos_y, pos_x)}) to \n'
            f'[{new_y}, {new_x}] (rel: {new_rel_y}, {new_rel_x}] d: {new_dir}, q: {new_quadrant}')
        return new_y, new_x, new_dir

    return new_y, new_x, dir

def part2(filename, path):
    return calc(filename, path, new_pos2)

smp = "10R5L5R10L4R5L5"
inp = "22R34R41L30L16R22R49R7L23R6R30L35L27L13L20R33R9R7R42R36R26L13R30R10L1L36R35R48R33L4L50R28L50R38L10R30R34L11L27L29R3R3L29R3L20L21R49L47L18R12R31R22L27L31R8R11L27R29L26R31L2L43L23L25L18L48R50L34R16L10R11L41R27L34L29R42L13L31L26R20R21R38L21L24R42R30R42L27R33L38L26L19L40R32R35L13L21R20L5R26L38L4L43L21R30R38L29L4R25L3L40R44L2R17R13R24L29L6R41L29R37R34R36R26L18R6L41L6R28L3L38L49L48L21R23R42R50R33L40L16R5R19R17R24L48R2R43R14L27R36R32R17R27R48R50R22L32L15L4L43R17L45L37L14R14R8L5R31R43R28L20L50L7R17R41R50R40L26L47R18R11R16R14R32R32R35R40R13L43R13R29L8R24L10L41L29L36R36L11R7R6L46L24R3L32R46R48R25R6R34L40L28L9L13L24L2L2R6L22R22R14L19R4L24L46L18R25L41L14R49L3R14R13R8R20L38R22R24L22R12R34L18R2R44R31R34L20L28L48L19R19L42R23L31L16R46R18L34L42R33R39R46L19L29L16L35L7R41R32L12L15L40L50L16R38L36R8R50L20L4L2R33L47L44R29R11R12R31R43L25L38L42L37R8L21L27L6R3R12R37L46L6R18R24L7R32L41R15L49L38R8L31R32R24L1R3R5R23L39R9L39L35L21L34R29L44L8L9L35L20R31R23R25L32L6L45L41R7R16L13R8R34R3R7L23R15L20L33R33L46R35L22L48L12L43R45R5L8L36R44L8L11L48L6R49L10R34R44R32L9L27L33L8L46R34R23R21L19L1L37L12R36R40L27R8L9R4L34R10L10R8L22R26R15L5R12L39R28R5R32R31L36L47L4L39L37L37L22R38R43R31R20L25L9L13L5R33L35L5R45R41L8R20L19L2L47L45L3L25L30R45L5L4L27R23L4R6R8R9R22R19R2L31L6L23R37L19R37L15L27L23R34L4L1L22R30R35L20R8R5R39L17R41R27R32R42L7L42R50L7L22L1L25R4L14L34R19R2L21R46R27L38L42R10L43L39L41L2R45L32R44L3L14L4R47R27R25L45R44R3L25R42R7L44R23R35L49R1L46R11L38R41R48R23L6L38L19R44R21L47L23R10L39R45L50R1R42R3R50L12L26L7L38L7L42L1R44L20R49L22R23R33R17R38R44L2L23R1R13L43L16L50L43R28R5L10R35R46R10L39R22R37R7R33L6L26R12L15R49L33R9R9L44R38L16L26R16R30R38R27L33L19L4L2R38R22R22L39R37L6L32R43R5L17R35R45L21L2L19L49R11L33R15L3R16R6L48R13R8L28R22L31R35R13L11L42L31L32R12R23L6L39L31L34R28L34L36L45R28R36R19R38L8L2L13L27L18L43L39L23L29L26R10L15R14R3L45L5R43L46L3L17R31L19R40L6R11R9R22R27R18R1R11R2L27R50L39R43L22R11L49L9R32R26R20L33L46L32L45L44R46L12R25R49R24L22R29L40R8R14R8R49L31L35R40L8L34L32R14R27R25L27R6R27L19L17L17L18L1L8R43R7L44R13L4R2R2R29L44L41L4L50R33R17L24R42R18R17L4R27R1L10L41R12L47R28R42L9L4R23R17R11L37R25L5L47R29R13L42R32L6R29L35L36R10R28L47L11R50L22R12R32L19L19L12L13L31L4R26L29R14L18R31R17R28R19L13L34L25R19L41R16R28R48R13R8L21L34L37L37R31R13L41L12R31L44L22R33L7L6R5L27R22L12R31R30R14R16L30R16L39L31R44R41R40R34R16L36R39L5R21R19R45L46L50L22L34R12L35L27L46R13L14L47R15R24L12L27R8R24R19R40R43L12R31R41R29R46L43R45L1R18R34L5R35R31R2L31R16R19R38L3L40R24L4L8R30L24L3L24R7R27R29L37L47L17L21R43R42R13L22R11L2L2L45L16R35R27L9R20R24L33R45R46L4R11R6L1L46R38L49R37L26R38R50L22L18L5L31L32R45R36R47L5R47L42R49L15R9R3L38L29R46L5R19R42L2L25R19R47R48R7L13R25L3L13L19L6L27L48L2L48R5R12L9L11R18R7R25L3L5L11R29R32L8R41L5L29L26L26R4R11R46L19L28L33L5R30L45L16R40R19L42R26L28R12R5L1R50L26L48R22L27L17L22L8L22L37L22R48R45L21R47L44R11R46R30R1R2L33L50L35L37L30L23L16L8L29R49R25L22R40L18R15R10R2R5L40L14L35R23L12R8R15R22L20R19R47L34L35L5R31L14L46L33L38L45L5L44L30R50R9R13R4R5R10L14R23L16L16R49R25R11R40R18L18R33R47R15L31R39R43R13L19R39R45L18L12R11L2L14L28R4R23R13R13R49R6R29L31R14L45R30L26L25R44L16R30R5L36L32R37R32R29R22R2L20R12L5R16L18L40R18L16L43R3L6L33R31L27R41L8R6L38R47R18R33R44R21R20R46R34L27L20R16R4R5R38L39R49R46L48R6R37R25R6R4L43L8L47R46R40R15L15L42R49L5L45R36L27R45R33R14L21R25R4R42L9L40R44L4R28L3L48L20R24R39R39L3L46R19L13R49R28R32L1R22L31L45L21L43L34L5L48L5R11R31L48L8R42L15R6L20R48L38L13R39R26L29L2R25R33R42R35L9R34R49R26L10L1L49R10R50L3R15L8L46R30L2L23L17L16L33L14L9L12R11R30R12R16R12L14L29R28R9R46L21L11R13L43L18R18R37L7L34L22L23L4R5L42R30L49L4R5R41L1R46L12R45L15R9L29R9L16R10L36L22L5R42R40L41L50R48R31R40R40R12L48L25R28L13L49R41L50L18R27L15R43R11L26L1R24L36L29L7L26L30R5R6L4R24L5R14L46L48L25L32L30L10R42L33L33L45R44L1L15L19L20L3R29L48L27R13L14R8L5L37L17L3L32R26L38R27L38L30R6L28R44L20R17L43R6R5L15L18L36L41L29L42R43R43L41L42R12L39L26R42L15L13L38R2R41R13R39R27L15R21R12R42L17R4R42R14L45R47L40L2L26R42R11R15L34R35R39L3L30R26L28L1R1L30R15L20L25R5L25L2R27L35L6R33R3L46L2L16L31R15L7L34R8R26L12R48R31L21R20L17R35R32L21R13L11R36L6L1R42L4L2R17R5L26R45L35R42L48R6L5R35R38R1R11L23L25R38R28R5L42R32R9R47L15R5R47L39R1L19L27L35L36L39L35L10R10L24R41R24R48L1L31L24L49L24R27L31R45R19R31L9L45L3L14R20R32L8L45R22R8R46R23L50R33L1L27R38R32L14L38R18L26R8L34R9R34L29R39L41R2R2R46R34L4L31L15L34R4L31L31L4R7L3R18R33L22L44L5R34R43L4L45L12L24R23L46L23R36L25R34R9L22R2R5L36L11L39L45R39R38R4L18R12R28L44L28R27R29R23R11R19L49L18L21L20L24L24L20L44L26L36R13R44L48R20R36R13R20R42R45R17L16R49L38L39L6R20L41L35L44R11R23L31L8R28R33R48L46L49L1R44L40L30R39L25L13R14L22R6L13L20R38L5L44R16R27L46L23L22L20L49L1R38R20R29L3L49R35L23R50R32L28L40R17L2L45R40L21R42L21R7L17R18R22R29R19R20R29L26R6L17L22R37R15L30R13R7R17L29R14R34L8R47L41L17R14R29L4R25L1R15R4R30R45L40R10L6R46R1R7R25R44R6R20L43L38R22L33L20R30R11L42L38L34L26R46L5R23R31R12R24R9R10R3L46L45L24R49L50R34L37R20L32L14L46R46R5R26L27L38R27R21R5L45R27R30R30R50L27L2R48L37R11R4R45L17R28L5L13L43L48R39R29L10L26L21L30L43R26L12L19L28R45R33R25R37L4R37R33R8R48R24R24L26R18L32R23L42L14L35R50L36L45L32L40L5R42R44R32R30R16R2L27R24L10L10L33R7L29L9R26R23R1L35R13L25R33R21L31R49R21L44L34L16L41L20L2R30L43L10R11R27L42L26R49L10L8L31R2R29R21L43L24L23R13L19L37R17L5L44R4L35L38R46R28L22R5L37L32R36L6R12L35L50L43L4L16R38L13L20R35L30R27L21R41R41L50R39L14L12R18R36R4R34R15R16R47R23R42R41L13R33R24L2L7L8R5L23L30R41R43L11L2R17L48L18L28R5L23R25R45R9R21L34R9L38R27L18L41R3R35L28R37L47R18R40L14L21R50R28L8L15L23L28L37R24L33L20L20R1R7L36R17R18L21L20R14R32R43L35R5L9R38L8L12L29R10R14L31R46R36L27R39R11R13L29R49R13R34R6L48R41L18L28L11R41R45L31L46L44R11R24L41R13L42R41L23L34L14L10R41L18R25L6R8R36R46L8L40R50R21L43L13R42L13L39R33L22R6R32R41L4L4R22R38R39L42L36L20R4R28L3L18L2"

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(6032, part1('sample.txt', smp))

    def test_input(self):
        self.assertEqual(149138, part1('input.txt', inp))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        global quadrant_mappings
        QUAD_1 = (0, 2)
        QUAD_2 = (1, 0)
        QUAD_3 = (1, 1)
        QUAD_4 = (1, 2)
        QUAD_5 = (2, 2)
        QUAD_6 = (2, 3)
        quadrant_mappings = {
            QUAD_1: {  # QUAD 1
                # dir: quadrant, new direction
                UP: (QUAD_2, DOWN),
                DOWN: (QUAD_4, DOWN),
                RIGHT: (QUAD_6, LEFT),
                LEFT: (QUAD_3, DOWN)
            },
            QUAD_2: {
                UP: (QUAD_1, DOWN),
                DOWN: (QUAD_5, UP),
                RIGHT: (QUAD_3, RIGHT),
                LEFT: (QUAD_6, UP),
            },
            QUAD_3: {
                UP: (QUAD_1, RIGHT),
                DOWN: (QUAD_5, RIGHT),
                RIGHT: (QUAD_4, RIGHT),
                LEFT: (QUAD_2, LEFT)
            },
            QUAD_4: {
                UP: (QUAD_1, UP),
                DOWN: (QUAD_5, DOWN),
                RIGHT: (QUAD_6, DOWN),
                LEFT: (QUAD_3, LEFT)
            },
            QUAD_5: {
                UP: (QUAD_4, UP),
                DOWN: (QUAD_2, UP),
                RIGHT: (QUAD_6, RIGHT),
                LEFT: (QUAD_3, UP)
            },
            QUAD_6: {
                UP: (QUAD_4, RIGHT),
                DOWN: (QUAD_2, RIGHT),
                RIGHT: (QUAD_1, LEFT),
                LEFT: (QUAD_5, LEFT)
            },
        }
        self.assertEqual(5031, part2('sample.txt', smp))

    def test_input(self):
        global quadrant_mappings
        QUAD_1 = (0, 1)
        QUAD_2 = (0, 2)
        QUAD_3 = (1, 1)
        QUAD_4 = (2, 0)
        QUAD_5 = (2, 1)
        QUAD_6 = (3, 0)
        quadrant_mappings = {
            QUAD_1: {  # QUAD 1
                # dir: quadrant, new direction
                UP: (QUAD_6, RIGHT),
                DOWN: (QUAD_3, DOWN),
                RIGHT: (QUAD_2, RIGHT),
                LEFT: (QUAD_4, RIGHT)
            },
            QUAD_2: {
                UP: (QUAD_6, UP),
                DOWN: (QUAD_3, LEFT),
                RIGHT: (QUAD_5, LEFT),
                LEFT: (QUAD_1, LEFT),
            },
            QUAD_3: {
                UP: (QUAD_1, UP),
                DOWN: (QUAD_5, DOWN),
                RIGHT: (QUAD_2, UP),
                LEFT: (QUAD_4, DOWN)
            },
            QUAD_4: {
                UP: (QUAD_3, RIGHT),
                DOWN: (QUAD_6, DOWN),
                RIGHT: (QUAD_5, RIGHT),
                LEFT: (QUAD_1, RIGHT)
            },
            QUAD_5: {
                UP: (QUAD_3, UP),
                DOWN: (QUAD_6, LEFT),
                RIGHT: (QUAD_2, LEFT),
                LEFT: (QUAD_4, LEFT)
            },
            QUAD_6: {
                UP: (QUAD_4, UP),
                DOWN: (QUAD_2, DOWN),
                RIGHT: (QUAD_5, UP),
                LEFT: (QUAD_1, DOWN)
            },
        }
        self.assertEqual(153203, part2('input.txt', inp))

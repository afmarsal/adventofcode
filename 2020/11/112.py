import copy


def next_coord(pos, delta, curr_grid):
    if 0 <= pos[0] + delta[0] < len(curr_grid) and 0 <= pos[1] + delta[1] < len(curr_grid[0]):
        return pos[0] + delta[0], pos[1] + delta[1]
    else:
        return -1, -1


def adj_occupied(y, x, curr_grid):
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    result = 0
    for delta in deltas:
        next_y, next_x = y, x
        while next_y >= 0:
            next_y, next_x = next_coord((next_y, next_x), delta, curr_grid)
            if next_y >= 0:
                if curr_grid[next_y][next_x] == '#':
                    result += 1
                    break
                elif curr_grid[next_y][next_x] == 'L':
                    break
    return result


def calc_next(y, x, curr_grid):
    if curr_grid[y][x] == 'L' and adj_occupied(y, x, curr_grid) == 0:
        return '#'
    elif curr_grid[y][x] == '#' and adj_occupied(y, x, curr_grid) >= 5:
        return 'L'
    else:
        return curr_grid[y][x]


def flatten(grid):
    return ''.join([c for l in grid for c in l])


def do_it(filename):
    with open(filename) as f:
        grid = [[c for c in line.strip()] for line in f]
    states = {flatten(grid)}
    curr_grid = grid
    new_grid = []
    while flatten(new_grid) not in states:
        states.add(flatten(new_grid))
        new_grid = copy.deepcopy(curr_grid)
        for y in range(0, len(curr_grid)):
            for x in range(0, len(curr_grid[y])):
                new_grid[y][x] = calc_next(y, x, curr_grid)

        # print_grid(new_grid)
        curr_grid = new_grid

    print_grid(new_grid)
    return flatten(new_grid).count('#')


def print_grid(grid):
    print('------')
    for l in grid:
        print(''.join(l))
    print('------')


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 2176

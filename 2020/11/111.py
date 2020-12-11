import copy


def adj_occupied(y, x, curr_grid):
    result = 0
    if y - 1 >= 0:
        if x - 1 >= 0:
            result += curr_grid[y - 1][x - 1] == '#'
        if x + 1 < len(curr_grid[y]):
            result += curr_grid[y - 1][x + 1] == '#'
        result += curr_grid[y - 1][x] == '#'
    if x - 1 >= 0:
        result += curr_grid[y][x - 1] == '#'
    if x + 1 < len(curr_grid[y]):
        result += curr_grid[y][x + 1] == '#'
    if y + 1 < len(curr_grid):
        if x - 1 >= 0:
            result += curr_grid[y + 1][x - 1] == '#'
        if x + 1 < len(curr_grid[y]):
            result += curr_grid[y + 1][x + 1] == '#'
        result += curr_grid[y + 1][x] == '#'
    return result


def calc_next(y, x, curr_grid):
    if curr_grid[y][x] == 'L' and adj_occupied(y, x, curr_grid) == 0:
        return '#'
    elif curr_grid[y][x] == '#' and adj_occupied(y, x, curr_grid) >= 4:
        return 'L'
    else:
        return curr_grid[y][x]


def flatten(grid):
    return ''.join([c for l in grid for c in l])


def do_it(filename):
    with open(filename) as f:
        grid = [[c for c in line.strip()] for line in f]
        print(grid)
    states = {flatten(grid)}
    curr_grid = grid
    print_grid(curr_grid)
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

# Result: 2412